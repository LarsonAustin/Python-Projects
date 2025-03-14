import pygame
from colors import *

class Map():
    def __init__(self, map):
        self.grid = map

        self.width = len(self.grid[0])
        self.height = len(self.grid)


    def draw(self, surface, scale, origin, border=1):
        for y in range(self.height):
            for x in range(self.width):
                color = WHITE if self.grid[y][x] else BLACK
                pygame.draw.rect(
                    surface,
                    color,
                    pygame.Rect(
                        origin[0] + (x * scale) + border,
                        origin[1] + (y * scale) + border,
                        scale - (border * 2),
                        scale - (border * 2)
                    )
                )