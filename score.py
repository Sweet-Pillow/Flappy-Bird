import pygame as pg


class Score:
    def __init__(self, width):
        self.number_images = ['./assets/0.png', './assets/1.png', './assets/2.png', './assets/3.png',
                              './assets/4.png', './assets/5.png', './assets/6.png', './assets/7.png',
                              './assets/8.png', './assets/9.png']
        
        self.score = 0
        self.score_surface = pg.Surface((72, 36))
        self.score_rect = self.score_surface.get_rect()
        self.score_rect.topright = (width, 20)
        self.score_surface.set_colorkey((0, 0, 0))

        self.digit1 = pg.image.load(self.number_images[self.score])
        self.digit1_rect = self.digit1.get_rect()
        self.digit1_rect.center = (72//2, 36//2)

        self.digit2 = pg.image.load(self.number_images[self.score])
        self.digit2_rect = self.digit2.get_rect()

        self.digit3 = pg.image.load(self.number_images[self.score])
        self.digit3_rect = self.digit3.get_rect()

        self.score_surface.blit(self.digit1, self.digit1_rect)

    def score_update(self):
        self.score += 1
        self.score_surface.fill((0, 0, 0)) # Using this to fix ghost image

        match len(str(self.score)):
            case 1:
                self.digit1 = pg.image.load(self.number_images[self.score])
                self.digit1_rect.center = (72//2, 36//2)
                self.score_surface.blit(self.digit1, self.digit1_rect)

            case 2:

                self.digit1 = pg.image.load(self.number_images[int(str(self.score)[0])])
                self.digit1_rect.center = (72//2 - 12, 36//2)
                self.digit2 = pg.image.load(self.number_images[int(str(self.score)[1])])
                self.digit2_rect.center = (72//2 + 12, 36//2)
                self.score_surface.blits(((self.digit1, self.digit1_rect),
                                         (self.digit2, self.digit2_rect)))
            case 3:
                self.digit1 = pg.image.load(self.number_images[int(str(self.score)[0])])
                self.digit1_rect.topright = (72//3, 0)
                self.digit2 = pg.image.load(self.number_images[int(str(self.score)[1])])
                self.digit2_rect.center = (72//2, 36//2)
                self.digit3 = pg.image.load(self.number_images[int(str(self.score)[2])])
                self.digit3_rect.topright = (72, 0)
                self.score_surface.blits(((self.digit1, self.digit1_rect),
                                         (self.digit2, self.digit2_rect),
                                         (self.digit3, self.digit3_rect)))

    def reset(self):
        self.score = 0
        self.score_surface.fill((0, 0, 0))
        self.digit1 = pg.image.load(self.number_images[self.score])
        self.digit1_rect.center = (72//2, 36//2)
        self.score_surface.blit(self.digit1, self.digit1_rect)