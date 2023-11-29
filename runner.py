from pico2d import *

import game_framework
import game_world

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# class Idle:
#     @staticmethod
#     def enter(runner, e):
#         runner.wait_time = get_time()
#
#     @staticmethod
#     def do(runner):
#         runner.frame = (runner.frame + 1) % 8
#         if get_time() - runner.wait_time > 1:
#             runner.state_machine.handle_event(('TIME_OUT', 0))
#
#     @staticmethod
#     def draw(runner):
#         runner.image.clip_draw(runner.frame * 16, 128, 100, 100, runner.x, runner.y)
#         # runner.image.draw(runner.x, runner.y)


class Idle:
    @staticmethod
    def enter(runner, e):
        runner.frame = 0
        runner.wait_time = get_time()

    @staticmethod
    def do(runner):
        # runner.frame = (runner.frame + 1) % 8
        runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if get_time() - runner.wait_time > 1:
            runner.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(runner):
        # runner.image.draw(runner.x, runner.y)
        runner.image.clip_draw(int(runner.frame) * 16, 128, 100, 100, runner.x, runner.y)



class Run:
    @staticmethod
    # def enter(runner, e):
    #     if space_down(e):
    #         pass

    @staticmethod
    def do(runner):
        runner.frame = (runner.frame + 1) % 8
        runner.x += RUN_SPEED_PPS * game_framework.frame_time
        runner.x = clamp(80, runner.x, 1280 - 80)
        # runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(runner):
        runner.image.clip_draw(runner.frame * 16, 128, 100, 100, runner.x, runner.y)


class StateMachine:
    def __init__(self, runner):
        self.runner = runner
        self.cur_state = Run
        self.transitions = {
            Idle: {space_down: Run},
            Run: {space_down: Idle}
        }

    def start(self):
        self.cur_state.enter(self.runner, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.runner)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.runner, e)
                self.cur_state = next_state
                self.cur_state.enter(self.runner, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.runner)


class Runner:
    def __init__(self):
        self.x, self.y = 600, 300
        self.frame = 0
        self.image = load_image('running.png')
        self.font = load_font('neodgm.TTF', 30)
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 10, self.y + 50, f'RUNNER', (255, 255, 0))

        # self.image.draw(400, 300)
        # self.image.clip_draw(self.frame * 16, 128, 100, 100, self.x, self.y)
