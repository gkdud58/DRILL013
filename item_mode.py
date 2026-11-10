from pico2d import *

# 0: 공없음, 1: 작은공, 2: 큰공
KEY_TO_ITEM = {SDLK_0: 0, SDLK_1: 1, SDLK_2: 2}
ITEM_NAMES = {0: '공 없음', 1: '작은공', 2: '큰공'}

font = None


def handle_event(boy, event):
    # 게임을 멈추지 않고 키를 누르는 즉시 들고 있는 공을 바꿈
    if event.type == SDL_KEYDOWN and event.key in KEY_TO_ITEM:
        boy.ball_type = KEY_TO_ITEM[event.key]
        return True
    return False

def draw(boy):
    global font
    if font is None:
        font = load_font('C:/Windows/Fonts/malgun.ttf', 20)
    font.draw(10, get_canvas_height() - 20,
              f'[0]없음 [1]작은공 [2]큰공  현재: {ITEM_NAMES[boy.ball_type]}',
              (0, 0, 0))
