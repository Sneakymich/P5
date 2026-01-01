#!/bin/bash
SYNTH=../../build/release/src/synth

# Generar ToyStory con parámetro de gain 0.1
$SYNTH ToyStory.orc ../../samples/ToyStory_A_Friend_in_me.sco ToyStory.wav -g 0.1

echo "Generado: ToyStory.wav"
