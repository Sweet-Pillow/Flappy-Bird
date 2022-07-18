import pygame as pg
import random


class PipeTop(pg.sprite.Sprite):
    def __init__(self, posX, posY):
        pg.sprite.Sprite.__init__(self)

        self.pipe_top_image = './assets/pipe-green.png'
        self.image = pg.transform.flip(pg.image.load(self.pipe_top_image), False, True)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY 


class PipeBottom(pg.sprite.Sprite):
    def __init__(self, posX, distance):
        pg.sprite.Sprite.__init__(self)

        self.pipe_bottom_image = './assets/pipe-green.png'
        self.image = pg.image.load(self.pipe_bottom_image)
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

    def respawn_pipe(self):
        if self.pipe_top.rect.x <= -52:
            # 52 is the width of the pipe image, the pipe will respawn only when the pipe is fully outside the screen
            self.posX = self.distanceX_between_pipes * 2 - 52
            self.posY = random.randint(30, 220)
            self.pipe_top.rect.x = self.posX
            self.pipe_top.rect.y = self.posY - 320
            self.pipe_bottom.rect.x = self.posX
            self.pipe_bottom.rect.y = self.posY + self.distanceY_between_pipes


'''class Pipes(pg.sprite.Sprite):
    def __init__(self, posX, num_pipe): 
        pg.sprite.Sprite.__init__(self)

        # num_pipe, defined by the order of creation of a pipe, for example, for pipe1 num_pipe=0, for pipe2 num_pipe=1 ...
        self.distanceY_between_pipes = 150
        self.distanceX_between_pipes = 190
        self.posX = posX

        self.pipe_image = './assets/pipe-green.png'
        self.pipes = pg.Surface((52, 640 + self.distanceY_between_pipes)) #A surface that will conteins the two pipes
        self.rect = self.pipes.get_rect()
        self.rect.x = posX + self.distanceX_between_pipes * num_pipe
        self.rect.y = random.randint(-280, -100)

        self.pipe_top = pg.transform.flip(pg.image.load(self.pipe_image), False, True)
        self.pipe_top_rect = self.pipe_top.get_rect()
        self.pipe_top_rect.x = 0
        self.pipe_top_rect.y = 0

        self.pipe_bottom = pg.image.load(self.pipe_image)
        self.pipe_bottom_rect = self.pipe_bottom.get_rect()
        self.pipe_bottom_rect.x = 0
        self.pipe_bottom_rect.y = 320 + self.distanceY_between_pipes

        self.pipes.blit(self.pipe_top, [0, 0])
        self.pipes.blit(self.pipe_bottom, [0, 320 + self.distanceY_between_pipes])

        self.pipes.set_colorkey((0, 0, 0))

        #self.pos = [posX + self.distanceX_between_pipes * num_pipe, random.randint(-280, -100)]
        
        self.velocidade = 2

    def move(self):
        #self.pos[0] -= self.velocidade
        self.rect.x -= self.velocidade
    
    def respawn_pipe(self):
        if self.rect.x <= -52:
            # 52 is the width of the pipe image, the pipe will respawn only when the pipe is fully outside the screen
            self.rect.x = self.distanceX_between_pipes * 3 - 52
            self.rect.y = random.randint(-280, -100)
    
    def pipes_rects(self):
        return [self.pipe_bottom_rect, self.pipe_top_rect, self.rect]'''
