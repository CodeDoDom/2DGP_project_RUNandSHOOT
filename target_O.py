import random

from pico2d import *


class TargetO:
    def __init__(self):
        self.x, self.y = 600, 500
        self.w, self.h = 100, 100
        self.image = load_image('target_O.png')

    def update(self):
        self.x -= 3
        # self.y -= random.randint(-50, 50)

    def draw(self):
        self.image.draw(self.x, self.y)
