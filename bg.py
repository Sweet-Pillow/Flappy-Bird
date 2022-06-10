import pygame as pg
from datetime import datetime


class Bg:
    def __init__(self, pos):
        self.day = './assets/background-day.png'
        self.night = './assets/background-night.png'
        self.background = ''
        self.speed = 3
        self.pos = pos
        self.get_time()
    
    def get_time(self):
        if int(datetime.now().strftime("%H")) < 18:
            self.background = pg.image.load(self.day)
        
        else:
            self.background = pg.image.load(self.night)

    def move(self):

        self.pos[0] -= self.speed

        if self.pos[0] < -288:
            self.pos[0] = 288  + self.speed

        return self.pos
