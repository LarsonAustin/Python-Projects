import pygame

import colors

SCALE = 64
MARGIN = 2

class Map:
    def __init__(self, grid):
        self.grid = grid

    def draw(self, surface: pygame.Surface, origin: pygame.Vector2):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                position = pygame.Vector2(
                    (y * SCALE) + MARGIN,
                    (x * SCALE) + MARGIN
                )
                pygame.draw.rect(
                    surface,
                    colors.WHITE if self.grid[x][y] else colors.BLACK,
                    pygame.Rect(
                        position,
                        pygame.Vector2(SCALE - (MARGIN), SCALE - (MARGIN))
                    )
                )