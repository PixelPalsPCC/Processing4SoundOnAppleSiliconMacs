add_library("sound")

def setup():
    size(200, 200)
    
    # Initialize the sound library
    global file
    file = SoundFile(this, "sample.wav")
    file.play()

def draw():
    background(51)
