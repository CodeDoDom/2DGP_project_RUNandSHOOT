import random

from pico2d import *
import game_framework

import game_world
from background import Background
from drum import Drum
from runner import Runner, Idle


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

    running = True

    # background = Background()
    # game_world.add_object(background, 0)

    global wait_time

    wait_time = get_time()

    runner = Runner()
    game_world.add_object(runner, 2)



def finish():
    game_world.clear()
    pass


def update():
    global drum
    global runner
    global wait_time

    if get_time() - wait_time > (random.random() * 100) + 0.3 and runner.state_machine.cur_state != Idle:
        drum = Drum()
        game_world.add_object(drum, 1)
        wait_time = get_time()

    # if get_time() - wait_time > 1.0 and runner.state_machine.cur_state != Idle:
    # if get_time() - wait_time > random.randint(1, 150) and runner.state_machine.cur_state != Idle:
    #     drum = Drum()
    #     game_world.add_object(drum, 1)
    #     wait_time = get_time()

    # if get_time() - wait_time > 1.0 and runner.state_machine.cur_state != Idle:
    #     if random.randint(1, 10) == 1:
    #         drum = Drum()
    #         game_world.add_object(drum, 1)
    #         wait_time = get_time()


    # drum = Drum()
    # game_world.add_object(drum, 1)

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

