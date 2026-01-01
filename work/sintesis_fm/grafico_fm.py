import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile

# Cargar archivo combinado
sample_rate, audio_data = wavfile.read("seno_vs_fm_vibrato.wav")
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# ============================================================================
# FIGURA 1: FM VIBRATO vs SENO LIMPIO
# ============================================================================
fig1, axs1 = plt.subplots(2, 1, figsize=(14, 8))

# Subplot 1: Seno plano
t1_start, t1_end = 0, 0.65
idx1 = np.logical_and(time >= t1_start, time <= t1_end)
axs1[0].plot(time[idx1], audio_data[idx1], linewidth=0.18, color='steelblue', alpha=0.9)
axs1[0].set_title("Señal sinusoidal sin efecto", fontsize=12)
axs1[0].set_ylabel("Amplitud")
axs1[0].grid(True, alpha=0.3)

# Subplot 2: FM vibrato
t2_start, t2_end = 0.90, 1.10
idx2 = np.logical_and(time >= t2_start, time <= t2_end)
axs1[1].plot(time[idx2], audio_data[idx2], linewidth=0.15, color='darkviolet', alpha=0.8)
axs1[1].set_title("FM Vibrato (N1=1.0, N2=1.0, I=2.0 semitones)", fontsize=12)
axs1[1].set_xlabel("Tiempo (s)")
axs1[1].set_ylabel("Amplitud")
axs1[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("fm_vibrato_comparison.png", dpi=150, bbox_inches='tight')
print("Gráfica FM vibrato guardada")
plt.close()

# ============================================================================
# FIGURA 2: COMPARACIÓN DE PARÁMETROS FM
# ============================================================================

# Leer las tres variantes
sr_c, aud_c = wavfile.read("fm_clarinete.wav")
sr_b, aud_b = wavfile.read("fm_campana.wav")

time_c = np.arange(len(aud_c)) / sr_c
time_b = np.arange(len(aud_b)) / sr_b

fig2, axs2 = plt.subplots(2, 2, figsize=(14, 8))

# Fila superior: Clarinete (N1=3, N2=1, I=2)
# Escala completa
t_start, t_end = 0.0, 2.0
idx_c = np.logical_and(time_c >= t_start, time_c <= t_end)
axs2[0,0].plot(time_c[idx_c], aud_c[idx_c], linewidth=0.3, color='coral')
axs2[0,0].set_title("Clarinete FM (N1=3.0, N2=1.0, I=2.0)", fontsize=11)
axs2[0,0].set_ylabel("Amplitud")
axs2[0,0].grid(True, alpha=0.3)

# Detalle clarinete
t_start, t_end = 0.05, 0.15
idx_c_det = np.logical_and(time_c >= t_start, time_c <= t_end)
axs2[0,1].plot(time_c[idx_c_det], aud_c[idx_c_det], linewidth=0.4, color='coral')
axs2[0,1].set_title("Detalle escala clarinete (0.05–0.15s)", fontsize=11)
axs2[0,1].set_ylabel("Amplitud")
axs2[0,1].grid(True, alpha=0.3)

# Fila inferior: Campana (N1=1, N2=1.414, I=14)
# Escala completa
t_start, t_end = 0.0, 2.2
idx_b = np.logical_and(time_b >= t_start, time_b <= t_end)
axs2[1,0].plot(time_b[idx_b], aud_b[idx_b], linewidth=0.3, color='mediumseagreen')
axs2[1,0].set_title("Campana FM (N1=1.0, N2=1.414, I=14.0)", fontsize=11)
axs2[1,0].set_xlabel("Tiempo (s)")
axs2[1,0].set_ylabel("Amplitud")
axs2[1,0].grid(True, alpha=0.3)

# Detalle campana
t_start, t_end = 0.0, 0.22
idx_b_det = np.logical_and(time_b >= t_start, time_b <= t_end)
axs2[1,1].plot(time_b[idx_b_det], aud_b[idx_b_det], linewidth=0.4, color='mediumseagreen')
axs2[1,1].set_title("Detalle primeras notas campana", fontsize=11)
axs2[1,1].set_xlabel("Tiempo (s)")
axs2[1,1].set_ylabel("Amplitud")
axs2[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("fm_parametros_comparison.png", dpi=150, bbox_inches='tight')
print("Gráfica FM parámetros guardada")
