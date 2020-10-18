from game import *

if __name__ == '__main__':
    game = Game()
    game.run()

# import pygame
# import sys

# WIDTH, HEIGHT = 800, 800
# BACKGROUND = (42, 21, 13)

# def get_events():
#     global running
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT():
#             running = False

# def update():
#     pass

# def draw():
#     window.fill(BACKGROUND)

# pygame.init()
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()

# running = True
# while running:
#     get_events()
#     update()
#     draw()
#     pygame.display.update()
#     clock.tick()
# pygame.quit()
# sys.exit()
