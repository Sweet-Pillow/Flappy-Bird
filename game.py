import pygame
import sys
from bg import Bg
from fg import Fg
from bird import Bird
from pipes import Pipes
from gamestart import GameStart
from gameover import GameOver


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
        self.game_start = GameStart(self.width, self.height)
        self.game_over = GameOver(self.width, self.height)

        self.bg1 = Bg([0, 0])
        self.bg2 = Bg([self.width, 0])

        self.pipe1 = Pipes(self.width, 0)
        self.pipe2 = Pipes(self.width, 1)

        self.fg1 = Fg([0, 400])
        self.fg2 = Fg([self.width, 400])

        self.bird = Bird([self.width//6, self.height//4])

        # Defining the sprite group of the obstacles
        self.all_obstacles_group = pygame.sprite.Group()
        self.all_pipes_group = pygame.sprite.Group()
        self.all_fgs_group = pygame.sprite.Group()

        self.all_pipes_group.add(self.pipe1.pipes, self.pipe2.pipes)
        self.all_fgs_group.add(self.fg1, self.fg2)

        self.all_obstacles_group.add(self.all_pipes_group, self.all_fgs_group)

    def start(self):
        run = True
        
        while run:
            self.clock.tick(60)

            #   Getting Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(self.bg1.background, self.bg1.pos)
            self.screen.blit(self.bg2.background, self.bg2.pos)

            self.all_fgs_group.draw(self.screen)

            self.screen.blit(self.game_start.image, self.game_start.rect)

            #   Updating
            self.bg1.move()
            self.bg2.move()

            self.fg1.move()
            self.fg2.move()

            #   Animation
            self.game_start.animation()

            #   Control
            run = self.game_start.pressed_start()

            pygame.display.update()
        
        self.loop()

    def over(self):
        run = True

        while run:
            self.clock.tick(60)

            #   Getting Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg1.background, self.bg1.pos)
            self.screen.blit(self.bg2.background, self.bg2.pos)

            self.all_obstacles_group.draw(self.screen)

            self.screen.blit(self.bird.bird, self.bird.rect)

            self.screen.blit(self.game_over.image, self.game_over.rect)
            
            #   Animation
            self.game_over.animation()

            #if not (pygame.sprite.collide_rect(self.bird, self.fg1) or pygame.sprite.collide_rect(self.bird, self.fg2)):
            if not (pygame.sprite.spritecollide(self.bird, self.all_fgs_group, False)):
                print(self.bird.rect)
                self.bird.gravity_force(True)
            
            else:
                run = self.game_over.pressed_restart()

            pygame.display.update()

        self.pipe1.restart_pipe()
        self.pipe2.restart_pipe()

        self.bird.respawn()
        
        self.loop()

    def loop(self):
        run = True
        while run:
            self.clock.tick(60)

            #   Getting Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #   Drawing on screen
            self.screen.blit(self.bg1.background, self.bg1.pos)
            self.screen.blit(self.bg2.background, self.bg2.pos)

            self.all_obstacles_group.draw(self.screen)

            self.screen.blit(self.bird.bird, self.bird.rect)

            #   Updating
            self.bg1.move()
            self.bg2.move()

            self.pipe1.move()
            self.pipe2.move()

            self.fg1.move()
            self.fg2.move()

            self.bird.gravity_force()
            self.bird.bird_control()

            self.bird.bird_animation()

            #   Colission check
            if pygame.sprite.spritecollide(self.bird, self.all_obstacles_group, False):
                run = False

            pygame.display.update()

        self.over()

if __name__ == '__main__':
    root = Game()
    root.start()
