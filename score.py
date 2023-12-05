from pico2d import *


class Score:
    def __init__(self):
        self.x, self.y = 1020, 680
        self.score = 100
        self.font = load_font('neodgm.TTF', 30)

    def update(self):
        pass

    def draw(self):
        self.font.draw(self.x, self.y, f'Score: {self.score}', (255, 255, 255))
