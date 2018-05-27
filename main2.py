import pydir
import os
from mdfile import MidiFile

# os.listdir(path=".") - список файлов и директорий в папке.
# os.chdir(path) - смена текущей директории.

# os.path.basename(path) - имя файла/папки по указанному пути
# os.path.dirname(path) - путь до родительской папки
# os.path.basename(os.path.dirname(path)) - имя родительской папки


main_dir = os.getcwd()  # текущая дериктория
# print("Текущая дериктория =", main_dir)

unrec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Midi"
gtp_midi = "D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI"


class Folder:
    """ Класс Папки """

    def __init__(self, path):
        """ Метод принимает путь"""
        self.name = os.path.basename(path)
        self.parfolder = os.path.dirname(path)
        self.path = path
        self.files = []

    def getfiles(self, ext=None):
        """ Получить файлы. Указать расширение, если нужен конкретный тип файлов """
        self.files = getListFiles(self.path, ext)

class Basefile:

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.path = path
        self.parfolder = os.path.dirname(path)
        self.artist = os.path.basename(os.path.dirname(path))

class Midfile:

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.parfolder = os.path.dirname(path)
        self.path = path
        self.artist = os.path.basename(os.path.dirname(path))
        #self.duration = MidiFile(path).length


# ======================================================

def getListFolders(folder):
    """Создать список обектов Folder в указаннной папке"""
    subdirs = []
    if not pydir.is_empty_dir(folder):
        tempsubdirs = pydir.get_subdirs(folder)
        subdirs = [Folder(dir) for dir in tempsubdirs]

    return subdirs


# ------------------------------------------------------

def getListFiles(folder, ext=None):
    """Создать список обектов File в указаннной папке"""
    files = []

    if not pydir.is_empty_dir(folder):
        tempfiles = pydir.get_files(folder, ext)

        if ext is None:
            return tempfiles
        else:
            for file in tempfiles:
                temp = MidFile(file)
                files.append(temp)
            return files



# ------------------------------------------------------

def pr(arr, z):
    for f in arr:
        print(getattr(f, z))


x = getListFolders(gtp_midi)  # получили список подпапок
pr(x, "name")

num = 0

for sub in x:
    sub.getfiles("mid") # вызвали функцию получить файлы

    for mfile in sub.files:
        #print(mfile.name)
        num += 1

print (num)