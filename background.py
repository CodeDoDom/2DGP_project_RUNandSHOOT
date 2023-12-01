from pico2d import *


class Background:
    def __init__(self):
        self.x, self.y = 290, 360
        self.w, self.h = 294, 412
        self.image = load_image('background_01.png')

    def update(self):
        pass

    def draw(self):
        # self.image.draw(600, 300)
        self.image.clip_draw(0, 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
