import logging
import pygame as pg
import os

from pygame import Surface, Rect

from src.utils.utils import check_directories_exist
from config.log_utils import setup_logging
from typing import Tuple, List, Set, Dict

setup_logging(p_logging_config_fp='src/config/logging_config.yaml')
main_logger: logging.Logger = logging.getLogger('main')


class Game:
    # Directories
    main_dir: str
    assets_dir: str

    # Constants
    title: str
    default_screensize: Tuple[int, int] = (1280, 720)

    # Globals
    clock: pg.time.Clock
    screen: pg.Surface
    frame_rate: int
    dt: float

    # States
    playing: bool

    def __init__(self, p_title: str = 'Default Title', p_disp_size: Tuple[int, int] = None, p_frame_rate: int=60):
        main_logger.info(f'Initializing globals and display...')
        pg.init()
        self.clock = pg.time.Clock()
        self.frame_rate = p_frame_rate
        self.dt = self.clock.tick(self.frame_rate) / 1000

        # Checking if necessary directories exist, creating them if not
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.assets_dir = os.path.join(self.main_dir, "assets")
        check_directories_exist([self.main_dir, self.assets_dir])

        # Initializing screen
        screen_size = p_disp_size if p_disp_size is not None else self.default_screensize
        self.screen = pg.display.set_mode(screen_size)
        self.title = p_title
        pg.display.set_caption(p_title)

        # Initializing states
        self.playing = False

    def run(self):
        self.playing = True
        while self.playing:

            # 1. Handle events in queue

            # 2. Update map, sprites

            # 3. Redraw scene, display

            raise NotImplementedError()

    """ ===========  Resource creation functions =========== """

    def load_assets(self) -> None:
        raise NotImplementedError()

    def _load_image(name: str = None, parent_dir: str = None, colorkey=-1, scale: int = 1) -> Tuple[Surface, Rect]:
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

    def _load_sound(name: str = None, parent_dir: str = None):
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

        try:
            fullname = os.path.join(parent_dir, name)
            sound = pg.mixer.Sound(fullname)
        except FileNotFoundError as e:
            main_logger.error(f'File {parent_dir}\\{name} not found: {e}')
            return NoneSound

        return sound

    """ ====================================================== """


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything

    # Create The Background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects

    allsprites = pg.sprite.RenderPlain(_)

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
            pass

        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()


# Game Over

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
