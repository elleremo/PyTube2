import os
import shutil

# os.listdir(path=".") - список файлов и директорий в папке.
# os.chdir(path) - смена текущей директории.

main_dir = os.getcwd()  # текущая дериктория
# print("Текущая дериктория =", main_dir)

unrec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Midi"
gtpmid_dir = "D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI"


# Проверка папки на пустоту
def is_empty_dir(path):
    if len(os.listdir(path)) == 0:
        print(path, ": пусто")
        return True
    else:
        return False


# Получить список поддиректорий c полным путем
def get_subdirs(path):

    if is_empty_dir(path):
        print("Папка по пути " + path + ' ПУСТА' )
    else:
        subdirs = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        return subdirs


def get_files(path, ext=None):
    """Получить список файлов без расширение или с ним"""

    if is_empty_dir(path):
        print("Папка по пути " + path + ' ПУСТА')
    else:
        if ext is None:
            files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            return files
        else:
            files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith("." + ext)]
            return files




# gg = get_subdirs(gtpmid_dir)
# pp = get_files(gg[0])
# print(os.path.abspath ( pp[0] ))
