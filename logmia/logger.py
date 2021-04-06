import logging
import sys

from colorama import Fore

from logmia.sh import Sh


def get_logger():
    return LogmiaLogger()


class LogmiaLogger:

    def __init__(self, stream=sys.stderr):
        self._last_log_type = None
        self._sh = Sh(stream=stream)
    
    def debug(self, msg):
        """Successive debug lines overwrite themselves."""
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg)

    def _non_debug(self, msg):
        """Lines will overwite debug, but will be sticky i.e. won't get overwritten."""
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg)

        self._sh.newline()

    def info(self, msg):
        self._non_debug(msg)

    def warn(self, msg):
        self._non_debug(msg)

    def error(self, msg):
        self._non_debug(msg)

    def critical(self, msg, color=Fore.RED):
        self._non_debug(msg)
