import os
from modules import pyaudio_connection, spotipy_connection, python_osc_connection, quit_app
from threading import Thread
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

if __name__== "__main__":
    
    pyaudio_object = pyaudio_connection.pyaudio_connection()
    spotipy_object = spotipy_connection.spotipy_connection()
    python_osc_object = python_osc_connection.python_osc_connection()
    quit_object = quit_app.quit_app(spotipy_object)

    spotipy_object.open_spotify(quit_object)

    subprocess.Popen("./the_spotiroom/the_spotiroom/the_spotiroom")
    
    spotipy_object.run()

    pyaudio_thread = Thread(target = lambda:pyaudio_object.pyaudio_target(python_osc_object, quit_object))
    spotipy_thread = Thread(target = lambda:spotipy_object.spotipy_target(python_osc_object, quit_object))

    pyaudio_thread.start()
    spotipy_thread.start()

    quit_object.window()

    pyaudio_thread.join()
    spotipy_thread.join()
