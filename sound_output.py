import wave
image_file = '/Users/applestore/Desktop/Google_Scrape/bart_face.gif'
fin = open(image_file, 'rb')
data = fin.read()
fin.close()
sound_output = wave.open('image.wav', 'w')
params = (2,2,44100, 10, 'NONE', 'not compressed')
sound_output.setparams(params)
hex_str = bytes(data)
sound_output.writeframes(hex_str)
sound_output.close()




