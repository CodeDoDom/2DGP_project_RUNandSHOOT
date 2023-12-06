import game_framework
from pico2d import *

import play_mode
import server
import title_mode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 30.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


def init():
    global image_char
    global image_drum
    global image_sky1, image_sky4, image_sky5
    global frame
    global font, font_1, f_x, f_y
    global end_start_time

    frame = 0
    image_char = load_image('Shot.png')
    image_drum = load_image('drum.png')
    image_sky1 = load_image('sky_1.png')
    image_sky4 = load_image('sky_4.png')
    image_sky5 = load_image('sky_5.png')
    font = load_font('neodgm.TTF', 100)
    font_1 = load_font('neodgm.TTF', 50)
    f_x, f_y = 600, 650
    end_start_time = get_time()

def finish():
    global image_char, image_drum, image_sky1, image_sky4, image_sky5, font, font_1
    del image_char, image_drum, image_sky1, image_sky4, image_sky5, font, font_1


def handle_events():
    events = get_events()


def update():
    global end_start_time
    global frame

    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

    if get_time() - end_start_time >= 5.0:
        end_start_time = get_time()
        game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image_sky1.draw(640, 360)
    image_sky4.draw(640, 360)
    image_sky5.draw(640, 360)
    image_drum.clip_draw(0, 0, 128, 128, 200, 470, 128 * 6, 128 * 6)
    image_char.clip_draw(int(frame) * 128, 0, 100, 100, 350, 270, 128 * 3, 128 * 3)
    font.draw(f_x, f_y - 70, f'Score: {server.score.score}', (0, 0, 0))
    font_1.draw(f_x + 90, f_y - 170, f'Waiting For Restart', (255, 255, 255))
    update_canvas()
