#!/bin/bash

SYNTH=../../build/release/src/synth

echo "Generando envolvente_adsr.wav..."
$SYNTH envolvente_adsr.orc envolvente_adsr.sco envolvente_adsr.wav

echo "Generando generico.wav..."
$SYNTH envolvente_adsr.orc generico.sco generico.wav

echo "Generando percusivo1.wav..."
$SYNTH envolvente_adsr.orc percusivo1.sco percusivo1.wav

echo "Generando percusivo2.wav..."
$SYNTH envolvente_adsr.orc percusivo2.sco percusivo2.wav

echo "Generando plano.wav..."
$SYNTH envolvente_adsr.orc plano.sco plano.wav

echo "Archivos generados correctamente."
