#!/usr/bin/env python3
# Convierte formato NoteOn/NoteOff a formato de 5 columnas para synth

import sys
import re

def convert_sco(input_file, output_file):
    last_time = 0.0  # Tiempo del último evento
    
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            
            # Saltar comentarios y líneas vacías
            if line.startswith('//') or line.startswith('#') or not line:
                continue
            
            # Saltar líneas de control que no son notas
            if line.startswith('Volume') or line.startswith('ControlChange'):
                continue
            
            # Parsear NoteOn
            match_on = re.match(r'NoteOn\s+=([0-9.]+)\s+(\d+)\s+(\d+)\s+(\d+)', line)
            if match_on:
                tiempo_float = float(match_on.group(1))
                canal = int(match_on.group(2))
                nota = int(match_on.group(3))
                vel = int(match_on.group(4))
                
                # FILTRO: Solo canales 0, 1, 2 (evitar percusión canal 9 y otros)
                if canal not in [0, 1, 2]:
                    continue
                
                canal_out = canal + 1  # Convertir a 1-based
                
                # Calcular delta (tiempo relativo al último evento)
                delta = tiempo_float - last_time
                delta_ticks = int(delta * 200)  # Factor ALTO para ralentizar
                last_time = tiempo_float
                
                f_out.write(f"{delta_ticks}\t9\t{canal_out}\t{nota}\t{vel}\n")
                continue
            
            # Parsear NoteOff
            match_off = re.match(r'NoteOff\s+=([0-9.]+)\s+(\d+)\s+(\d+)\s+(\d+)', line)
            if match_off:
                tiempo_float = float(match_off.group(1))
                canal = int(match_off.group(2))
                nota = int(match_off.group(3))
                vel = int(match_off.group(4))
                
                # FILTRO: Solo canales 0, 1, 2
                if canal not in [0, 1, 2]:
                    continue
                
                canal_out = canal + 1  # Convertir a 1-based
                
                # Calcular delta (tiempo relativo al último evento)
                delta = tiempo_float - last_time
                delta_ticks = int(delta * 200)  # Factor ALTO para ralentizar
                last_time = tiempo_float
                
                f_out.write(f"{delta_ticks}\t8\t{canal_out}\t{nota}\t{vel}\n")
                continue

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: convert_sco.py <input.sco> <output.sco>")
        sys.exit(1)
    
    convert_sco(sys.argv[1], sys.argv[2])
    print(f"Convertido: {sys.argv[1]} -> {sys.argv[2]}")
