import numpy as np
import sounddevice as sd
import time

sample_rate = 44100
def sine_wave(frequency, duration, volume):

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    sinewave_data = np.sin(frequency * x)

    sinewave_data = sinewave_data * volume

    return sinewave_data



