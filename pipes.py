import pygame as pg

class Pipes:
    def __init__(self, pos):
        self.pipe_image = './assets/pipe-green.png'
        self.pipe_bottom = pg.image.load(self.pipe_image)
        self.pipe_top = pg.transform.flip(pg.image.load(self.pipe_image), False, True)
        
        self.distance_between_pipes = 150
        
        self.pipes = pg.Surface((52, 640 + self.distance_between_pipes)) #A surface that will conteins a the two pipes

        self.pipes.blit(self.pipe_top, [0, 0])
        self.pipes.blit(self.pipe_bottom, [0, 320 + self.distance_between_pipes])

        self.pipes.set_colorkey((0, 0, 0))

        self.pos = pos
        self.velocidade = 5

