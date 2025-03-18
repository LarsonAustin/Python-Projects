import pygame

import colors
from map import Map
from player import Player
from camera import Camera


class Game:
    def __init__(self, window_size, max_framerate, player: Player, map: Map, cameras):
        self.window = pygame.display.set_mode(window_size)
        self.max_framerate = max_framerate
        self.map = map
        self.player = player

        self.clock = pygame.time.Clock()
        self.running = True
        self.cameras = cameras
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("forward pressed\n") # forward
                if event.key == pygame.K_a:
                    print("left pressed\n") # left
                if event.key == pygame.K_s:
                    print("back pressed\n") # back
                if event.key == pygame.K_d:
                    print("right pressed\n") # right
    
    def update_physics(self):
        pass

    def update_graphics(self):
        self.window.fill(colors.DARK_GREY)

        self.map.draw(self.window, pygame.Vector2(0, 0))
        self.player.draw(self.window, self.cameras["player"])

        pygame.display.update()
        self.clock.tick(self.max_framerate)





WIDTH, HEIGHT = 1024, 512
MAX_FRAMERATE = 30
MAP = Map([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])
PLAYER = Player(pygame.Vector2(1.1, 2.1))
CAMERAS = {
    "player" : Camera(pygame.Vector2(0, 0), pygame.Vector2(8, 8), pygame.Vector2(0, 512), pygame.Vector2(512, 0))
}

default_game = Game((WIDTH, HEIGHT), MAX_FRAMERATE, PLAYER, MAP, CAMERAS)