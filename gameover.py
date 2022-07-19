import pygame as pg


class GameOver:
    def __init__(self, width, height):
        self.image = pg.image.load('./assets/gameover.png').convert_alpha()
        self.original_image = pg.image.load('./assets/gameover.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width//2, height//2)

        self.width = width
        self.height = height

        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.animation_update = 0
        self.scale = 1
        self.size = 1

    def animation(self):
        now = pg.time.get_ticks()

        if now - self.animation_update > 10:
            self.animation_update = now
            self.image = pg.transform.scale(
                self.original_image, (self.image_width * self.scale, self.image_height * self.scale))
            self.rect = self.image.get_rect()
            self.rect.center = (self.width//2, self.height//2)
            self.scale += 0.01 * self.size

            if self.scale >= 1.1:
                self.size = -1
            
            elif self.scale <= 0.9:
                self.size = 1
    
    def pressed_restart(self):
        if pg.key.get_pressed()[pg.K_SPACE]:
            return False
        return True