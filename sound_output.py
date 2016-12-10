>>> import wave
>>> image_file = '/Users/applestore/Desktop/Google_Scrape/bart_face.gif'
>>> fin = open(image_file, 'rb')
>>> data = fin.read()
>>> fin.close()
>>> sound_output = wave.open('image.wav', 'w')
>>> params = (2,2,44100, 10, 'NONE', 'not compressed')
>>> sound_output.setparams(params)
>>> hex_str = bytes(data)
>>> sound_output.writeframes(hex_str)
>>> sound_output.close()
>>> 


## integrate this automation into it...

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
