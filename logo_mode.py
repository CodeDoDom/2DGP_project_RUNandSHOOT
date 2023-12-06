from pico2d import *

import game_framework
import title_mode


def init():
    global image
    global running
    global logo_start_time

    image = load_image('sky_1.png')
    running =True
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global running
    global logo_start_time

    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)
        # game_framework.quit()
        # running = False


def draw():
    clear_canvas()
    image.draw(640, 360)
    update_canvas()


def handle_events():
    events = get_events()