import pygame
from settings import *

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((18, 18))
        self.rect = self.image.get_rect()
        self.friends = []
        self.alive_friends = 0

    def update(self):
        self.rect.topleft = (self.grid_x * 20, self.grid_y * 20)

    def draw(self):
        if self.alive:
            self.image.fill(LIVE_CELL)
        else:
            self.image.fill(BACKGROUND)
            pygame.draw.rect(self.image, DEAD_CELL, (1, 1, 18, 18))
        self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20))

    def get_friends(self, grid):
        friend_list = [
            [1, 1],
            [-1, -1],
            [-1, 1],
            [1, -1],
            [0, -1],
            [0, 1],
            [1, 0],
            [-1, 0]]
        for friend in friend_list:
            friend[0] += self.grid_x
            friend[1] += self.grid_y
        for friend in friend_list:
            if friend[0] < 0:
                friend[0] += 30
            if friend[1] < 0:
                friend[1] += 30
            if friend[1] > 29:
                friend[1] -= 30
            if friend[0] > 29:
                friend[0] -= 30
        for friend in friend_list:
            try:
                self.friends.append(grid[friend[1]][friend[0]])
            except:
                print(friend)

    def live_friends(self):
        count = 0
        for friend in self.friends:
            if friend.alive:
                count += 1

        self.alive_friends = count
