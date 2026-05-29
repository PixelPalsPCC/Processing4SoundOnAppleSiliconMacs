from p5 import *

def setup():
    # Creates a window workspace
    size(400, 400)

def draw():
    # Clears screen to white and draws a black circle
    background(255)
    fill(0)
    circle(200, 200, 100)

if __name__ == '__main__':
    run()
