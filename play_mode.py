from pico2d import *
from bird import Bird
import game_world
import random

import game_framework


birds = []

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def init():
    global running
    global birds

    running = True

    for i in range(10):
        bird = Bird()
        bird.y = random.randint(100, 500)
        bird.direction = random.choice([-1, 1])
        birds.append(bird)

        game_world.add_object(bird, 0)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

