from moviepy import VideoFileClip
import os
import sys

def convert_mov_to_mp4(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    if not input_path.lower().endswith('.mov'):
        raise ValueError("Файл должен быть формата .mov")

    output_path = os.path.splitext(input_path)[0] + ".mp4"

    try:
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        print(f"[✓] Файл сконвертирован: {output_path}")
    except Exception as e:
        print(f"[!] Ошибка при конвертации: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python parse.py путь_к_файлу.mov")
        sys.exit(1)

    path = sys.argv[1]
    convert_mov_to_mp4(path)
