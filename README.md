PAV - P5: síntesis musical polifónica
=====================================

Íñigo Michelena, Enric Mayné.

Obtenga su copia del repositorio de la práctica accediendo a [Práctica 5](https://github.com/albino-pav/P5) 
y pulsando sobre el botón `Fork` situado en la esquina superior derecha. A continuación, siga las
instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para crear una rama con el apellido de
los integrantes del grupo de prácticas, dar de alta al resto de integrantes como colaboradores del proyecto
y crear la copias locales del repositorio.

Como entrega deberá realizar un *pull request* con el contenido de su copia del repositorio. Recuerde que
los ficheros entregados deberán estar en condiciones de ser ejecutados con sólo ejecutar:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.sh
  make release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A modo de memoria de la práctica, complete, en este mismo documento y usando el formato *markdown*, los
ejercicios indicados.

Ejercicios.
-----------

### Envolvente ADSR.

Tomando como modelo un instrumento sencillo (puede usar el InstrumentDumb), genere cuatro instrumentos que
permitan visualizar el funcionamiento de la curva ADSR.

* Un instrumento con una envolvente ADSR genérica, para el que se aprecie con claridad cada uno de sus
  parámetros: ataque (A), caída (D), mantenimiento (S) y liberación (R).
* Un instrumento *percusivo*, como una guitarra o un piano, en el que el sonido tenga un ataque rápido, no
  haya mantenimiemto y el sonido se apague lentamente.
  - Para un instrumento de este tipo, tenemos dos situaciones posibles:
    * El intérprete mantiene la nota *pulsada* hasta su completa extinción.
    * El intérprete da por finalizada la nota antes de su completa extinción, iniciándose una disminución
	  abrupta del sonido hasta su finalización.
  - Debera representar en esta memoria **ambos** posibles finales de la nota.
* Un instrumento *plano*, como los de cuerdas frotadas (violines y semejantes) o algunos de viento. En
  ellos, el ataque es relativamente rápido hasta alcanzar el nivel de mantenimiento (sin sobrecarga), y la
  liberación también es bastante rápida.

Para los cuatro casos, deberá incluir una gráfica en la que se visualice claramente la curva ADSR. Deberá
añadir la información necesaria para su correcta interpretación, aunque esa información puede reducirse a
colocar etiquetas y títulos adecuados en la propia gráfica (se valorará positivamente esta alternativa).

![](work/ejercicio_envolvente_adsr/envolventes_adsr.png)

### Instrumentos Dumb y Seno.

Implemente el instrumento `Seno` tomando como modelo el `InstrumentDumb`. La señal **deberá** formarse
mediante búsqueda de los valores en una tabla.

- Incluya, a continuación, el código del fichero `seno.cpp` con los métodos de la clase Seno.

```cpp
InstrumentSeno::InstrumentSeno(const std::string &param) 
  : adsr(SamplingRate, param) {
  bActive = false;
  x.resize(BSIZE);

  KeyValue kv(param);
  int N;

  if (!kv.to_int("N",N))
    N = 512; // tabla de mayor resolución para seno
  
  // Crear tabla de búsqueda con un período completo de onda sinusoidal
  tbl_seno.resize(N);
  float paso = 2 * M_PI / (float) N;
  float fase = 0;
  for (int i = 0; i < N; ++i) {
    tbl_seno[i] = sin(fase);
    fase += paso;
  }
}

```

- Explique qué método se ha seguido para asignar un valor a la señal a partir de los contenidos en la tabla,
  e incluya una gráfica en la que se vean claramente (use pelotitas en lugar de líneas) los valores de la
  tabla y los de la señal generada.

![](work/ejercicio_seno/tabla_lookup_seno.png)

- Si ha implementado la síntesis por tabla almacenada en fichero externo, incluya a continuación el código
  del método `command()`.

```cpp

void InstrumentSeno::command(long cmd, long note, long vel) {
  if (cmd == 9) {		// Tecla presionada: comienza ataque
    bActive = true;
    adsr.start();
    phase = 0;
    float f0 = 440.0 * pow(2.0, (note - 69.0) / 12.0); // Nota MIDI a frecuencia
    incr_phase = 2*M_PI * (f0 / SamplingRate) * tbl_seno.size();
    A = vel / 127.;
  }
  else if (cmd == 8) {	// Tecla liberada: sustain termina, release comienza
    adsr.stop();
  }
  else if (cmd == 0) {	// Sonido extinguido sin esperar release completo
    adsr.end();
  }
}

```

### Efectos sonoros.

- Incluya dos gráficas en las que se vean, claramente, el efecto del trémolo y el vibrato sobre una señal
  sinusoidal. Deberá explicar detalladamente cómo se manifiestan los parámetros del efecto (frecuencia e
  índice de modulación) en la señal generada (se valorará que la explicación esté contenida en las propias
  gráficas, sin necesidad de *literatura*).

![](work/ejercicio_efectos/senoPlano_vs_senoTremolo.png)
![](work/ejercicio_efectos/senoPlano_vs_senoVibrato.png)

- Si ha generado algún efecto por su cuenta, explique en qué consiste, cómo lo ha implementado y qué
  resultado ha producido. Incluya, en el directorio `work/ejemplos`, los ficheros necesarios para apreciar
  el efecto, e indique, a continuación, la orden necesaria para generar los ficheros de audio usando el
  programa `synth`.

### Síntesis FM.

Construya un instrumento de síntesis FM, según las explicaciones contenidas en el enunciado y el artículo
de [John M. Chowning](https://web.eecs.umich.edu/~fessler/course/100/misc/chowning-73-tso.pdf). El
instrumento usará como parámetros **básicos** los números `N1` y `N2`, y el índice de modulación `I`, que
deberá venir expresado en semitonos.

- Use el instrumento para generar un vibrato de *parámetros razonables* e incluya una gráfica en la que se
  vea, claramente, la correspondencia entre los valores `N1`, `N2` e `I` con la señal obtenida.

![](work/sintesis_fm/fm_vibrato_comparison.png)

- Use el instrumento para generar un sonido tipo clarinete y otro tipo campana. Tome los parámetros del
  sonido (N1, N2 e I) y de la envolvente ADSR del citado artículo. Con estos sonidos, genere sendas escalas
  diatónicas (fichero `doremi.sco`) y ponga el resultado en los ficheros `work/doremi/clarinete.wav` y
  `work/doremi/campana.work`.

![](work/sintesis_fm/fm_parametros_comparison.png)

  * También puede colgar en el directorio work/doremi otras escalas usando sonidos *interesantes*. Por
    ejemplo, violines, pianos, percusiones, espadas láser de la
	[Guerra de las Galaxias](https://www.starwars.com/), etc.

### Orquestación usando el programa synth.

Use el programa `synth` para generar canciones a partir de su partitura MIDI. Como mínimo, deberá incluir la
*orquestación* de la canción *You've got a friend in me* (fichero `ToyStory_A_Friend_in_me.sco`) del genial
[Randy Newman](https://open.spotify.com/artist/3HQyFCFFfJO3KKBlUfZsyW/about).

- En este triste arreglo, la pista 1 corresponde al instrumento solista (puede ser un piano, flautas,
  violines, etc.), y la 2 al bajo (bajo eléctrico, contrabajo, tuba, etc.).
- Coloque el resultado, junto con los ficheros necesarios para generarlo, en el directorio `work/music`.
- Indique, a continuación, la orden necesaria para generar la señal (suponiendo que todos los archivos
  necesarios están en directorio indicado).

  "./work/music/generar_music.sh".  

  Esta orden ejecuta un script que genera la música orquestada de la canción "You've got a friend in me" utilizando el programa synth con los archivos de partitura, instrumentos y efectos adecuados. El código del script es el siguiente:

  ```sh
  #!/bin/bash
  SYNTH=../../build/release/src/synth

  # Generar ToyStory con parámetro de gain 0.1
  $SYNTH ToyStory.orc ../../samples/ToyStory_A_Friend_in_me.sco ToyStory.wav -g 0.1

  echo "Generado: ToyStory.wav"
  ```

También puede orquestar otros temas más complejos, como la banda sonora de *Hawaii5-0* o el villacinco de
John Lennon *Happy Xmas (War Is Over)* (fichero `The_Christmas_Song_Lennon.sco`), o cualquier otra canción
de su agrado o composición. Se valorará la riqueza instrumental, su modelado y el resultado final.
- Coloque los ficheros generados, junto a sus ficheros `score`, `instruments` y `efffects`, en el directorio
  `work/music`.
- Indique, a continuación, la orden necesaria para generar cada una de las señales usando los distintos
  ficheros.

  "./work/music/generar_hawaii50.sh". 

  Esta orden ejecuta un script que genera la música orquestada de la serie "Hawaii5-0" utilizando el programa synth con los archivos de partitura, instrumentos y efectos adecuados. El código del script es el siguiente:

  ```sh
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
  ```


  "./work/music/generar_wearefamily.sh".  

  Esta orden ejecuta un script que genera la música orquestada de la canción "We Are Family" utilizando el programa synth con los archivos de partitura, instrumentos y efectos adecuados. El código del script es el siguiente:

  ```sh

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
  ``` 
> NOTA:
>
> No olvide escuchar el resultado generado y comprobar que no se producen ruidos extraños o distorsiones.
> Sobre todo, tenga en cuenta la salud auditiva de quien será encargado de corregir su trabajo.
