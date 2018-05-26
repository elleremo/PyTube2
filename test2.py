import os

unrec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Unrecorded"
rec_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Recorded"
midi_dir = "D:/Projects SSD/YouTube 2018/PyTube2/Midi"
gtpmid_dir = "D:/Projects SSD/YouTube 2018/PyTube2/GTP_MIDI"

f = "D://Projects SSD\YouTube 2018\PyTube2/Unrecorded\Black Veil Brides\Black Veil Brides - Carolyn  .mid"

x = os.path.dirname(f)
y = os.path.basename(f)
print(x)
print(y)