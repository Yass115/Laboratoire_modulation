import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import pandas as pd

st.title("ÉCHANTILLONNAGE DU SIGNAL")

# ---------------------------------------------------------------------
# PARAMÈTRES
# ---------------------------------------------------------------------
f = st.sidebar.slider("Fréquence du signal (Hz)", 1, 3000, 100)
fs = st.sidebar.slider("Fréquence d'échantillonnage (Hz)", 50, 20000, 800)
duration = st.sidebar.slider("Durée (s)", 0.05, 1.0, 0.2)
noise = st.sidebar.slider("Bruit (aléatoire) sur les échantillons", 0.0, 1.0, 0.0)
jitter = st.sidebar.slider("Jitter d’échantillonnage (%)", 0.0, 1.0, 0.0)

# ---------------------------------------------------------------------
# SIGNAL ANALOGIQUE
# ---------------------------------------------------------------------
t = np.linspace(0, duration, 20000)
x = np.sin(2 * np.pi * f * t)

# ---------------------------------------------------------------------
# ÉCHANTILLONNAGE
# ---------------------------------------------------------------------
ts = np.arange(0, duration, 1/fs)

# jitter temporel
ts = ts + (np.random.randn(len(ts)) * jitter * (1/fs))

samples = np.sin(2 * np.pi * f * ts) + noise * np.random.randn(len(ts))

# ---------------------------------------------------------------------
# INTERPOLATION SINC
# ---------------------------------------------------------------------
x_sinc = np.zeros_like(t)
for n, s in enumerate(samples):
    x_sinc += s * np.sinc((t - ts[n]) * fs)

# ---------------------------------------------------------------------
# GRAPHIQUE SIGNAL + ÉCHANTILLONS + SINC
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t, x, label="Signal analogique")
ax.stem(ts, samples, linefmt='r-', markerfmt='ro', basefmt=' ', label="Échantillons")
ax.plot(t, x_sinc, label="Interpolation Sinc", color='green', alpha=0.7)
ax.legend()
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Amplitude")
st.pyplot(fig)

# ---------------------------------------------------------------------
# FFT
# ---------------------------------------------------------------------
st.subheader("FFT du signal échantillonné")

N = len(samples)
freqs = np.fft.fftfreq(N, d=1/fs)
fft_vals = np.abs(np.fft.fft(samples))

fig_fft, ax_fft = plt.subplots(figsize=(12,4))
ax_fft.plot(freqs[:N//2], fft_vals[:N//2])
ax_fft.set_xlabel("Fréquence (Hz)")
ax_fft.set_ylabel("Amplitude")
st.pyplot(fig_fft)

# ---------------------------------------------------------------------
# SPECTROGRAMME
# ---------------------------------------------------------------------
st.subheader("Spectrogramme")
f_spectro, t_spectro, Sxx = spectrogram(samples, fs, nperseg=128, noverlap=64)

fig_s, ax_s = plt.subplots(figsize=(12,4))
ax_s.pcolormesh(t_spectro, f_spectro, Sxx, shading='gouraud')
ax_s.set_ylabel("Fréquence (Hz)")
ax_s.set_xlabel("Temps (s)")
st.pyplot(fig_s)

# ---------------------------------------------------------------------
# EXPORT CSV
# ---------------------------------------------------------------------
df_sig = pd.DataFrame({"t": t, "signal": x})
df_samp = pd.DataFrame({"ts": ts, "samples": samples})

st.download_button("Télécharger le signal analogique", df_sig.to_csv().encode(), "signal.csv")
st.download_button("Télécharger les échantillons", df_samp.to_csv().encode(), "echantillons.csv")
