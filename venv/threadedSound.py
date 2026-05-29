from p5 import *
from playsound3 import playsound  # The updated, Apple Silicon-compatible version
import threading

def setup():
    size(400, 400)
    # No audio loading required in setup, playsound handles it on the fly

def draw():
    background(240)
    fill(0)
    text("Click anywhere to play audio without freezing!", 50, 200)

def play_audio_worker():
    # This runs entirely on a side thread
    # block=True forces the THREAD to wait for the sound to finish, 
    # but it won't freeze your p5 window!
    playsound("sample.wav", block=True)

def mouse_pressed():
    # Spin up the audio on a separate thread whenever the mouse is clicked
    audio_thread = threading.Thread(target=play_audio_worker)
    
    # ---------------------------------------------------------
    # CRITICAL LINE: This tells Python to kill this thread 
    # the moment the main p5 window is closed.
    audio_thread.daemon = True 
    # ---------------------------------------------------------
     
    audio_thread.start()

if __name__ == '__main__':
    run()