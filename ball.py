from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}
    files = {1: 'ball21x21.png', 2: 'ball41x41.png'}

    @staticmethod
    def get_image(kind):
        if kind not in Ball.images:
            Ball.images[kind] = load_image(Ball.files[kind])
        return Ball.images[kind]

    def __init__(self, x, y, velocity, kind=1):
        self.image = Ball.get_image(kind)
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
