from pico2d import *
import game_world
import game_framework


def time_out(e):
    return e[0] == 'TIME_OUT'


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
            # drum.x -= 1

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
        drum.x -= 1.0

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
        self.x, self.y = 720, 160 # 이 y 좌표로 하면 캐릭터 점프 위치랑  완벽하게 맞음
        self.w, self.h = 128, 128
        self.image = load_image('drum.png')
        # self.x, self.y = 120, 110
        # self.image = load_image('drum_new.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        # self.x -= 1
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        # self.image.clip_draw(0, 0, self.w, self.h, self.x, self.y)
        # self.image.clip_draw(0, 0, 35, 30, self.x, self.y)
        self.state_machine.draw()
