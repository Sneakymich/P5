#include <iostream>
#include <math.h>
#include "instrument_fm.h"
#include "keyvalue.h"

using namespace upc;
using namespace std;

InstrumentFM::InstrumentFM(const std::string &param)
  : adsr(SamplingRate, param) {
  bActive = false;
  x.resize(BSIZE);

  // Valores por defecto
  N1 = 1.0f;
  N2 = 1.0f;
  I_semitones = 2.0f;

  KeyValue kv(param);
  kv.to_float("N1", N1);
  kv.to_float("N2", N2);
  kv.to_float("I", I_semitones);

  carrier_phase = 0.0f;
  mod_phase = 0.0f;
  carrier_inc = 0.0f;
  mod_inc = 0.0f;
  beta = 0.0f;
  A = 0.0f;
}

void InstrumentFM::command(long cmd, long note, long vel) {
  if (cmd == 9) { // Note on
    bActive = true;
    adsr.start();
    carrier_phase = 0.0f;
    mod_phase = 0.0f;

    // Frecuencia base a partir de la nota MIDI
    float f0 = 440.0f * pow(2.0f, (note - 69.0f) / 12.0f);
    float fc = N1 * f0;
    float fm = N2 * f0;

    carrier_inc = 2.0f * M_PI * fc / SamplingRate;
    mod_inc = 2.0f * M_PI * fm / SamplingRate;

    // Desviación en Hz a partir de semitonos, aplicada sobre fc
    float dev_hz = fc * (pow(2.0f, I_semitones / 12.0f) - 1.0f);
    beta = (fm != 0.0f) ? dev_hz / fm : 0.0f;

    A = vel / 127.0f;
  }
  else if (cmd == 8) { // Note off
    adsr.stop();
  }
  else if (cmd == 0) { // Sound extinguished immediately
    adsr.end();
  }
}

const vector<float> & InstrumentFM::synthesize() {
  if (not adsr.active()) {
    x.assign(x.size(), 0.0f);
    bActive = false;
    return x;
  }
  else if (not bActive)
    return x;

  for (unsigned int i = 0; i < x.size(); ++i) {
    float sample = sin(carrier_phase + beta * sin(mod_phase));
    x[i] = A * sample;

    carrier_phase += carrier_inc;
    mod_phase += mod_inc;

    if (carrier_phase > 2.0f * M_PI)
      carrier_phase -= 2.0f * M_PI;
    if (mod_phase > 2.0f * M_PI)
      mod_phase -= 2.0f * M_PI;
  }

  adsr(x);
  return x;
}
