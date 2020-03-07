from PyQt5 import QtWidgets
import sys
import numpy as np
import sounddevice as sd
import time

import tunerUI
from audiolib import sine_wave
from tuning import standard_e, half_step_down

class TunerApp(QtWidgets.QMainWindow, tunerUI.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.keys = standard_e
        self.sample_rate = 44100
        self.sixString.clicked.connect(self.playSixth)
        self.fiveString.clicked.connect(self.playFifth)
        self.fourString.clicked.connect(self.playFourth)
        self.threeString.clicked.connect(self.playThird)
        self.twoString.clicked.connect(self.playSecond)
        self.firstString.clicked.connect(self.playFirst)

    def playSixth(self):
        tune_index = self.tuningBox.currentIndex()

        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())
        
        duration = self.sixSeconds.value()
        frequency = self.keys[0]
        volume = self.volumeSlide.value() * 0.1
        
        wave = sine_wave(frequency, duration, volume)
        
        self.play_wave(wave, duration)

    def playFifth(self):
        tune_index = self.tuningBox.currentIndex()
        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())

        duration = self.fiveSeconds.value()
        frequency = self.keys[1]
        volume = self.volumeSlide.value() * 0.1

        wave = sine_wave(frequency, duration, volume)

        self.play_wave(wave, duration)

    def playFourth(self):
        tune_index = self.tuningBox.currentIndex()
        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())

        duration = self.fourSeconds.value()
        frequency = self.keys[2]
        volume = self.volumeSlide.value() * 0.1

        wave = sine_wave(frequency, duration, volume)
        self.play_wave(wave, duration)

    def playThird(self):
        tune_index = self.tuningBox.currentIndex()
        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())

        duration = self.threeSeconds.value()
        frequency = self.keys[3]
        volume = self.volumeSlide.value() * 0.1

        wave = sine_wave(frequency, duration, volume)
        self.play_wave(wave, duration)

    def playSecond(self):
        tune_index = self.tuningBox.currentIndex()
        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())

        duration = self.twoSeconds.value()
        frequency = self.keys[4]
        volume = self.volumeSlide.value() * 0.1

        wave = sine_wave(frequency, duration, volume)
        self.play_wave(wave, duration)

    def playFirst(self):
        tune_index = self.tuningBox.currentIndex()
        if tune_index == 0:
            self.keys = list(standard_e.values())
        elif tune_index == 1:
            self.keys = list(half_step_down.values())

        duration = self.oneSeconds.value()
        frequency = self.keys[5]
        volume = self.volumeSlide.value() * 0.1

        wave = sine_wave(frequency, duration, volume)
        self.play_wave(wave, duration)

    
    def play_wave(self, wave, duration):

        sd.play(wave, self.sample_rate)
        time.sleep(duration)

        sd.stop()

def main():
    app = QtWidgets.QApplication(sys.argv)
    tuner = TunerApp()
    tuner.show()
    app.exec_()

if __name__ == "__main__":
    main()


