import game_framework
from pico2d import *

import play_mode


def init():
    global image_char
    global image_drum
    global frame

    frame = 0
    image_char = load_image('Shot.png')
    image_drum = load_image('drum.png')


def finish():
    global image_char, image_drum
    del image_char, image_drum


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)


def update():
    global frame

    frame = (frame + 1) % 12


def draw():
    clear_canvas()
    image_char.clip_draw(frame * 128, 0, 100, 100, 600, 300, 128 * 2, 128 * 2)
    image_drum.draw(400, 500)
    update_canvas()
