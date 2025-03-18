import pygame
from pygame import Vector2
import math

import colors
from camera import Camera


RADIUS = 8


class Player:
    def __init__(self, position: Vector2):
        self.position = position
        self.direction = 0

    def direction_vector(self):
        return Vector2(math.cos(self.direction), math.sin(self.direction))

    def cast_ray(self):
        ray = self.direction_vector()

    def draw(self, surface: pygame.Surface, camera: Camera):
        pygame.draw.circle(
            surface,
            colors.BLUE,
            camera.to_screen(self.position),
            RADIUS,
        )