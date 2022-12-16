import sounddevice

from scipy.io.wavfile import write

def grabador(seconds,file):
    print("Iniciando grabacion")
    
    recording=sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()

    write(file, 44100, recording)
    print("Grabacion finalizada")

grabador(10, "record.wav")