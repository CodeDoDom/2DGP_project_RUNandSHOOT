from pico2d import *

import game_framework
import logo_mode


class Timer:
    def __init__(self):
        self.x, self.y = 620, 680
        self.sec = 90
        self.wait_time = get_time()
        self.font = load_font('neodgm.TTF', 30)

    def update(self):
        if get_time() - self.wait_time > 1.0:
            self.sec -= 1
            self.wait_time = get_time()
        if (self.sec // 60) < 0.0:
            game_framework.change_mode(logo_mode)


    def draw(self):
        self.font.draw(self.x, self.y, f'{int(self.sec // 60)}:{self.sec % 60}', (255, 255, 255))
