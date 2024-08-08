import logging
import pygame as pg

from src.utils.utils import load_image
from typing import Tuple
from pygame import Surface, Rect


main_logger: logging.Logger = logging.getLogger('main')

""" Classes for game objects """

class Fist(pg.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    fist_offset: Tuple
    image: Surface
    punching: bool
    rect: Rect

    def __init__(self, p_image: Surface = None, p_rect: Rect = None, p_fist_offset: Tuple = (-235, -80)):
        if p_image is None or not isinstance(p_image, Surface):
            main_logger.error(f'p_image argument cannot be None, must be Surface')
        if p_rect is None or not isinstance(p_rect, Rect):
            main_logger.error(f'p_rect argument cannot be None, must be Rect')

        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = p_image
        self.rect = p_rect
        self.fist_offset = p_fist_offset
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the fist back"""
        self.punching = False
