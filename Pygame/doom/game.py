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
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.player.move("forward") # forward
        if pressed[pygame.K_a]:
            self.player.turn("left") # left
        if pressed[pygame.K_s]:
            self.player.move("back") # back
        if pressed[pygame.K_d]:
            self.player.turn("right") # right

    
    def update_physics(self):
        pass #self.player.cast_ray(self.map)

    def update_graphics(self):
        self.window.fill(colors.DARK_GREY)

        self.map.draw(self.window, pygame.Vector2(0, 0))
        self.player.draw(self.window, self.cameras["player"], self.map.grid)

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