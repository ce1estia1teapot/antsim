import logging
import pygame as pg
import os
import sys

from pygame import Surface
from config.log_utils import setup_logging
from utils.utils import check_directories_exist

setup_logging(p_logging_config_fp='src/config/logging_config.yaml')
pg.init()

"""# Initializing Globals"""
dt = 0
m_clock = pg.time.Clock()
m_screen = pg.display.set_mode(size=(1280, 720))
m_game_running: bool = True
main_logger: logging.Logger = logging.getLogger('main')
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

test_surface_1: Surface = Surface(size=(100, 200))

check_directories_exist([main_dir, assets_dir])

# Applying Initial Settings
pg.display.set_caption(title='Antsim')
test_surface_1.fill(color='Red')

""" Initializing game start settings """
player_pos: pg.Vector2 = pg.Vector2(m_screen.get_width()/2, m_screen.get_height()/2)
player_color: str = 'red'
player_radius: int = 40

""" # ===== MAIN LOOP ===== """
while m_game_running:

    """ Event loop: Process events in the Event queue """
    for event in pg.event.get():
        # main_logger.debug(f'Handling {event.type} event: {event.dict}')
        match event.type:
            case pg.QUIT:
                m_game_running = False
                main_logger.debug(f'Handling {event.type} event: Quitting Game')

    """ Render next frame """
    m_screen.fill('white')

    pg.draw.circle(m_screen, player_color, player_pos, player_radius)

    # Detect input key
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        main_logger.debug(f'Key pressed: W')
        player_pos.y -= 150 * dt
    if keys[pg.K_s]:
        main_logger.debug(f'Key pressed: S')
        player_pos.y += 150 * dt
    if keys[pg.K_a]:
        main_logger.debug(f'Key pressed: A')
        player_pos.x -= 150 * dt
    if keys[pg.K_d]:
        main_logger.debug(f'Key pressed: D')
        player_pos.x += 150 * dt

    # Update display after frame is rendered
    pg.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = m_clock.tick(60) / 1000

pg.quit()
