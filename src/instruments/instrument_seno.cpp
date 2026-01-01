#include <iostream>
#include <math.h>
#include "instrument_seno.h"
#include "keyvalue.h"

#include <stdlib.h>

using namespace upc;
using namespace std;

InstrumentSeno::InstrumentSeno(const std::string &param) 
  : adsr(SamplingRate, param) {
  bActive = false;
  x.resize(BSIZE);

  KeyValue kv(param);
  int N;

  if (!kv.to_int("N",N))
    N = 512; // tabla de mayor resolución para seno
  
  // Crear tabla de búsqueda con un período completo de onda sinusoidal
  tbl_seno.resize(N);
  float paso = 2 * M_PI / (float) N;
  float fase = 0;
  for (int i = 0; i < N; ++i) {
    tbl_seno[i] = sin(fase);
    fase += paso;
  }
}


void InstrumentSeno::command(long cmd, long note, long vel) {
  if (cmd == 9) {		// Tecla presionada: comienza ataque
    bActive = true;
    adsr.start();
    phase = 0;
    float f0 = 440.0 * pow(2.0, (note - 69.0) / 12.0); // Nota MIDI a frecuencia
    incr_phase = 2*M_PI * (f0 / SamplingRate) * tbl_seno.size();
    A = vel / 127.;
  }
  else if (cmd == 8) {	// Tecla liberada: sustain termina, release comienza
    adsr.stop();
  }
  else if (cmd == 0) {	// Sonido extinguido sin esperar release completo
    adsr.end();
  }
}


const vector<float> & InstrumentSeno::synthesize() {
  if (not adsr.active()) {
    x.assign(x.size(), 0);
    bActive = false;
    return x;
  }
  else if (not bActive)
    return x;

  for (unsigned int i=0; i<x.size(); ++i) {
    // Búsqueda en tabla con interpolación lineal
    int indice = (int) phase;
    float frac = phase - indice;
    int indice_sig = (indice + 1) % tbl_seno.size();
    
    float valor_actual = tbl_seno[indice];
    float valor_siguiente = tbl_seno[indice_sig];
    float interpolado = valor_actual + frac * (valor_siguiente - valor_actual);
    
    x[i] = A * interpolado;
    phase += incr_phase;
    
    while (phase >= tbl_seno.size())
      phase -= tbl_seno.size();
  }
  adsr(x); // aplicar envolvente ADSR a la señal

  return x;
}
