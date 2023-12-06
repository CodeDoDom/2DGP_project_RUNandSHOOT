from pico2d import *
import game_world
import game_framework
import server


def time_out(e):
    return e[0] == 'TIME_OUT'

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 30.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class Idle:
    @staticmethod
    def enter(drum, e):
        drum.wait_time = get_time()

    @staticmethod
    def exit(drum, e):
        pass

    @staticmethod
    def do(drum):
        if get_time() - drum.wait_time > 1.0:
            drum.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(drum):
        drum.image.clip_draw(0, 0, drum.w, drum.h, drum.x, drum.y)


class Move:
    @staticmethod
    def enter(drum, e):
        pass

    @staticmethod
    def exit(drum, e):
        pass

    @staticmethod
    def do(drum):
        # drum.x -= 1.0
        drum.x -= MOVE_SPEED_PPS*game_framework.frame_time

    @staticmethod
    def draw(drum):
        drum.image.clip_draw(0, 0, drum.w, drum.h, drum.x, drum.y)


class StateMachine:
    def __init__(self, drum):
        self.drum = drum
        self.cur_state = Idle
        self.transitions = {
            Idle: {time_out: Move},
            Move: {}
        }

    def start(self):
        self.cur_state.enter(self.drum, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.drum)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.drum, e)
                self.cur_state = next_state
                self.cur_state.enter(self.drum, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.drum)


class Drum:
    # image = None
    def __init__(self):
        self.x, self.y = 1300, 160   # 이 y 좌표로 하면 캐릭터 점프 위치랑  완벽하게 맞음
        self.w, self.h = 128, 128
        self.image = load_image('drum.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.crash = False

    def update(self):
        if self.x <= -20:
            game_world.remove_object(self)
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.crash == False:
            return self.x - 8, self.y - 64, self.x + 7, self.y - 40
        else:
            return -10, -10, -10, -10   # return 0, 0, 0, 0일 시 오류

    def handle_collision(self, group, other):
        if group == 'runner:drum':
            self.crash = True
            server.score.score -= 2
