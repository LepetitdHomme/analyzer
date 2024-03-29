# event_handler.py
import pygame

class EventHandler:
    def __init__(self, tile):
        self.tile = tile
        pygame.key.set_repeat(100, 50) # delay, interval

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_i:
                    self.tile.rotate(-5, 0)
                elif event.key == pygame.K_k:
                    self.tile.rotate(5, 0)
                elif event.key == pygame.K_j:
                    self.tile.rotate(0, -5)
                elif event.key == pygame.K_l:
                    self.tile.rotate(0, 5)
        return True
