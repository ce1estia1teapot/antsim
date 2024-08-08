import logging
import os
import pygame as pg

from typing import List
from pygame import Surface, Rect

main_logger: logging.Logger = logging.getLogger('main')

def check_directories_exist(p_directories: List[str]) -> None:
    for directory in p_directories:
        try:
            os.makedirs(directory)
            main_logger.debug(f'Creating directory: {directory}')
        except OSError:
            main_logger.warning(f'Error creating directory - Directory already exists: {directory}')


""" ===========  Resource creation functions =========== """


def load_image(name: str = None, parent_dir: str = None, colorkey=-1, scale: int = 1):
    """
    Loads, an image, converts the pixel space, performs optional scaling,
    :param name:
    :param parent_dir:
    :param colorkey: A pg colorkey? An enum int I think
    :param scale:
    :return: A tuple containing a Surface representing the image, and a rectangle representing a bounding box
    """

    if name is None or not isinstance(name, str):
        main_logger.error(f'name argument cannot be None, must be string')
    if parent_dir is None or not isinstance(parent_dir, str):
        main_logger.error(f'parent_dir argument cannot be None, must be string')

    fullname = os.path.join(parent_dir, name)
    image = pg.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name: str = None, parent_dir: str = None):
    """
    Attempts to load a sound asset, returns a NoneSound (Sound with empty play method) if it can't
    :param name:
    :param parent_dir:
    :return: pg.mixer.Sound, or NoneSound
    """

    if name is None or not isinstance(name, str):
        main_logger.error(f'name argument cannot be None, must be string')
    if parent_dir is None or not isinstance(name, str):
        main_logger.error(f'parent_dir argument cannot be None, must be string')

    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(parent_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound


""" ====================================================== """
