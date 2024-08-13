import logging
import os

from typing import List

main_logger: logging.Logger = logging.getLogger('main')


def check_directories_exist(p_directories: List[str]) -> None:
    for directory in p_directories:
        try:
            os.makedirs(directory)
            main_logger.debug(f'Creating directory: {directory}')
        except OSError:
            main_logger.warning(f'Error creating directory - Directory already exists: {directory}')
