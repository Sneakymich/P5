#!/bin/bash

# Script para generar We Are Family con orquestación multi-instrumento

# Ruta del sintetizador
SYNTH="../../build/release/src/synth"

# Verificar que existe el sintetizador
if [ ! -f "$SYNTH" ]; then
    echo "Error: No se encuentra el sintetizador en $SYNTH"
    echo "Ejecuta 'make release' desde el directorio raíz del proyecto"
    exit 1
fi

# Verificar que existe el score
if [ ! -f "../../samples/WeAreFamily_fixed.sco" ]; then
    echo "Error: No se encuentra WeAreFamily_fixed.sco en samples/"
    exit 1
fi

echo "Generando We Are Family (Sister Sledge - Disco/Funk)..."
echo "=============================================="
echo ""
echo "Orquestación (3 pistas, canales 0-2 filtrados):"
echo "  - Pista 1: Bajo (FM profundo, N1=1, I=3)"
echo "  - Pista 2: Teclado melódico (Seno)"
echo "  - Pista 3: Cuerdas (FM clarinete con vibrato)"
echo ""

# Generar audio con ganancia ajustada para 3 pistas
$SYNTH WeAreFamily.orc ../../samples/WeAreFamily_fixed.sco WeAreFamily.wav -g 0.12

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Generado: WeAreFamily.wav"
    echo ""
    echo "Comando utilizado:"
    echo "$SYNTH WeAreFamily.orc ../../samples/WeAreFamily_fixed.sco WeAreFamily.wav -g 0.12"
else
    echo ""
    echo "✗ Error al generar WeAreFamily.wav"
    exit 1
fi
