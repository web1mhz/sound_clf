from pydub import AudioSegment

soundType = 'bird8'

sound = AudioSegment.from_mp3(soundType + ".mp3")
sound.export(sound + ".wav", format="wav")
