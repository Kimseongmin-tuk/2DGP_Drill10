from pico2d import *
import game_framework

PIXEL_PER_METER = (100.0 / 0.3)   # 약 333.33 (1미터 = 333.33픽셀)
METER_PER_PIXEL = (0.3 / 100.0)   # 0.003 (1픽셀 = 0.3cm)


BIRD_SPEED_MPS = 2.0  # 새가 초당 2미터 이동

class Bird:
    image = None

    def __init__(self, x=400, y=300, direction=1, frame=0):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y

        self.speed = BIRD_SPEED_MPS * PIXEL_PER_METER
        self.direction = direction
        self.frame = frame

        self.frame_width = 183
        self.frame_height = 168
        self.total_frames = 14
        self.frame_per_row = 5

        self.frame_time = 0
        self.frame_interval = 0.05

        self.screen_width = get_canvas_width()
        self.screen_height = get_canvas_height()

    def draw(self):
        col = self.frame % self.frame_per_row # 최대 5프레임
        row = self.frame // self.frame_per_row # 최대 3행

        if self.direction == 1:
            if row == 0:
                col = self.frame % 4
                self.image.clip_draw(col * self.frame_width, row * self.frame_height,
                                   self.frame_width, self.frame_height,
                                   self.x, self.y, 100, 100)
            else:
                self.image.clip_draw(col * self.frame_width, row * self.frame_height,
                                   self.frame_width, self.frame_height,
                                   self.x, self.y, 100, 100)
        else:
            if row == 0:
                col = self.frame % 4
                self.image.clip_composite_draw(col * self.frame_width, row * self.frame_height,
                                              self.frame_width, self.frame_height,
                                              0, 'h', self.x, self.y, 100, 100)
            else:
                self.image.clip_composite_draw(col * self.frame_width, row * self.frame_height,
                                              self.frame_width, self.frame_height,
                                              0, 'h', self.x, self.y, 100, 100)

    def update(self):
        self.x += self.speed * self.direction * game_framework.frame_time

        if self.x >= self.screen_width - 50:
            self.direction = -self.direction
        elif self.x <= 50:
            self.direction = -self.direction

        self.frame_time += game_framework.frame_time
        if self.frame_time >= self.frame_interval:
          self.frame = (self.frame + 1) % self.total_frames
          self.frame_time = 0