import pygame
from level import Map
from player import Player
from colors import *



class Game:
    def __init__(self, width, height, map: Map, player: Player, max_framerate=30):
        self.window = pygame.display.set_mode((width, height))
        self.max_framerate = max_framerate
        self.map = map
        self.player = player

        self.running = True
        self.clock = pygame.time.Clock()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move("forward")
                if event.key == pygame.K_a:
                    self.player.rotate("left")
                if event.key == pygame.K_s:
                    self.player.move("backward")
                if event.key == pygame.K_d:
                    self.player.rotate("right")


    def update_display(self):
        self.window.fill(DARK_GRAY)

        self.map.draw(
            self.window,
            64,
            (0, 0)
        )

        self.player.draw(self.window)

        pygame.display.update()
        self.clock.tick(self.max_framerate)