from pico2d import *


class TargetX:
    def __init__(self):
        self.x, self.y = 300, 500
        self.w, self.h = 100, 100
        self.image = load_image('target_X.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
