import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Leer archivos de audio
rate1, data1 = wav.read("generico.wav")
rate2, data2 = wav.read("percusivo1.wav")
rate3, data3 = wav.read("percusivo2.wav")
rate4, data4 = wav.read("plano.wav")

# Crear tiempo en segundos
time1 = np.arange(len(data1)) / rate1
time2 = np.arange(len(data2)) / rate2
time3 = np.arange(len(data3)) / rate3
time4 = np.arange(len(data4)) / rate4

# Crear figura con 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Envolventes ADSR - Comparación de Instrumentos', fontsize=16, fontweight='bold')

# Plot 1: Generico
axs[0, 0].plot(time1, data1, linewidth=0.8, color='blue')
axs[0, 0].set_title('Instrumento Genérico')
axs[0, 0].set_xlabel('Tiempo (s)')
axs[0, 0].set_ylabel('Amplitud')
axs[0, 0].grid(True, alpha=0.3)

# Plot 2: Percusivo1
axs[0, 1].plot(time2, data2, linewidth=0.8, color='green')
axs[0, 1].set_title('Percusivo 1 (nota sostenida)')
axs[0, 1].set_xlabel('Tiempo (s)')
axs[0, 1].set_ylabel('Amplitud')
axs[0, 1].grid(True, alpha=0.3)

# Plot 3: Percusivo2
axs[1, 0].plot(time3, data3, linewidth=0.8, color='red')
axs[1, 0].set_title('Percusivo 2 (release anticipado)')
axs[1, 0].set_xlabel('Tiempo (s)')
axs[1, 0].set_ylabel('Amplitud')
axs[1, 0].grid(True, alpha=0.3)

# Plot 4: Plano
axs[1, 1].plot(time4, data4, linewidth=0.8, color='purple')
axs[1, 1].set_title('Instrumento Plano (cuerdas/viento)')
axs[1, 1].set_xlabel('Tiempo (s)')
axs[1, 1].set_ylabel('Amplitud')
axs[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('envolventes_adsr.png', dpi=150)
plt.show()

print("Gráfica generada: envolventes_adsr.png")
