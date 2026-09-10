# Laboratoire de Modulation

Rapports realises dans le cadre du cours de Laboratoire de Modulation, ISIB (HE2B), sous la supervision de Ing. M. Garcia Acevedo.

Auteurs : Yassine AMINE EL JAZAR, Daoud M'RABET, Alexis ARELLANO CHALUISA

## Objectif du cours

Ce laboratoire vise a faire le lien entre la theorie du traitement du signal et sa mise en oeuvre pratique, en etudiant experimentalement les principales briques d'une chaine de transmission numerique : echantillonnage, modulation, multiplexage temporel et controle d'erreurs. Les manipulations s'appuient sur les bancs didactiques Modicom 1, 2 et 3, completees par un projet final base sur une technologie de communication sans fil reelle.


## Contenu des manipulations

### Manipulation 1 - Echantillonnage et reconstruction du signal

Etude du theoreme de Shannon-Nyquist, du phenomene d'aliasing et de la reconstruction d'un signal par filtre passe-bas, a l'aide du banc Modicom 1.

Points cles :
- Modelisation mathematique de l'echantillonnage (peigne de Dirac) et demonstration du noyau de reconstruction en sinus cardinal
- Observation du signal echantillonne avant et apres le bloqueur d'ordre zero
- Comparaison des filtres passe-bas du second et du quatrieme ordre pour la reconstruction
- Mise en evidence experimentale de l'aliasing par variation de la frequence d'echantillonnage (32 kHz a 2 kHz)
- Influence du duty cycle sur l'amplitude du signal echantillonne, avec analyse de la charge du condensateur de maintien
- Travail complementaire : simulation du circuit Sample and Hold sous Falstad (MOSFET, condensateur de maintien, amplificateur suiveur)

### Manipulation 2 - PAM et TDM

Etude de la modulation par amplitude d'impulsions (PAM) et du multiplexage temporel (TDM) a l'aide du banc Modicom 2.

Points cles :
- Generation de signaux analogiques, echantillonnage par PAM et multiplexage de deux voies sur un seul canal
- Reconstruction de chaque voie par filtrage passe-bas apres demultiplexage
- Etude de l'influence du rapport cyclique (duty cycle) sur la largeur des echantillons et la puissance du signal
- Diagnostic d'un defaut de reconstruction (bruit sur le signal reconstruit), remonte jusqu'au filtre actif de la carte et a un condensateur suspecte

### Manipulation 3 - PCM et TDM (Modicom 3)

Etude d'une chaine de transmission numerique complete basee sur la modulation par impulsions codees (PCM) combinee au TDM, a l'aide du banc Modicom 3.

Points cles :
- Structure de trame a 15 timeslots (synchronisation, voie 0, voie 1) et lecture spectrale par FFT
- Validation de la chaine complete emetteur/recepteur en Connection Mode 1 (horloge, synchro et donnees separees)
- Connection Mode 2 : synchronisation par sequence pseudo-aleatoire (reduction du cablage a deux liaisons)
- Connection Mode 3 : regeneration d'horloge par PLL/VCO a partir des transitions de la donnee (une seule liaison)
- Controle d'erreurs par bit de parite (odd/even) et par code de Hamming, avec activation de defauts commutes (switched faults)
- Analyse de l'impact du niveau DC d'entree sur la quantification et le motif binaire transmis

## Projet final - Reseau LoRa avec Meshtastic

Conception d'un reseau de communication local et decentralise base sur la technologie LoRa (Long Range) et le protocole de routage Meshtastic, a l'aide de modules LilyGO TTGO LoRa32 868 MHz.

Points cles :
- Principe de la modulation CSS (Chirp Spread Spectrum) utilisee par LoRa et ses trois parametres cles : Spreading Factor, bande passante et coding rate
- Architecture testee par etapes : liaison filaire de validation, puis liaison Bluetooth via smartphones, puis reseau maille (mesh) a plusieurs noeuds
- Fonctionnement du routage par sauts (hopping) permettant a chaque module de relayer les messages des autres
- Extension possible du reseau par passerelles MQTT reliant plusieurs "bulles" de reseau maille
- Discussion des cas d'usage (randonnee, evenements, reseaux de secours) et des limites du systeme (debit, nombre de sauts)

## Outils utilises

- Bancs pedagogiques Modicoms
- Oscilloscope Keysight (mesures temporelles et FFT)
- Modules LilyGO TTGO LoRa32 868 MHz (ESP32) et firmware Meshtastic
- Simulateur de circuits Falstad (travail complementaire sur le Sample and Hold)
- LaTeX pour la redaction des rapports
