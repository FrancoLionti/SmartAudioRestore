import soundfile as sf
import librosa
import numpy as np

class AudioProcessor:
    def __init__(self,AudioPath=None):  
        """ AudioProcessor 0.1.0

        Inicializa la clase con opciones configurables
        
        Args:
            AudioIn: Ubicación del Audio de entrada 

        """

        self.AudioIn =sf.read(AudioPath)
        self.SR = 44100
        print("AudioProcessor initialized with sample rate:", self.SR)

