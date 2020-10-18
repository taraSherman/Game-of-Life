import pygame
vector = pygame.math.Vector2

class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = vector(x, y)
        self.width, self.height = 1000, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = self.position

    def draw(self):
        self.image.fill((25, 53, 76))
        self.screen.blit(self.image, (self.position.x, self.position.y))