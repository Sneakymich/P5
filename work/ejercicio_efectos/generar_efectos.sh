#!/bin/bash

SYNTH=../../build/release/src/synth

echo "Generando sin_efecto.wav..."
$SYNTH sin_efecto.orc sin_efecto.sco sin_efecto.wav

echo "Generando tremolo.wav..."
$SYNTH tremolo.orc tremolo.sco tremolo.wav

echo "Generando vibrato.wav..."
$SYNTH vibrato.orc vibrato.sco vibrato.wav

echo "Generando senoPlano_vs_senoTremolo.wav (combinado)..."
$SYNTH tremolo.orc senoPlano_vs_senoTremolo.sco senoPlano_vs_senoTremolo.wav

echo "Generando senoPlano_vs_senoVibrato.wav (combinado)..."
$SYNTH vibrato.orc senoPlano_vs_senoVibrato.sco senoPlano_vs_senoVibrato.wav

echo "Archivos de audio generados correctamente."
