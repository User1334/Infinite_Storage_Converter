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

### **1. Installiere Python**

Überprüfe, ob Python installiert ist:

```bash
python --version

2. Installiere FFmpeg

MacOS

brew install ffmpeg

Ubuntu/Debian

sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg

Windows
	1.	Lade FFmpeg von der offiziellen FFmpeg-Website herunter.
	2.	Entpacke die ZIP-Datei und kopiere den Inhalt in ein Verzeichnis (z. B. C:\ffmpeg).
	3.	Füge den bin-Ordner zum PATH hinzu:
	•	Öffne die Umgebungsvariablen (Systemsteuerung > System > Erweiterte Systemeinstellungen > Umgebungsvariablen).
	•	Bearbeite die Variable PATH und füge den Pfad zu deinem ffmpeg/bin-Ordner hinzu (z. B. C:\ffmpeg\bin).

    Überprüfe, ob ffmpeg korrekt installiert ist:

    bash
    ffmpeg --version

    3. Installiere Python - Bibliotheken:

    pip install pillow (wenn pip nicht funktioniert benutze pip3)

    Falls pip nicht verfügbar ist, installiere es mit:
    python -m ensurepip --upgrade

    Verwendung

1. Dateipfad anpassen

Öffne die Datei filetomp4.py und passe den Pfad der Datei an, die umgewandelt werden soll:

file_path = "test/Archiv.zip"
Ersetze test/Archiv.zip durch den Pfad deiner Datei.

2. Skript ausführen

Führe das Skript aus: 
python3 filetomp4.py 

Das Skript generiert:
	•	Ein MP4-Video mit dem Namen <Dateiname>.<Dateityp>.<Länge>.mp4.

3. Beispiel

Wenn die Eingabedatei Archiv.zip heißt, könnte das Skript ein Video wie Archiv.zip.12345678.mp4 erstellen.

Funktionsweise
	1.	Datei zu Binärstring: Die Datei wird in Binärdaten umgewandelt.
	2.	Binärdaten zu Bildern: Die Binärdaten werden in eine Serie von Bildern übersetzt.
	3.	Bilder zu Video: Die Bilder werden mithilfe von FFmpeg zu einem MP4-Video zusammengefügt.
	4.	Aufräumen: Nach der Erstellung des Videos werden die generierten Bilder gelöscht.

    Befehle zur Installation und Ausführung

Für eine schnelle Einrichtung kannst du die folgenden Befehle verwenden:

Linux/MacOS
# FFmpeg installieren
sudo apt update && sudo apt install ffmpeg -y

# Pillow installieren
pip install pillow

# Skript ausführen
python filetomp4.py

Windows
	1.	Installiere Python von der Python-Website.
	2.	Lade FFmpeg von ffmpeg.org herunter, entpacke es, und füge den bin-Ordner zum PATH hinzu.
	3.	Installiere Pillow:

    pip install pillow

	4.	Führe das Skript aus:

    python filetomp4.py

    Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die Datei LICENSE für Details.

