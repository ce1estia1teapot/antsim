import logging
import yaml

from typing import Dict


def setup_logging() -> None:
    with open(file='src/config/logging_config.yaml', mode='r') as file:
        try:
            # Setting up using config...
            config: Dict = yaml.safe_load(file)
            logging.config.dictConfig(config)

        except Exception as e:
            logging.root.exception(msg=e)

        logging.root.debug('Logging initialized')


main_logger: logging.Logger = logging.getLogger('main_logger')
