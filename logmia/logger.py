import logging
import sys

from logmia.sh import Sh


def get_logger():
    return LogmiaLogger()


class LogmiaLogger:

    def __init__(self, stream=sys.stderr):
        self._last_log_type = None
        self._sh = Sh(stream=stream)
    
    def debug(self, msg):
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg)
