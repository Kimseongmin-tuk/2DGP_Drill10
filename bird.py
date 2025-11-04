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



    def draw(self):
        self.image.clip_draw()

    def update(self):
        pass