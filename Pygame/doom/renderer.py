import pygame
import numpy as np

class RenderWindow:
    def __init__(self, screen_size, max_framerate):
        self.screen_size = screen_size
        self.surface = pygame.display.set_mode(screen_size)
        self.max_framerate = max_framerate
        self.clock = pygame.time.Clock()

        self.running = True
        pygame.init()
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render_from_buffer(self, buffer: np.ndarray):
        surface = pygame.surfarray.make_surface(buffer.swapaxes(0, 1))
        self.surface.blit(surface, (0, 0))
        pygame.display.flip()

        self.clock.tick(30) 