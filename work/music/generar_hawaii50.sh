#!/bin/bash

# Ruta del ejecutable synth
SYNTH="../../build/release/src/synth"

echo "Generando Hawaii 5-0 Theme (The Ventures - Surf Rock)..."
echo "=============================================="
echo ""
echo "Orquestación (9 canales - orquestación completa):"
echo "  - Canal 14: Melodía principal (624 notas) - FM brillante I=8"
echo "  - Canal 3: Línea secundaria (538 notas) - FM clarinete I=6"
echo "  - Canales 9-10: Percusión (380 notas c/u) - FM percusivo I=10"
echo "  - Canal 5: Bajo (378 notas) - FM profundo I=3"
echo "  - Canal 8: Acompañamiento (366 notas) - Seno"
echo "  - Canales 12-13: Armonía/bells (266 notas c/u) - FM campana I=7"
echo "  - Canal 7: Complemento melódico (246 notas) - FM armonía I=4"
echo ""

# Generar audio con 9 pistas (ganancia reducida)
$SYNTH Hawaii50.orc ../../samples/Hawaii5-0.sco Hawaii50.wav -g 0.06

# Verificar si se generó correctamente
if [ -f Hawaii50.wav ]; then
    echo ""
    echo "✓ Generado: Hawaii50.wav"
    echo ""
    echo "Comando utilizado:"
    echo "$SYNTH Hawaii50.orc ../../samples/Hawaii5-0.sco Hawaii50.wav -g 0.06"
    echo ""
    ls -lh Hawaii50.wav
else
    echo ""
    echo "✗ ERROR: No se pudo generar Hawaii50.wav"
    exit 1
fi
