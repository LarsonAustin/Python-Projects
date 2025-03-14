import pygame
from game import Game
from level import Map
from player import Player


WIDTH, HEIGHT = 1024, 512

map = Map([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
])

player = Player(
    pygame.Vector2(128+8, 256+8)
)

def main():
    game = Game(WIDTH, HEIGHT, map, player)

    while game.running:
        game.handle_events()

        game.update_physics()

        game.update_display()


if __name__ == "__main__":
    main()