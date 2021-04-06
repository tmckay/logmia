import logging
import sys

from colorama import Fore, Style

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

        self._last_log_type = logging.DEBUG

    def _non_debug(self, msg, color=Style.NORMAL):
        """Lines will overwite debug, but will be sticky i.e. won't get overwritten."""
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg, color=color)

        self._sh.newline()

    def info(self, msg):
        self._non_debug(msg)

        self._last_log_type = logging.INFO

    def warn(self, msg):
        self._non_debug(msg)

        self._last_log_type = logging.WARN

    def error(self, msg):
        self._non_debug(msg)

        self._last_log_type = logging.ERROR

    def critical(self, msg):
        self._non_debug(msg, color=Fore.RED)

        self._last_log_type = logging.CRITICAL
