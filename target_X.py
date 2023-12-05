from pico2d import *

import game_world
import server


class TargetX:
    def __init__(self):
        self.x, self.y = 1000, 500
        self.w, self.h = 100, 100
        self.image = load_image('target_X.png')

    def update(self):
        self.x -= 3
        if self.x <= 100:
            game_world.remove_object(self)

        if self.x - 50 <= server.runner.mx <= self.x + 50 and self.y - 50 <= server.runner.my <= self.y + 50:
            game_world.remove_object(self)
            server.runner.mx, server.runner.my = 0, 0
            server.score.score -= 5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
