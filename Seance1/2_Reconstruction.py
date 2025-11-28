import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import pandas as pd

st.title("RECONSTRUCTION DU SIGNAL")


# PARAMÈTRES

f = st.sidebar.slider("Fréquence du signal original (Hz)", 1, 3000, 100)
fs = st.sidebar.slider("Fréquence d'échantillonnage (Hz)", 50, 20000, 800)
duration = st.sidebar.slider("Durée (s)", 0.05, 1.0, 0.2)

method = st.sidebar.radio("Méthode de reconstruction",
                          ["Interpolation Sinc", "ZOH", "Linéaire", "Filtre RC"])

RC_fc = st.sidebar.slider("Fréquence de coupure RC (Hz)", 10, 2000, 200)


# SIGNAL ORIGINAL & ÉCHANTILLONS

t = np.linspace(0, duration, 20000)
x = np.sin(2 * np.pi * f * t)

ts = np.arange(0, duration, 1/fs)
samples = np.sin(2 * np.pi * f * ts)


# RECONSTRUCTION
if method == "Interpolation Sinc":
    xr = np.zeros_like(t)
    for n, s in enumerate(samples):
        xr += s * np.sinc((t - ts[n]) * fs)

elif method == "ZOH":
    xr = np.interp(t, ts, samples)

elif method == "Linéaire":
    xr = np.interp(t, ts, samples)

elif method == "Filtre RC":
    RC = 1/(2*np.pi*RC_fc)
    y = np.zeros(len(samples))
    for i in range(1, len(samples)):
        y[i] = y[i-1] + (1/fs) * (-(y[i-1]/RC) + samples[i])
    xr = np.interp(t, ts, y)


# AFFICHAGE

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t, x, label="Signal original")
ax.stem(ts, samples, linefmt="r-", markerfmt="ro", basefmt=" ", label="Échantillons")
ax.plot(t, xr, label=f"Reconstruction ({method})")
ax.legend()
st.pyplot(fig)


# SPECTROGRAMME (pour avoir le graphe de la fréquence en fonction du temps, normalement pas trop de variation)

f_s, t_s, Sxx = spectrogram(xr, fs*20, nperseg=256, noverlap=128)

fig2, ax2 = plt.subplots(figsize=(12,4))
ax2.pcolormesh(t_s, f_s, Sxx, shading='gouraud')
ax2.set_title("Spectrogramme du signal reconstruit")
ax2.set_xlabel("Temps (s)")
ax2.set_ylabel("Fréquences (Hz)")
st.pyplot(fig2)


# EXPORT

df_out = pd.DataFrame({"t": t, "signal_reconstruit": xr})
st.download_button("Télécharger le signal reconstruit", df_out.to_csv().encode(), "reconstruction.csv")
