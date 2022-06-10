import pygame as pg
from datetime import datetime


class Bg:
    def __init__(self):
        self.day = './assets/background-day.png'
        self.night = './assets/background-night.png'
        self.background = ''
        self.get_time()
    
    def get_time(self):
        if int(datetime.now().strftime("%H")) < 18:
            self.background = pg.image.load(self.day)
        
        else:
            self.background = pg.image.load(self.night)
