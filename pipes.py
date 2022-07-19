import pygame as pg
import random


class PipeTop(pg.sprite.Sprite):
    def __init__(self, posX, posY):
        pg.sprite.Sprite.__init__(self)

        self.pipe_top_image = './assets/pipe-green.png'
        self.image = pg.transform.flip(pg.image.load(self.pipe_top_image), False, True).convert()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY 


class PipeBottom(pg.sprite.Sprite):
    def __init__(self, posX, distance):
        pg.sprite.Sprite.__init__(self)

        self.pipe_bottom_image = './assets/pipe-green.png'
        self.image = pg.image.load(self.pipe_bottom_image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = distance # 320 is the height of the pipe image


class Pipes:
    def __init__(self, posX, num_pipe):
        self.distanceY_between_pipes = 150
        self.distanceX_between_pipes = 190 
        self.speed = 2

        self.posX = posX + self.distanceX_between_pipes * num_pipe
        self.posY = random.randint(30, 220)
        
        self.pipe_top = PipeTop(self.posX, self.posY - 320)
        self.pipe_bottom = PipeBottom(self.posX, self.posY + self.distanceY_between_pipes)

        self.pipes = pg.sprite.Group()
        self.pipes.add(self.pipe_top)
        self.pipes.add(self.pipe_bottom)


    def move(self):
        self.pipe_top.rect.x -= self.speed
        self.pipe_bottom.rect.x -= self.speed
        self.respawn()

    def respawn(self):
        if self.pipe_top.rect.x <= -52:
            # 52 is the width of the pipe image, the pipe will respawn only when the pipe is fully outside the screen
            self.posX = self.distanceX_between_pipes * 2 - 52
            self.posY = random.randint(30, 220)
            self.pipe_top.rect.x = self.posX
            self.pipe_top.rect.y = self.posY - 320
            self.pipe_bottom.rect.x = self.posX
            self.pipe_bottom.rect.y = self.posY + self.distanceY_between_pipes

    def restart_pipe(self):
        self.posY = random.randint(30, 220)
        self.pipe_top.rect.x = self.posX
        self.pipe_top.rect.y = self.posY - 320
        self.pipe_bottom.rect.x = self.posX
        self.pipe_bottom.rect.y = self.posY + self.distanceY_between_pipes
