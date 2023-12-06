from pico2d import *

import game_framework
import game_world
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 60.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class TargetX:
    def __init__(self):
        self.x, self.y = 1300, 500
        self.w, self.h = 100, 100
        self.image = load_image('target_X.png')

    def update(self):
        # self.x -= 3
        self.x -= MOVE_SPEED_PPS * game_framework.frame_time
        if self.x <= -50:
            game_world.remove_object(self)

        if self.x - 50 <= server.runner.mx <= self.x + 50 and self.y - 50 <= server.runner.my <= self.y + 50:
            server.runner.mx, server.runner.my = 0, 0
            server.score.score -= 5
            server.runner.runner_shoot_target.play()
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
