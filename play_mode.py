from pico2d import *
import game_framework

import game_world
from background import Background
from hurdle import Hurdle
from runner import Runner


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            runner.handle_event(event)


def init():
    global runner
    global background
    global drum

    running = True

    # background = Background()
    # game_world.add_object(background, 0)

    drum = Hurdle()
    game_world.add_object(drum, 1)


    runner = Runner()
    game_world.add_object(runner, 2)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

