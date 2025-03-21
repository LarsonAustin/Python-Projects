import pygame
from pygame import Vector2
import math

import colors
from camera import Camera
from ray import Ray


RADIUS = 8
MOVE_SPEED = 0.05
TURN_SPEED = 0.05
PLAYER_COLOR = colors.ORANGE


class Player:
    def __init__(self, position: Vector2):
        self.position = position
        self.direction = 0

    def direction_vector(self):
        return Vector2(math.cos(self.direction), math.sin(self.direction))

    def cast_ray(self, map):
        ray = Ray(self.direction, self.position)
        return ray.cast(map)

    def draw(self, surface: pygame.Surface, camera: Camera, map):
        pygame.draw.line(
            surface,
            colors.YELLOW,
            camera.to_screen(self.position),
            camera.to_screen(self.position + self.cast_ray(map)),
            2
        )
        pygame.draw.circle(
            surface,
            PLAYER_COLOR,
            camera.to_screen(self.position),
            RADIUS,
        )
        pygame.draw.line(
            surface,
            PLAYER_COLOR,
            camera.to_screen(self.position),
            camera.to_screen(self.position + (self.direction_vector() * 0.5)),
            2
        )

    def move(self, direction):
        if direction == "forward":
            self.position += self.direction_vector() * MOVE_SPEED
        if direction == "back":
            self.position -= self.direction_vector() * MOVE_SPEED
    
    def turn(self, direction):
        if direction == "right":
            self.direction -= TURN_SPEED
        if direction == "left":
            self.direction += TURN_SPEED
        self.direction = self.direction % math.tau