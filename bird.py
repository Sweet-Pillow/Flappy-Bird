import pygame as pg
from random import choice


class Bird(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)

        self.pos = pos
        self.jump_height = 12
        self.gravity = 1
        self.rotation = 0
        self.bird_fly_update = 0  # Variable to control the fly animation speed
        self.bird_rotate_update = 0  # Variable to control the rotation animataion speed
        self.jumping = False    # Variable to turn off the gravity_force function while the bird is jumping
        
        self.birds_images = {"yellow": ['./assets/yellowbird-downflap.png',
                                        './assets/yellowbird-midflap.png',
                                        './assets/yellowbird-upflap.png',
                                        './assets/yellowbird-midflap.png'],

                             "blue": ['./assets/bluebird-downflap.png',
                                      './assets/bluebird-midflap.png',
                                      './assets/bluebird-upflap.png',
                                      './assets/bluebird-midflap.png'],

                             "red": ['./assets/redbird-downflap.png',
                                     './assets/redbird-midflap.png',
                                     './assets/redbird-upflap.png',
                                     './assets/redbird-midflap.png'], }

        self.bird_colors = choice(['yellow', 'blue', 'red'])
        self.bird_frame = 0
        self.bird = pg.image.load(self.birds_images[self.bird_colors][1]).convert()
        self.rect = self.bird.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


    def bird_control(self):
        if pg.key.get_pressed()[pg.K_SPACE] or self.jumping:
            self.jumping = True
            self.gravity = 1

            if self.jump_height > 0:
                self.rect.y -= self.jump_height
                self.jump_height -= 1
            else:
                self.jump_height = 12
                self.jumping = False

    def respawn(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def gravity_force(self, game_over=False):
        if self.jumping == False or game_over:
            self.rect.y += self.gravity
            self.gravity += 0.2

    def bird_animation(self):
        now = pg.time.get_ticks()

        if now - self.bird_fly_update > 60:
            self.bird_fly_update = now
            self.bird = pg.image.load(
                self.birds_images[self.bird_colors][self.bird_frame]).convert()
            self.bird = pg.transform.rotate(self.bird, self.rotation).convert()

            '''if self.jumping == False:
                if now - self.bird_rotate_update > 3:
                    self.bird_rotate_update = now
                    if self.rotation > -90:
                        self.rotation -= 10
            else:
                print('Pulando')
                if now - self.bird_rotate_update > 3:
                    self.bird_rotate_update = now
                    #self.rotation = 0
                    #if self.rotation < 90:
                    self.rotation += 30'''

            self.bird_frame = (self.bird_frame + 1) % 4
