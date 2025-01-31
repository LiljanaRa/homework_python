import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('file_path')
args = parser.parse_args()

def starts_file():
    path_file = args.file_path
    if not os.path.exists(path_file):
        print("Файл не найден.")
        return
    try:
        os.system(f"Python {path_file}")
        print(f"Файл {path_file} успешно запущен.")
    except Exception as e:
        print(e)

starts_file()
