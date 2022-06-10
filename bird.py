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

        self.bird_colors = choice(['yellow', 'blue', 'red'])

        self.bird = pg.image.load(self.birds_images[self.bird_colors][1])

        self.pos = pos
        self.jump = 10
        self.gravity = 1
        self.jumping = False
        self.pressed = False

    def bird_control(self):
        if pg.key.get_pressed()[pg.K_SPACE] or self.pressed:
            self.jumping = True
            self.pressed = True
            self.gravity = 1

            if self.jump > 0:
                self.pos[1] -= self.jump
                self.jump -= 1
            else:
                self.jump = 10
                self.pressed = False
                self.jumping = False

    def gravity_force(self):
        if self.jumping == False:
            self.pos[1] += self.gravity 
            self.gravity += 0.2
            