import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile

# ============================================================================
# FIGURA 1: TREMOLO
# ============================================================================
# Cargar archivo de audio
sample_rate, audio_data = wavfile.read("senoPlano_vs_senoTremolo.wav")

# Crear eje de tiempo
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# Definir los intervalos de tiempo
t1_start, t1_end = 0, 0.65
t2_start, t2_end = 0.90, 0.96  # Ventana muy corta para ver 2-3 periodos de trémolo

# Obtener los índices correspondientes
idx1 = np.logical_and(time >= t1_start, time <= t1_end)
idx2 = np.logical_and(time >= t2_start, time <= t2_end)

# Crear figura 2x1
fig, axs = plt.subplots(2, 1, figsize=(14, 8), sharey=True)

# Primer subplot: seno plano
axs[0].plot(time[idx1], audio_data[idx1], linewidth=0.18, color='steelblue', alpha=0.9)
axs[0].set_title("Señal sinusoidal sin efecto", fontsize=12)
axs[0].set_ylabel("Amplitud")
axs[0].grid(True, alpha=0.3)

# Segundo subplot: seno tremolo
axs[1].plot(time[idx2], audio_data[idx2], linewidth=0.15, color='coral', alpha=0.8)
axs[1].set_title("Señal sinusoidal con trémolo (fm=5Hz, índice=80%)", fontsize=12)
axs[1].set_xlabel("Tiempo (s)")
axs[1].set_ylabel("Amplitud")
axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("senoPlano_vs_senoTremolo.png", dpi=150, bbox_inches='tight')
print("Gráfica 1 guardada: senoPlano_vs_senoTremolo.png")

# ============================================================================
# FIGURA 2: VIBRATO
# ============================================================================
# Cargar archivo de audio
sample_rate, audio_data = wavfile.read("senoPlano_vs_senoVibrato.wav")

# Crear eje de tiempo
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# Definir los intervalos de tiempo
t1_start, t1_end = 0, 0.65
t2_start, t2_end = 0.96, 1.00  # Ventana aún más reducida para ver la modulación
t3_start, t3_end = 0.0, 0.025
t4_start, t4_end = 0.74, 0.80  # Ventana más amplia

# Obtener los índices correspondientes
idx1 = np.logical_and(time >= t1_start, time <= t1_end)
idx2 = np.logical_and(time >= t2_start, time <= t2_end)
idx3 = np.logical_and(time >= t3_start, time <= t3_end)
idx4 = np.logical_and(time >= t4_start, time <= t4_end)

# Crear figura 2x2
fig, axs = plt.subplots(2, 2, figsize=(14, 8), sharey=True)

# Primer subplot: seno plano
axs[0,0].plot(time[idx1], audio_data[idx1], linewidth=0.18, color='steelblue', alpha=0.9)
axs[0,0].set_title("Señal sinusoidal sin efecto", fontsize=11)
axs[0,0].set_ylabel("Amplitud")
axs[0,0].grid(True, alpha=0.3)

# Segundo subplot: seno vibrato
axs[1,0].plot(time[idx2], audio_data[idx2], linewidth=0.08, color='mediumorchid', alpha=0.75)
axs[1,0].set_title("Señal sinusoidal con vibrato (fm=6Hz, desv=50cents)", fontsize=11)
axs[1,0].set_xlabel("Tiempo (s)")
axs[1,0].set_ylabel("Amplitud")
axs[1,0].grid(True, alpha=0.3)

# Tercer subplot: curva ataque sin efectos
axs[0,1].plot(time[idx3], audio_data[idx3], linewidth=0.4, color='steelblue')
axs[0,1].set_title("Detalle de la envolvente sin efecto", fontsize=11)
axs[0,1].set_ylabel("Amplitud")
axs[0,1].grid(True, alpha=0.3)

# Cuarto subplot: curva ataque con vibrato
axs[1,1].plot(time[idx4], audio_data[idx4], linewidth=0.4, color='mediumorchid')
axs[1,1].set_title("Detalle de la envolvente con vibrato (fm=6Hz, desv=50cents)", fontsize=11)
axs[1,1].set_xlabel("Tiempo (s)")
axs[1,1].set_ylabel("Amplitud")
axs[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("senoPlano_vs_senoVibrato.png", dpi=150, bbox_inches='tight')
print("Gráfica 2 guardada: senoPlano_vs_senoVibrato.png")
