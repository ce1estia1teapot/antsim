import logging
import pygame
import sys

from pygame import Surface

pygame.init()
main_logger: logging.Logger = logging.getLogger('main')

"""# Initializing display"""
screen = pygame.display.set_mode(size=(1280, 720))
pygame.display.set_caption(title='Antsim')

"""# Initializing Globals"""
clock = pygame.time.Clock()

test_surface_1: Surface = Surface(size=(100, 200))
test_surface_1.fill(color='Red')

""" # ===== MAIN LOOP ===== """
while True:
    # Event loop: Process events in the Event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(source=test_surface_1, dest=(0, 0))

    # Update display after frame is rendered
    pygame.display.update()
    clock.tick(60)