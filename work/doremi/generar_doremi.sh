#!/bin/bash

SYNTH=../../build/release/src/synth

echo "Generando escalas FM en doremi/"

$SYNTH clarinete.orc doremi.sco clarinete.wav
$SYNTH campana.orc doremi.sco campana.wav

echo "Generados: clarinete.wav y campana.wav"
