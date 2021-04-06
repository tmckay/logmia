import sys

from colorama import Fore, Style


class Sh:
    """Provides a layer on top of normal shell output. This extra
    layer allows for manipulating log output on the shell e.g.
    removing printed output."""
    def __init__(self, stream=sys.stderr):
        self.stream = stream
        self.last_line_width = 0

    def echo(self, chars, color=Style.NORMAL):
        self._print(color + chars + Style.RESET_ALL)
        self.last_line_width = len(chars)

    def _print(self, chars):
        # Print without a trailing newline
        print(chars, file=self.stream, end='', flush=True)

    def reset_line(self):
        """Replaces current shell output with spaces, so that the line can be overwritten."""
        self._print('\r' + ' ' * self.last_line_width + '\r')

    def newline(self):
        print(file=self.stream, flush=True)
