## integrate variation of this automation into sound conversion...

import wave
import contextlib
import os


for file_name in os.listdir(os.getcwd()):
    if file_name.endswith(".wav") or file_name.endswith(".aiff"):
        with contextlib.closing(wave.open(file_name, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            duration = int(duration)
            duration = str(duration)
            new_file_name = duration + " " + file_name
            print(file_name)
            os.rename(file_name, new_file_name)
    else:
        continue
