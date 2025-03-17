import pygame
from pygame import Vector2

from camera import Camera
from game import default_game


game = default_game

c = Camera(Vector2(0, 0), Vector2(2, 2), Vector2(0, 512), Vector2(512, 0))

print(c.to_screen(Vector2(0.5, 1.75)))

def main():
    while game.running:
        game.handle_events()

        game.update_physics()

        game.update_graphics()


if __name__ == "__main__":
    main()