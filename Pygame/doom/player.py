import pygame
import math
from colors import *


SCALE = 8
MOVE_SPEED = 16
ROTATION_SPEED = math.tau / 16
POINTER_LENGTH = 16


class Player():
    def __init__(self, position: pygame.Vector2, angle=0):
        self.position = position
        self.angle = angle


    def angle_vector(self):
        return pygame.Vector2(math.cos(self.angle), math.sin(self.angle))


    def cast_ray(self, map, scale):
        position = self.position // scale


        if math.pi > self.angle > 0: # Facing down
            offset = 1 / math.tan(self.angle)
            ray_x = ((self.position.y - (self.position.y // scale)) * offset) + self.position.x
            print(ray_x)


        if math.tau > self.angle > math.pi: # Facing up
            offset = -1 / math.tan(self.angle)
            ray_x = ((self.position.y - (self.position.y // scale)) * offset) + self.position.x
            print(ray_x)


    def move(self, direction):
        vector = self.angle_vector() * MOVE_SPEED
        if direction == "forward":
            self.position += vector
        if direction == "backward":
            self.position -= vector

    def rotate(self, direction):
        if direction == "right":
            self.angle += ROTATION_SPEED
        if direction == "left":
            self.angle -= ROTATION_SPEED
        self.angle = self.angle % math.tau
    
    def draw(self, surface):
        pygame.draw.line(
            surface,
            YELLOW,
            self.position,
            (self.angle_vector() * POINTER_LENGTH) + self.position
        )
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