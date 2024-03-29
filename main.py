# main.py
import pygame
import sys
from tile import Tile
from event_handler import EventHandler

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Setup
BLACK = (0, 0, 0)
RED = (255, 0, 0)
tile = Tile(RED, [0, 0, 0], 50, (screen_width / 2, screen_height / 2))

event_handler = EventHandler(tile)

running = True
while running:
    running = event_handler.handle_events()

    screen.fill(BLACK)
    tile.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()
