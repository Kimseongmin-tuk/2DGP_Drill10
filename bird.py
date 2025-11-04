from pico2d import *
import game_framework

class Bird:
    image = None

    def __init__(self, x=400, y=300, speed=200, direction=1, frame=0):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.frame = frame

        self.frame_width = 183
        self.frame_height = 168
        self.total_frames = 13
        self.frame_per_row = 5

        self.frame_time = 0
        self.frame_interval = 0.05

        self.screen_width = get_canvas_width()
        self.screen_height = get_canvas_height()

    def draw(self):
        col = self.frame % self.frame_per_row # 최대 5프레임
        row = self.frame // self.frame_per_row # 최대 3행

        if row == 0:
            col = self.frame % 4
            self.image.clip_draw(col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height, self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height, self.x, self.y, 100, 100)

    def update(self):
        self.x += self.speed * self.direction * game_framework.frame_time
        self.frame_time += game_framework.frame_time

        if self.frame_time >= self.frame_interval:
          self.frame = (self.frame + 1) % self.total_frames
          self.frame_time = 0