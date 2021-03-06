from pico2d import *
from random import *



class Boy:
    def __init__(self):
        self.x = randint(100,600)
        self.y = randint(100,600)
        self.image = load_image('../res/run_animation.png')
        self.dx = random()
        self.frame = randint(0,7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.dx * 5
        self.frame = (self.frame + 1) % 8
        if self.x >= 800:
            self.x = 0

class Grass:
    def __init__(self):
        self.x, self.y = 400,30
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(self.x,self.y)