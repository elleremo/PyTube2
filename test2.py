import os
import shutil


unrec_dir = r"D:/Projects SSD//YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2\Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/\PyTube2/Midi"
gtpmid_dir = "D:/Projects SSD/YouTube 2018/PyTube2\GTP_MIDI"

x = unrec_dir

a = os.path.dirname(x)
b = os.path.basename(x)
c = os.path.abspath(x)
d = os.path.normpath(x)
e = os.path.realpath(x)


def prt():
    print('dirname - путь родительской папки : ', a)
    print('basename - имя файла/папки : ', b)
    print('abspath - абсолютный путь  : ', c)
    print('normpath - нормализайия  : ', d)
    print('realpath - канонический путь  : ', e)

#print(x, "\n")
#prt()

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

# ===========================================================

def copy_file(file, dst):

    e = shutil.copy2(file, dst)
    print (e)

copy_file(r'D:\Projects SSD\YouTube 2018\PyTube2\Midi\rgaergvb2.txt', 'Recorded' )