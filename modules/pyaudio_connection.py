import pyaudio
import numpy as np
from scipy.fftpack import fft
from modules import features

#####################################################################################
#                            PYAUDIO                                                #
#####################################################################################

# constants
CHUNK = 512 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

class pyaudio_connection():

    def __init__(self):
        # pyaudio class instance
        p = pyaudio.PyAudio()

        count = p.get_device_count()

        input_device_index = 0
        for i in range(count):
            name = p.get_device_info_by_index(i)['name']
            if 'Missaggio' in name or 'missaggio' in name or 'mix' in name:
                input_device_index = i
                break

        # stream object to get data from microphone
        global stream
        try:
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                input_device_index=input_device_index
            )
        except:
            input_device_index = 0
            while True:
                try:
                    stream = p.open(
                        format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=input_device_index
                    )
                    break
                except:
                    if input_device_index < count:
                        input_device_index = input_device_index + 1
                    else:
                        break

    def pyaudio_target(self, python_osc_object, quit_object):
        max_freq = RATE//2
        xf = np.linspace(0, max_freq, CHUNK//2)     # frequencies (spectrum)
        features_object = features.features()

        while True:
            if quit_object.get_quit():
                break

            # binary data
            data = stream.read(CHUNK)    
            data_np = np.frombuffer(data, dtype='h')/2**15
                
            # compute FFT and update line
            yf = fft(data_np, len(xf))

            # yf = yf[1:len(yf)]
            # xf = xf[1:len(xf)]

            feat = features_object.compute_features(xf[1:-1], yf[1:-1], len(xf)-2)
            python_osc_object.send_features(feat)
