import pygame as pg


class Fg(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('./assets/base.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 2

    def move(self):
        self.rect.x -= self.speed

        if self.rect.x < -288:
            self.rect.x = 288 + self.speed
