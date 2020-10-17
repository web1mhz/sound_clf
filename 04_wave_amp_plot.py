from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from os import walk
import os

soundType = "bird8"

if not os.path.exists(soundType + "plots"):
    os.makedirs(soundType + "plots")
sound_wavs = []
for (_,_,filenames) in walk(soundType):
    sound_wavs.extend(filenames)
    break
for wav in sound_wavs:
    # read audio samples
    input_data = read(soundType + "/" + wav)
    audio = input_data[1]
    # plot the first 1024 samples
    plt.plot(audio)
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    # set the title
    # plt.title("Sample Wav")
    # display the plot
    plt.savefig(soundType + "Plots/" + wav.split('.')[0] + '.png')
    # plt.show()
    plt.close('all')