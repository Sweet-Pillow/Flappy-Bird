import pygame as pg
import random

class Pipes:
    def __init__(self, posX, num_pipe): 
        # num_pipe, defined by the order of creation of a pipe, for example, for pipe1 num_pipe=0, for pipe2 num_pipe=1 ...
        self.pipe_image = './assets/pipe-green.png'
        self.pipe_bottom = pg.image.load(self.pipe_image)
        self.pipe_top = pg.transform.flip(pg.image.load(self.pipe_image), False, True)
        
        self.distanceY_between_pipes = 150
        self.distanceX_between_pipes = 190
        self.posX = posX

        self.pipes = pg.Surface((52, 640 + self.distanceY_between_pipes)) #A surface that will conteins the two pipes

        self.pipes.blit(self.pipe_top, [0, 0])
        self.pipes.blit(self.pipe_bottom, [0, 320 + self.distanceY_between_pipes])

        self.pipes.set_colorkey((0, 0, 0))

        self.pos = [posX + self.distanceX_between_pipes * num_pipe, random.randint(-280, -100)]
        
        self.velocidade = 2

    def move(self):
        self.pos[0] -= self.velocidade
    
    def respawn_pipe(self):
        if self.pos[0] <= -52:
            # 52 is the width of the pipe image, the pipe will respawn only when the pipe is fully outside the screen
            self.pos[0] = self.distanceX_between_pipes * 3 - 52