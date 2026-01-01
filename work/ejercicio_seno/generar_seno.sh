#!/bin/bash

SYNTH=../../build/release/src/synth

echo "Generando seno.wav..."
$SYNTH seno.orc seno.sco seno.wav

echo "Archivo de audio generado correctamente."
