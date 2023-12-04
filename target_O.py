from pico2d import *

import game_world


class TargetO:
    def __init__(self):
        self.x, self.y = 1000, 500
        self.w, self.h = 100, 100
        self.image = load_image('target_O.png')

    def update(self):
        self.x -= 3
        if self.x <= 100:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
