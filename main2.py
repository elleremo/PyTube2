import pydir
import os

from pprint import pprint
import time

from mdfile import MidiFile as MD

# os.listdir(path=".") - список файлов и директорий в папке.
# os.chdir(path) - смена текущей директории.

# os.path.basename(path) - имя файла/папки по указанному пути
# os.path.dirname(path) - путь до родительской папки
# os.path.basename(os.path.dirname(path)) - имя родительской папки


main_dir = os.getcwd()  # текущая дериктория
# print("Текущая дериктория =", main_dir)

unrec_dir = 'D:\Projects SSD/YouTube 2018/PyTube2/Unrecorded'
rec_dir = 'D:/Projects SSD/YouTube 2018/PyTube2/Recorded'
midi_dir = 'D:/Projects SSD/YouTube 2018/PyTube2/Midi'
gtp_midi = 'D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI'


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
        self.fullname = os.path.basename(path)
        self.name = os.path.splitext(self.fullname)[0]
        self.ext = os.path.splitext(self.fullname)[1]
        self.path = path
        self.parfolder = os.path.dirname(path)

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return 'Basefile ("' + self.fullname + '")'


class Midifile(Basefile):
    def __init__(self, path):
        super().__init__(path)
        self.artist = os.path.basename(os.path.dirname(path))

    def get_duration(self):
        self.length = MD(self.path).length

    def __repr__(self):
        return 'Midifile ("' + self.fullname + '")'


# ======================================================

def getListFolders(folder):
    """Создать список обектов Folder в указаннной папке"""

    tempsubdirs = pydir.get_subdirs(folder)
    subdirs = [Folder(dir) for dir in tempsubdirs]

    return subdirs


# ------------------------------------------------------

def getListFiles(folder, ext=None):
    """Создать список обектов File в указаннной папке"""

    files = []
    tempfiles = pydir.get_files(folder, ext)

    if ext is None:
        for file in tempfiles:
            temp = Basefile(file)
            files.append(temp)
        return files
    elif ext == "mid":
        for file in tempfiles:
            temp = Midifile(file)
            files.append(temp)
        return files


# ------------------------------------------------------
x = Folder('D:\Projects SSD\YouTube 2018\PyTube2\GTP_MIDI\Black Veil Brides -Gtp')
x.getfiles()
print (x.files)
