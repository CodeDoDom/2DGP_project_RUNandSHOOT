from pico2d import *

class Runner:
    def __init__(self):
        self.image = load_image('running.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
