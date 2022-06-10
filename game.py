import pygame
import sys
from bg import Bg
from fg import Fg
from bird import Bird


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

        self.bg1 = Bg([0, 0])
        self.bg2 = Bg([self.width, 0])

        self.fg1 = Fg([0, 400])
        self.fg2 = Fg([self.width, 400])

        self.bird = Bird([self.width//6, self.height//4])


    def loop(self):

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.blit(self.bg1.background, self.bg1.move())
            self.screen.blit(self.bg2.background, self.bg2.move())

            self.screen.blit(self.fg1.foreground, self.fg1.move())
            self.screen.blit(self.fg2.foreground, self.fg2.move())

            self.screen.blit(self.bird.bird, self.bird.pos)

            pygame.display.update()


if __name__ == '__main__':
    root = Game()
    root.loop()