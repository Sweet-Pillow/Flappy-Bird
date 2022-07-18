import pygame
import sys
from bg import Bg
from fg import Fg
from bird import Bird
from pipes import Pipes


class Game:
    def __init__(self):
        pygame.init()

        self.width = 288
        self.height = 512

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Flappy Bird')
        self.icon = pygame.image.load('./assets/yellowbird-downflap.png')
        pygame.display.set_icon(pygame.transform.scale(self.icon, (32, 32)))
        self.clock = pygame.time.Clock()

        # Instantiating objects
        self.bg1 = Bg([0, 0])
        self.bg2 = Bg([self.width, 0])

        self.pipe1 = Pipes(self.width, 0)
        self.pipe2 = Pipes(self.width, 1)

        self.fg1 = Fg([0, 400])
        self.fg2 = Fg([self.width, 400])

        self.bird = Bird([self.width//6, self.height//4])

        # Defining the sprite group of the obstacles
        self.obstacles_sprites = pygame.sprite.Group()
        self.obstacles_sprites.add(self.pipe1.pipes)
        self.obstacles_sprites.add(self.pipe2.pipes)
        self.obstacles_sprites.add(self.fg1)
        self.obstacles_sprites.add(self.fg2)

    def start(self):
        pass

    def game_over(self):
        pass

    def loop(self):

        while True:
            self.clock.tick(60)

            #   Getting Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #   Drawing on screen
            self.screen.blit(self.bg1.background, self.bg1.pos)
            self.screen.blit(self.bg2.background, self.bg2.pos)

            '''self.screen.blit(self.pipe1.pipes, self.pipe1.rect)
            self.screen.blit(self.pipe2.pipes, self.pipe2.rect)
            self.screen.blit(self.pipe3.pipes, self.pipe3.rect)

            self.screen.blit(self.fg1.foreground, self.fg1.rect)
            self.screen.blit(self.fg2.foreground, self.fg2.rect)'''

            self.obstacles_sprites.draw(self.screen)

            self.screen.blit(self.bird.bird, self.bird.rect)

            #   Updating
            self.bg1.move()
            self.bg2.move()

            self.pipe1.move()
            self.pipe2.move()

            self.pipe1.respawn_pipe()
            self.pipe2.respawn_pipe()

            self.fg1.move()
            self.fg2.move()

            self.bird.gravity_force()
            self.bird.bird_control()

            self.bird.bird_animation()

            #   Colission check
            if pygame.sprite.spritecollide(self.bird, self.obstacles_sprites, False):
                print('colidiu no chão')
                print(pygame.sprite.spritecollide(self.bird, self.obstacles_sprites, False))

            pygame.display.update()


if __name__ == '__main__':
    root = Game()
    root.loop()
