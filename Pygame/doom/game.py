import pygame
import colors


class Game:
    def __init__(self, window_size, max_framerate):
        self.window = pygame.display.set_mode(window_size)
        self.max_framerate = max_framerate

        self.clock = pygame.time.Clock()
        self.running = True
    
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

        pygame.display.update()
        self.clock.tick(self.max_framerate)





WIDTH, HEIGHT = 1024, 512
MAX_FRAMERATE = 30

default_game = Game((WIDTH, HEIGHT), MAX_FRAMERATE)