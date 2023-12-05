from pico2d import *


class Score:
    def __init__(self):
        self.w, self.h = 1280, 760
        self.font = load_font('neodgm.TTF', 30)

    def update(self):
        pass

    def draw(self):
        self.font.draw(1020, 700, f'Score: {self.w}', (255, 255, 255))
