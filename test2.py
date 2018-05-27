import os

unrec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Midi"
gtpmid_dir = "D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI"

x = 'D:\Projects SSD\YouTube 2018\PyTube2\\Unrecorded\Black Veil Brides\Black Veil Brides - Carolyn  .mid'
# x = os.path.dirname(x)

a = os.path.dirname(x)
b = os.path.basename(x)
c = os.path.abspath(x)
d = os.path.normpath(x)
e = os.path.realpath(x)



print( 'путь родительской папки : ', a)
print( 'имя файла/папки : ', b)
print( 'абсолютный путь  : ', c)
print( 'нормализайия  : ', d)
print( 'какннический путь  : ', e)

import os

filename = 'accounts.txt'

print(os.path.join('C:\\', filename))