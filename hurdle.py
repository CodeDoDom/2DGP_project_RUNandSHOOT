from pico2d import *


class Hurdle:
    # image = None
    def __init__(self):
        self.image = load_image('drum.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(120, 160) # 이 좌표로 하면 캐릭터 점프 위치랑 완벽하게 맞음
        