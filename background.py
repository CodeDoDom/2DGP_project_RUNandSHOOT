from pico2d import *

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 30.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class Background:
    def __init__(self):
        self.x1, self.y1 = 640, 360

        self.x2, self.y2 = 0, 360
        self.x2_copy, self.y2_copy = 1280, 360

        self.x3, self.y3 = 0, 360
        self.x3_copy, self.y3_copy = 1280, 360

        self.x4, self.y4 = 0, 360
        self.x4_copy, self.y4_copy = 1280, 360

        self.x5, self.y5 = 0, 360
        self.x5_copy, self.y5_copy = 1280, 360

        #self.w, self.h = 576, 324

        self.image1 = load_image('sky_1.png')

        self.image2 = load_image('sky_2.png')
        self.image2_copy = load_image('sky_2.png')

        self.image3 = load_image('sky_3.png')
        self.image3_copy = load_image('sky_3.png')

        self.image4 = load_image('sky_4.png')
        self.image4_copy = load_image('sky_4.png')

        self.image5 = load_image('sky_5.png')
        self.image5_copy = load_image('sky_5.png')

    def update(self):
        # self.x2 -= 1
        # self.x3 -= 1
        # self.x4 -= 3
        # self.x5 -= 2
        #
        # self.x2_copy -= 1
        # self.x3_copy -= 1
        # self.x4_copy -= 3
        # self.x5_copy -= 2

        self.x2 -= MOVE_SPEED_PPS*game_framework.frame_time * 1
        self.x3 -= MOVE_SPEED_PPS*game_framework.frame_time * 1
        self.x4 -= MOVE_SPEED_PPS*game_framework.frame_time * 1.5
        self.x5 -= MOVE_SPEED_PPS*game_framework.frame_time * 2

        self.x2_copy -= MOVE_SPEED_PPS*game_framework.frame_time * 1
        self.x3_copy -= MOVE_SPEED_PPS*game_framework.frame_time * 1
        self.x4_copy -= MOVE_SPEED_PPS*game_framework.frame_time * 1.5
        self.x5_copy -= MOVE_SPEED_PPS*game_framework.frame_time * 2

    def draw(self):
        self.image1.draw(self.x1, self.y1)

#        if self.x2 == -640:
#            self.x2 = 1280 + 640
#        self.image2.draw(self.x2, self.y2)
#        if self.x2_copy == -640:
#            self.x2_copy = 1280 + 640
#        self.image2_copy.draw(self.x2_copy, self.y2_copy)

        if self.x3 <= -640:
            self.x3 = 1280 + 640
        self.image3.draw(self.x3, self.y3)
        if self.x3_copy <= -640:
            self.x3_copy = 1280 + 640
        self.image3_copy.draw(self.x3_copy, self.y3_copy)

        if self.x4 <= -640:
            self.x4 = 1280 + 640
        self.image4.draw(self.x4, self.y4)
        if self.x4_copy <= -640:
            self.x4_copy = 1280 + 640
        self.image4_copy.draw(self.x4_copy, self.y4_copy)

        if self.x5 <= -640:
            self.x5 = 1280 + 640
        self.image5.draw(self.x5, self.y5)
        if self.x5_copy <= -640:
            self.x5_copy = 1280 + 640
        self.image5_copy.draw(self.x5_copy, self.y5_copy)
