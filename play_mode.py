import random

from pico2d import *
import game_framework

import game_world
import server
import title_mode
from background import Background
from drum import Drum
from runner import Runner, Idle
from score import Score
from target_O import TargetO
from target_X import TargetX
from timer import Timer


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            server.runner.handle_event(event)


def init():
    global background
    global wait_time

    running = True

    wait_time = get_time()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.runner = Runner()
    game_world.add_object(server.runner, 2)

    server.score = Score()
    game_world.add_object(server.score, 3)

    server.timer = Timer()
    game_world.add_object(server.timer, 3)

    game_world.add_collision_pair('runner:drum', server.runner, None)


def finish():
    game_world.clear()
    pass


def update():
    global drum
    global runner
    global wait_time
    global targetO
    global targetX

    if server.runner.state_machine.cur_state != Idle:
        if get_time() - wait_time > random.randint(1, 3):
            targetO = TargetO()
            targetO.y -= random.randint(-100, 100)
            game_world.add_object(targetO, 1)
            wait_time = get_time()

        if get_time() - wait_time > random.randint(1, 5):
            targetX = TargetX()
            targetX.y -= random.randint(-100, 100)
            game_world.add_object(targetX, 1)
            wait_time = get_time()

    if server.runner.state_machine.cur_state != Idle:
        if get_time() - wait_time > (random.random() * 50) + 0.1:
        # if get_time() - wait_time > random.randint(1, 3):
            drum = Drum()
            game_world.add_collision_pair('runner:drum', None, drum)
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

    game_world.update()

    game_world.handle_collisions()

    # if game_world.collide(runner, drum):
    #     print('COLLISION runner:drum')


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

