"""
This module displays a demo. It is meant to showcase the capabilities of this package.
"""
import time

from .logger import get_logger


def demo():
    """Runs our demo. It's meant to be viewed interactively on a terminal."""
    logger = get_logger()
    logger.debug('Here is a debug message')
    time.sleep(1)
    logger.info('This info message overrides the debug message')
    time.sleep(1)
    logger.info('This info message does not override the previous one')
    time.sleep(1)
    logger.debug('This debug message does not override the info message')
    time.sleep(1)
    logger.debug('But this debug message will override the previous debug message')
    time.sleep(1)
    logger.info('This is an info line and ends our demo')


if __name__ == '__main__':
    demo()
