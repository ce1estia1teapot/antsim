import logging.config
import yaml
import os

from typing import Dict

main_logger: logging.Logger = logging.getLogger(name='main_logger')

def setup_logging(p_logging_config_fp: str = 'src/cfg/logging_config.yaml') -> None:
    """
    This function loads the logging config and initializes loggings with the settings therein.
    :return:
    """

    """ 1. Create logging directory and log file if not already created """
    if not os.path.isdir("logs"):
        os.mkdir('logs')
    if not os.path.isfile('logs/main_log.log'):
        with open('logs/main_log.log', 'x'):
            pass

    global main_logger

    """ 2. Perform initialization of logging """
    with open(file=p_logging_config_fp, mode='r') as file:
        try:
            # Setting up using config...
            config: Dict = yaml.safe_load(file)
            logging.config.dictConfig(config)

        except Exception as e:
            main_logger.exception(msg=e)

        main_logger.debug('Logging initialized')
