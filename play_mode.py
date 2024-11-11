from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from bird import Bird

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            bird.handle_event(event)

def init():
    global grass
    #global boy
    global bird

    grass = Grass()
    game_world.add_object(grass, 0)

    #boy = Boy()
    #game_world.add_object(boy, 1)

    birds = []  # 새 리스트 초기화
    for i in range(10):  # 10번 반복
        bird = Bird()
        bird.x += i*50
        game_world.add_object(bird, 1)
        birds.append(bird)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # 성능 후진 PC 모사
    #delay(0.1)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

