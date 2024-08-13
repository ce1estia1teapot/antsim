import logging
import pygame as pg

from src.main import load_image
from typing import Tuple
from pygame import Surface, Rect
from pygame.sprite import Sprite

main_logger: logging.Logger = logging.getLogger('main')

""" Classes for game objects """


class Fist(Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    fist_offset: Tuple
    image: Surface
    punching: bool
    rect: Rect

    def __init__(self, p_im_directory: str = None, p_fist_offset: Tuple = (-235, -80)):
        if p_im_directory is None:
            main_logger.error(
                f'Provided image parent directory is None. Parent Directory: {p_im_directory}')
            return

        Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("fist.jpg", p_im_directory)
        self.fist_offset = p_fist_offset
        self.punching = False

    def update(self) -> None:
        """move the fist based on the mouse position"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target) -> bool:
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self) -> None:
        """called to pull the fist back"""
        self.punching = False


class Chimp(Sprite):
    """moves a monkey critter across the screen. it can spin the
    monkey when it is punched."""

    def __init__(self, p_im_directory: str = None):
        if p_im_directory is None:
            main_logger.error(
                f'Provided image parent directory is None. Parent Directory: {p_im_directory}')
            return

        Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("chimp.png", p_im_directory, -1, 0.5)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False

    def update(self):
        """walk or spin, depending on the monkeys state"""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """move the monkey across the screen, and turn at the ends"""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """spin the monkey image"""
        center = self.rect.center
        self.dizzy += 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pg.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        main_logger.info('Punched!')
        """this will cause the monkey to start spinning"""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image
