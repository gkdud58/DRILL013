import game_framework
from pico2d import *
import game_world
import pause_mode
import item_mode
from boy import Boy
from grass import Grass

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        elif item_mode.handle_event(boy, event):
            pass
        else:
            boy.handle_event(event)



def init():
    global boy

    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    item_mode.draw(boy)
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass

def resume():
    boy.sync_keys()
