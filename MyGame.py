# imports

import sys
import pygame

# constants
BOARD_SIZE = WIDTH, HEIGHT = 800, 600
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 0, 255, 85


class MyGame:
    def _init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(DEAD_COLOR)

            # screen.blit(ball, ballrect) blit to draw the scene, then flip to push it into memory
            pygame.display.flip()

if _name_ == '_main_':
    game = MyGame()
    game.run()
