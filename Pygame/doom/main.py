import pygame

from camera import Camera
from game import default_game


game = default_game

def main():
    while game.running:
        game.handle_events()

        game.update_physics()

        game.update_graphics()


if __name__ == "__main__":
    main()