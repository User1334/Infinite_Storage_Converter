from PIL import Image
import os
import subprocess


def file_to_binary_string(file_path):
    """Konvertiert eine Datei in einen Binärstring."""
    with open(file_path, 'rb') as file:
        binary_code = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_code)
    return binary_string


def binary_string_to_file(binary_string, file_path):
    """Konvertiert einen Binärstring in eine Datei."""
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)


def binary_to_image(binary_str):
    """Konvertiert einen Binärstring in eine Serie von Bildern."""
    img_width = 480
    img_height = 360
    index = 0
    count = 0

    # Sicherstellen, dass das Verzeichnis für Bilder existiert
    output_dir = "./images"
    os.makedirs(output_dir, exist_ok=True)

    while index < len(binary_str):
        image = Image.new("1", (img_width, img_height), color=1)
        for y in range(6, img_height, 6):
            for x in range(0, img_width, 6):
                if index < len(binary_str):
                    if binary_str[index] == "1":
                        for i in range(3):
                            for j in range(3):
                                image.putpixel((x + j, y + i), 0)
                    else:
                        for i in range(3):
                            for j in range(3):
                                image.putpixel((x + j, y + i), 1)
                index += 1

        image.save(f"{output_dir}/binary_image_{count}.png")
        count += 1


def image_to_binary(image_path):
    """Konvertiert ein Bild in einen Binärstring basierend auf den Pixelwerten."""
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_str = ""
    for y in range(6, height, 6):
        for x in range(0, width, 6):
            r, g, b = pixels[x, y]
            if r < 200 and g < 200 and b < 200:
                binary_str += "1"
            elif r > 200 and g > 200 and b > 200:
                binary_str += "0"
    return binary_str


def images_to_video(video_filename):
    """Konvertiert Bilder in ein MP4-Video."""
    input_path = "./images/*.png"
    output_path = video_filename
    fps = 1
    video_codec = "libx264"
    command = [
        "ffmpeg", "-y", "-framerate", str(fps),
        "-i", "./images/binary_image_%d.png",
        "-codec:v", video_codec, output_path
    ]
    subprocess.call(command)


def capture_frame(filePath):
    """Extrahiert Frames aus einem Video und speichert sie als Bilder."""
    output_frames = "data/binary_image_%d.png"
    command = ["ffmpeg", "-i", filePath, "-vf", "fps=1", output_frames]
    subprocess.call(command)


def remove_img(path):
    """Löscht eine Bilddatei."""
    try:
        os.remove(path)
    except FileNotFoundError:
        print(f"Datei nicht gefunden: {path}")


def convert_file_to_video():
    """Hauptfunktion zur Konvertierung einer Datei in ein Video."""
    file_path = input("Gib den Pfad zur Datei ein, die in ein Video konvertiert werden soll: ").strip()
    if not os.path.exists(file_path):
        print(f"Die Datei '{file_path}' existiert nicht.")
        return

    binary_string = file_to_binary_string(file_path)
    binary_to_image(binary_string)
    video_name = file_path + ".mp4"
    images_to_video(video_name)
    print(f"Das Video wurde gespeichert unter: {video_name}")


def convert_video_to_file():
    """Hauptfunktion zur Rekonstruktion einer Datei aus einem Video."""
    file_path = input("Gib den Pfad zum MP4-Video ein: ").strip()
    if not os.path.exists(file_path):
        print(f"Die Datei '{file_path}' existiert nicht.")
        return

    capture_frame(file_path)
    onlyfiles = next(os.walk("data"))[2]
    binary_string = ""

    for i in range(len(onlyfiles)):
        image_path = f"data/binary_image_{i + 1}.png"
        binary_string += image_to_binary(image_path)
        remove_img(image_path)

    output_file = file_path.replace(".mp4", "")
    binary_string_to_file(binary_string, output_file)
    print(f"Die rekonstruierte Datei wurde gespeichert unter: {output_file}")


def main():
    """Hauptprogramm, das den Benutzer die gewünschte Aktion wählen lässt."""
    print("Wähle eine Aktion:")
    print("1. Datei in MP4-Video konvertieren")
    print("2. MP4-Video in Datei rekonstruieren")
    choice = input("Gib 1 oder 2 ein: ").strip()

    if choice == "1":
        convert_file_to_video()
    elif choice == "2":
        convert_video_to_file()
    else:
        print("Ungültige Auswahl. Programm wird beendet.")


if __name__ == "__main__":
    main()