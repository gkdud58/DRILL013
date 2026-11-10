import game_framework
from pico2d import *
import pico2d.pico2d as pico2d_core
import game_world

font = None
title_font = None


def init():
    global font, title_font

    font = load_font('C:/Windows/Fonts/malgun.ttf', 24)
    title_font = load_font('C:/Windows/Fonts/arialbd.ttf', 80)
    SDL_SetRenderDrawBlendMode(pico2d_core.renderer, SDL_BLENDMODE_BLEND)  # 반투명 사각형용

def finish():
    global font, title_font
    font = title_font = None

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()

def update():
    pass

def render():
    clear_canvas()
    game_world.render()  # 아래에 깔린 플레이 화면을 그대로 그림

    w, h = get_canvas_width(), get_canvas_height()
    gold = (255, 215, 120)

    # 화면 전체를 어둡게
    draw_rectangle(0, 0, w, h, 0, 0, 20, 150, True)
    # 중앙 띠와 금색 라인
    draw_rectangle(0, h // 2 - 70, w, h // 2 + 70, 0, 0, 0, 200, True)
    draw_rectangle(0, h // 2 + 70, w, h // 2 + 71, *gold, 255, True)
    draw_rectangle(0, h // 2 - 71, w, h // 2 - 70, *gold, 255, True)

    # 그림자 + 제목
    title_font.draw(w // 2 - 160 + 4, h // 2 + 14 - 4, 'PAUSED', (0, 0, 0))
    title_font.draw(w // 2 - 160, h // 2 + 14, 'PAUSED', gold)
    # 깜빡이는 안내 문구
    if int(get_time() * 1.5) % 2 == 0:
        font.draw(w // 2 - 120, h // 2 - 40, '일시정지 · P 키로 계속하기', (220, 220, 220))
    update_canvas()

def pause(): pass

def resume(): pass
