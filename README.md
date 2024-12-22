# Infinite Storage Glitch: File to MP4 Converter

Dieses Projekt wandelt Dateien in MP4-Videos um, indem die Binärdaten der Datei in Bilder konvertiert und anschließend als Video gespeichert werden. Dies kann verwendet werden, um Daten auf Plattformen wie YouTube zu speichern.

---

## Voraussetzungen

Bevor du das Skript ausführst, stelle sicher, dass die folgenden Programme und Bibliotheken installiert sind:

1. **Python 3.7+**
2. **FFmpeg** (zur Konvertierung von Bildern in Videos)
3. Die Python-Bibliotheken:
   - `Pillow`
   - `glob`
   - `subprocess` (Teil der Python-Standardbibliothek)

---

## Installation

Überprüfe, ob Python installiert ist:

`python --version`

2. Installiere FFmpeg

MacOS
Ubuntu/Debian
Windows
	1.	Lade FFmpeg von der offiziellen FFmpeg-Website herunter.
	2.	Kopiere FFmpeg in den Ordner "mp4_end_dec"

3. Installiere Python - Bibliotheken:

    `pip install pillow` (wenn pip nicht funktioniert benutze pip3)

Verwendung:

Führe das script aus `python3 converter.py`

