from pico2d import *


class Hurdle:
    # image = None
    def __init__(self):
        self.x, self.y = 720, 160 # 이 y 좌표로 하면 캐릭터 점프 위치랑  완벽하게 맞음
        self.w, self.h = 128, 128
        self.image = load_image('drum.png')
        # self.x, self.y = 120, 110
        # self.image = load_image('drum_new.png')

    def update(self):
        self.x -= 1
        # drum을 움직일 때, 3초 후에 runner이랑 동시에 움직여야 함.
        # drum의 statemachine을 만들어야 할까?

    def draw(self):
        self.image.clip_draw(0, 0, self.w, self.h, self.x, self.y)
        # self.image.clip_draw(0, 0, 35, 30, self.x, self.y)
