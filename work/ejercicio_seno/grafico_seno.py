import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Crear tabla de búsqueda idéntica a la del instrumento
N = 512
tbl_seno = np.sin(2 * np.pi * np.arange(N) / N)

# Plot 1: Tabla de búsqueda y señal interpolada
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Síntesis por Tabla Lookup - InstrumentSeno', fontsize=16, fontweight='bold')

# Subplot 1: Tabla completa con puntos
ax = axs[0, 0]
indices = np.arange(N)
ax.scatter(indices, tbl_seno, s=10, alpha=0.6, color='blue', label='Puntos tabla')
ax.plot(indices, tbl_seno, color='blue', alpha=0.3, linewidth=0.5)
ax.set_xlabel('Índice tabla')
ax.set_ylabel('Amplitud')
ax.set_title('Tabla de búsqueda (512 puntos)')
ax.grid(True, alpha=0.3)
ax.legend()

# Subplot 2: Vista detallada zona pequeña
ax = axs[0, 1]
window_start, window_end = 50, 100
indices_window = np.arange(window_start, window_end)

# Puntos tabla
ax.scatter(indices_window, tbl_seno[window_start:window_end], s=40, alpha=0.8, 
          color='blue', label='Puntos tabla', zorder=3)

# Interpolación lineal entre puntos
fine_indices = np.linspace(window_start, window_end-1, 500)
interpolated = []
for idx in fine_indices:
    i_int = int(idx)
    frac = idx - i_int
    i_next = (i_int + 1) % N
    val = tbl_seno[i_int] + frac * (tbl_seno[i_next] - tbl_seno[i_int])
    interpolated.append(val)

ax.plot(fine_indices, interpolated, color='red', linewidth=2, label='Interpolación lineal', zorder=2)
ax.set_xlabel('Índice tabla')
ax.set_ylabel('Amplitud')
ax.set_title('Detalle: Interpolación entre puntos')
ax.grid(True, alpha=0.3)
ax.legend()

# Subplot 3: Método de interpolación
ax = axs[1, 0]
ax.axis('off')
metodo = """
MÉTODO: Interpolación Lineal

Para cada muestra de salida:
1. Calcular índice flotante: phase
2. Obtener parte entera e fracción:
   idx = int(phase)
   frac = phase - idx
   
3. Leer dos valores consecutivos:
   v1 = tabla[idx]
   v2 = tabla[idx+1]
   
4. Interpolar linealmente:
   salida = v1 + frac * (v2 - v1)
   
VENTAJAS:
✓ Suave entre puntos tabla
✓ Bajo costo computacional
✓ Reduce aliasing

PARÁMETROS:
• Tamaño tabla: 512 puntos
• Resolución: ±2.44 cents
"""
ax.text(0.1, 0.9, metodo, transform=ax.transAxes, fontsize=10,
       verticalalignment='top', fontfamily='monospace',
       bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Subplot 4: Señal de audio si existe
ax = axs[1, 1]
try:
    rate, data = wav.read('seno.wav')
    time = np.arange(len(data)) / rate
    ax.plot(time, data, color='purple', linewidth=0.5, alpha=0.7)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Amplitud')
    ax.set_title('Señal generada (seno.wav)')
    ax.grid(True, alpha=0.3)
except:
    ax.text(0.5, 0.5, 'Ejecutar generar_seno.sh primero\npara generar seno.wav', 
           ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.set_title('Audio generado')

plt.tight_layout()
plt.savefig('tabla_lookup_seno.png', dpi=150)
print("Gráfica guardada: tabla_lookup_seno.png")
