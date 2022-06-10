import pygame as pg
from random import choice


class Bird:
    def __init__(self, pos):
        self.birds_images = {"yellow": ['./assets/yellowbird-downflap.png',
                                 './assets/yellowbird-midflap.png',
                                 './assets/yellowbird-upflap.png'],

                      "blue": ['./assets/bluebird-downflap.png',
                               './assets/bluebird-midflap.png',
                               './assets/bluebird-upflap.png'],

                      "red": ['./assets/redbird-downflap.png',
                              './assets/redbird-midflap.png',
                              './assets/redbird-upflap.png'], }
        self.bird_colors = ['yellow', 'blue', 'red']
        
        self.bird = pg.image.load(self.birds_images['yellow'][1])

        self.pos = pos
        self.gravity = 1
        
    def draw_bird(self):
        pass
