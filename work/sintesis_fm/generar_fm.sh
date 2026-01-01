#!/bin/bash
SYNTH=../../build/release/src/synth

$SYNTH fm_vibrato.orc fm_vibrato.sco fm_vibrato.wav
$SYNTH fm_clarinete.orc fm_clarinete.sco fm_clarinete.wav
$SYNTH fm_campana.orc fm_campana.sco fm_campana.wav

echo "Generados: fm_vibrato.wav, fm_clarinete.wav, fm_campana.wav"
