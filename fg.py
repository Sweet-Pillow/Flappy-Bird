import pygame as pg


class Fg:
    def __init__(self, pos):
        self.foreground = pg.image.load('./assets/base.png')
        self.speed = 2
        self.pos = pos

    def move(self):
        self.pos[0] -= self.speed

        if self.pos[0] < -288:
            self.pos[0] = 288  + self.speed
