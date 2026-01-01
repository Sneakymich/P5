#ifndef INSTRUMENT_FM
#define INSTRUMENT_FM

#include <vector>
#include <string>
#include "instrument.h"
#include "envelope_adsr.h"

namespace upc {
  class InstrumentFM : public Instrument {
    EnvelopeADSR adsr;
    float carrier_phase;
    float mod_phase;
    float carrier_inc;
    float mod_inc;
    float beta;   // modulation index (radians), derived from semitone deviation
    float A;
    float N1;
    float N2;
    float I_semitones;
  public:
    InstrumentFM(const std::string &param = "");
    void command(long cmd, long note, long velocity = 1);
    const std::vector<float> & synthesize();
    bool is_active() const { return bActive; }
  };
}

#endif
