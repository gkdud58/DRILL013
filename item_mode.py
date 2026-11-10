import game_framework
from pico2d import *
import game_world

image = None


def init():
    global image
    image = load_image('item_select.png')

def finish():
    global image
    image = None

def handle_events():
    import play_mode  # 순환 import 방지

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mode.boy.ball_type = 0  # 공 없음
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.boy.ball_type = 1  # 작은공
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.boy.ball_type = 2  # 큰공
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()

def update():
    pass

def render():
    clear_canvas()
    game_world.render()  # 아래에 깔린 플레이 화면
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def pause(): pass

def resume(): pass
