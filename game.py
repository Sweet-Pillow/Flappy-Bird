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

        self.bg = Bg().background

    def loop(self):

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.blit(self.bg, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    root = Game()
    root.loop()