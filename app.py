import streamlit as st

st.set_page_config(
    page_title="Échantillonnage & Reconstruction",
    page_icon="📡",
    layout="wide"
)

st.title("Simulation pour le laboratoire de modulation (Séance 1): Échantillonnage & Reconstruction d’un signal")

st.markdown("""
  
###  Présentation de l’application

Dans le cadre du **laboratoire de modulation** du professeur **Garcia**, j’ai développé cette application
interractive en **Python** afin d’illustrer de manière intuitive et visuelle deux notions fondamentales du traitement du signal :

- **l’échantillonnage d’un signal**,  
- **et sa reconstruction** à partir des échantillons.

L’application a été conçue grâce aux modules suivants :

- **Streamlit** : pour la création de l’interface interactive  
- **NumPy** : pour le traitement numérique des signaux  
- **Matplotlib** : pour la visualisation graphique  
- **SciPy** : pour les outils d’analyse du signal (FFT, spectrogrammes, etc.)  
- **Pandas** : pour l’exportation des données  

Ces outils permettent de manipuler en temps réel les paramètres essentiels (fréquence du signal, fréquence d’échantillonnage, bruit, type de reconstruction…), de visualiser les effets de l’**aliasing**, et d’observer différentes méthodes de **reconstruction** telles que la sinc, le ZOH, l’interpolation linéaire ou encore un filtre RC.

---

###  Rapport de laboratoire

Mon **rapport complet** peut être téléchargé directement en cliquant sur le bouton ci-dessous.  
Il contient une analyse détaillée des phénomènes observés grâce à cette application.

---

### Navigation dans l’application

Un **menu latéral** vous permet de choisir la partie que vous souhaitez explorer :

- **Échantillonnage** : visualisation du signal continu, des échantillons, de la FFT et du spectrogramme.  
- **Reconstruction** : comparaison des méthodes de reconstruction et analyse fréquentielle du signal reconstruit.

Cette application a pour objectif d’offrir un support clair, interactif et pédagogique pour mieux comprendre
la chaîne complète *signal continu → échantillonnage → reconstruction*.

""")
with open("labo_mod1.pdf", "rb") as pdf_file:
    st.download_button(
        label="Télécharger le rapport de labo (PDF)",
        data=pdf_file,
        file_name="labo_mod1.pdf",
        mime="application/pdf"
    )