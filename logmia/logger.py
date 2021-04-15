"""
Provides log classes. Should use factory function get_logger.
"""

import logging
import sys
from typing import IO

from colorama import Fore, Style

from logmia.sh import Sh


def get_logger() -> 'LogmiaLogger':
    """Factory for instantiating a logger."""
    return LogmiaLogger()


class LogmiaLogger:
    """Provides all basic log levels."""

    def __init__(self, stream: IO[str] = sys.stderr):
        self._last_log_type = 0
        self._sh = Sh(stream=stream)

    def debug(self, msg: str):
        """Successive debug lines overwrite themselves."""
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg)

        self._last_log_type = logging.DEBUG

    def _non_debug(self, msg: str, color: str = Style.NORMAL):
        """Lines will overwite debug, but will be sticky i.e. won't get overwritten."""
        if self._last_log_type == logging.DEBUG:
            self._sh.reset_line()

        self._sh.echo(msg, color=color)

        self._sh.newline()

    def info(self, msg: str):
        """Replaces debug lines but is sticky."""
        self._non_debug(msg)

        self._last_log_type = logging.INFO

    def warn(self, msg: str):
        """Replaces debug lines but is sticky."""
        self._non_debug(msg)

        self._last_log_type = logging.WARN

    def error(self, msg: str):
        """Replaces debug lines but is sticky."""
        self._non_debug(msg)

        self._last_log_type = logging.ERROR

    def critical(self, msg: str):
        """Replaces debug lines but is sticky."""
        self._non_debug(msg, color=Fore.RED)

        self._last_log_type = logging.CRITICAL


class LogmiaStreamHandler(logging.StreamHandler):
    """Makes a log handler compatible with the standard library's logging module."""

    def __init__(self, stream=None):
        super().__init__(stream)
        self._sh = Sh(stream)

    def emit(self, record: logging.LogRecord):
        """Writes record to the stream."""

        msg = self.format(record)
        self._sh.echo(msg)
