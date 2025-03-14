import pygame
from colors import *

SCALE = 8

class Player():
    def __init__(self, position: pygame.Vector2, angle=0):
        self.position = position
        self.angle = angle


    def move(self, vector):
        self.position += vector
    
    def draw(self, surface):
        pygame.draw.rect(
            surface,
            YELLOW,
            pygame.Rect(
                self.position.x - (SCALE / 2),
                self.position.y - (SCALE / 2),
                SCALE,
                SCALE
            )
        )