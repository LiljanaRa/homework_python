import os
import sys


def file_dir_list(path):
    for root, dirs, files in os.walk(path):
        print(f"Текущая директория: {root}")
        for dir in dirs:
            print(f"Поддиректория: {os.path.join(root, dir)}")
            for file in files:
                print(f"Файл: {os.path.join(root, dir, file)}")


file_dir_list(sys.argv[1])