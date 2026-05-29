from p5 import *
from playsound import playsound  # Import the independent sound module
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = os.path.join(SCRIPT_DIR, "sample.wav")

def setup():
    size(400, 400)

def draw():
    background(240)
    fill(50, 150, 250)
    circle(200, 200, 100)
    
    fill(0)
    text("Click anywhere to play audio", 110, 260)

def mouse_pressed():
    print("Playing sound...")
    # Provide the path to your file relative to your execution folder
    playsound(AUDIO_PATH)

if __name__ == '__main__':
    run()
