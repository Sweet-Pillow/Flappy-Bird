import pygame as pg


class GameOver:
    def __init__(self):
        self.image = pg.image.load('./asstes/gameover.png')
        self.rect = self.image.get_rect()