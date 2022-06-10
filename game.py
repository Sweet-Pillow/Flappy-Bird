import pygame
import sys
from bg import Bg


class Game:
    def __init__(self):
        pygame.init()

        self.width = 288
        self.height = 512

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        self.bg1 = Bg([0, 0])
        self.bg2 = Bg([self.width, 0])


    def loop(self):

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.blit(self.bg1.background, self.bg1.move())
            self.screen.blit(self.bg2.background, self.bg2.move())

            pygame.display.update()


if __name__ == '__main__':
    root = Game()
    root.loop()