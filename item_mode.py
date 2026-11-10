from pico2d import *

# 0: 공없음, 1: 작은공, 2: 큰공
KEY_TO_ITEM = {SDLK_0: 0, SDLK_1: 1, SDLK_2: 2}
ITEM_NAMES = {0: '공 없음', 1: '작은공', 2: '큰공'}

font = None
image = None
is_open = False


def handle_event(boy, event):
    # 게임은 멈추지 않고 인벤토리 창만 열고 닫음
    global is_open
    if event.type != SDL_KEYDOWN:
        return False
    if event.key == SDLK_i:
        is_open = not is_open
        return True
    if is_open and event.key in KEY_TO_ITEM:
        boy.ball_type = KEY_TO_ITEM[event.key]
        is_open = False
        return True
    return False

def draw(boy):
    global font, image
    if font is None:
        font = load_font('C:/Windows/Fonts/malgun.ttf', 20)
        image = load_image('item_select.png')
    font.draw(10, get_canvas_height() - 20,
              f'[I] 인벤토리  현재: {ITEM_NAMES[boy.ball_type]}', (0, 0, 0))
    if is_open:
        image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
