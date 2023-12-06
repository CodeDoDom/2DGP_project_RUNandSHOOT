from pico2d import *

import game_framework
import game_world
import server


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def mouse_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def mouse_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


def time_out(e):
    return e[0] == 'TIME_OUT'


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Runner Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Idle:
    @staticmethod
    def enter(runner, e):
        runner.action = 3
        runner.wait_time = get_time()
        runner.frame = 0

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if get_time() - runner.wait_time > 1.0:
            runner.state_machine.handle_event(('TIME_OUT', 0))
        # runner.frame = (runner.frame + 1) % 8
        runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(runner):
        # runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y, 128 * 2, 128 * 2)
        runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y)


class Run:
    @staticmethod
    def enter(runner, e):
        runner.action = 0
        runner.frame = 0

    @staticmethod
    def do(runner):
        # runner.x += RUN_SPEED_PPS * game_framework.frame_time
        # runner.x = clamp(80, runner.x, 1280 - 80)
        runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(runner):
        # runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y, 128 * 2, 128 * 2)
        runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y)

    @staticmethod
    def exit(runner, e):
        pass


class Shoot:
    @staticmethod
    def enter(runner, e):
        runner.action = 2
        runner.frame = 0
        runner.wait_time = get_time()

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if get_time() - runner.wait_time > 0.15:
            runner.state_machine.handle_event(('TIME_OUT', 0))

        runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1

    @staticmethod
    def draw(runner):
        # runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y, 128 * 2, 128 * 2)
        runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y)


class Jump:
    @staticmethod
    def enter(runner, e):
        runner.action = 1
        runner.frame = 3
        runner.wait_time = get_time()

    @staticmethod
    def exit(runner, e):
        pass

    @staticmethod
    def do(runner):
        if int(runner.frame) == 10:
            runner.state_machine.handle_event(('TIME_OUT', 0))
        runner.frame = (runner.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(runner):
        # runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y + 25, 128 * 2, 128 * 2)
        runner.image.clip_draw(int(runner.frame) * 128, runner.action * 128, 100, 100, runner.x, runner.y + 18)


class StateMachine:
    def __init__(self, runner):
        self.runner = runner
        self.cur_state = Idle
        self.transitions = {
            Idle: {time_out: Run},
            Run: {time_out: Idle, mouse_down: Shoot, space_down: Jump},
            Shoot: {time_out: Run},
            Jump: {time_out: Run}
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
    runner_shoot_target = None
    def __init__(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.action = 3
        self.image = load_image('runner_animation.png')
        self.font = load_font('neodgm.TTF', 30)
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.mx, self.my = 0, 0

        if not Runner.runner_shoot_target:
            Runner.runner_shoot_target = load_wav('gun_sound.wav')
            Runner.runner_shoot_target.set_volume(50)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.mx, self.my = event.x, 720 - 1 - event.y

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 30, self.y + 50, f'RUNNER', (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state_machine.cur_state == Run:
            return self.x - 8, self.y - 50, self.x + 18, self.y + 14
        elif self.state_machine.cur_state == Jump:
            return self.x - 8, self.y - 20, self.x + 18, self.y + 34
        else:
            return 0, 0, 0, 0

    def handle_collision(self, group, other):
        if group == 'runner:drum':
            # Runner.runner_shoot_target.play()
            # game_world.remove_object(self)
            print(f'hi')
