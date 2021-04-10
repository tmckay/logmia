"""
Wraps printing to the shell so that it's possible to easily override previous lines.
"""
import sys
from typing import IO

from colorama import Style


class Sh:
    """Provides a layer on top of normal shell output. This extra
    layer allows for manipulating log output on the shell e.g.
    removing printed output."""

    MOVE_CURSOR_UP = '\033[F'
    CARRIAGE_RETURN = '\r'

    def __init__(self, stream: IO[str] = sys.stderr):
        """Can override the stream, usually for testing."""
        self.stream = stream
        self._prev_line_width = 0
        self._last_line_width = 0

    def echo(self, chars: str, color: str = Style.NORMAL):
        """Print characters to the shell."""
        self._print(color + chars + Style.RESET_ALL)
        self._prev_line_width = self._last_line_width
        self._last_line_width = len(chars)

    def _print(self, chars: str):
        """Print line to shell without a newline."""
        print(chars, file=self.stream, end='', flush=True)

    def reset_line(self):
        """Replaces current shell output with spaces, so that the line can be overwritten."""
        self._print(self.CARRIAGE_RETURN)
        self._print(' ' * self._last_line_width)
        self._print(self.CARRIAGE_RETURN)

    def reset_prev_line(self):
        """Replaces previous line my moving the cursor up."""
        self._print(self.MOVE_CURSOR_UP)
        self._print(self.MOVE_CURSOR_UP)
        self._print(' ' * self._prev_line_width)

    def newline(self):
        """Print a newline."""
        print(file=self.stream, flush=True)
