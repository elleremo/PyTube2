import os

unrec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Midi"
gtpmid_dir = "D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI"

x = unrec_dir
print (x)

a = os.path.dirname(x)
b = os.path.basename(x)
c = os.path.abspath(x)
d = os.path.normpath(x)
e = os.path.realpath(x)


def prt():
    print('путь родительской папки : ', a)
    print('имя файла/папки : ', b)
    print('абсолютный путь  : ', c)
    print('нормализайия  : ', d)
    print('какннический путь  : ', e)

prt()

# ===========================================================

class Basefile:

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.path = path
        self.parfolder = os.path.dirname(path)


class Midfile(Basefile):
    def __init__(self, path):
        super().__init__(path)

        self.artist = os.path.basename(os.path.dirname(path))
        #self.duration = MidiFile(path).length



