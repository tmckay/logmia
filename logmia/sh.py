import sys


class Sh:
    """Provides a layer on top of normal shell output. This extra
    layer allows for manipulating log output on the shell e.g.
    removing printed output."""
    def __init__(self, stream=sys.stderr):
        self.stream = stream
        self.last_line_width = 0

    def echo(self, chars):
        # Print a line without a trailing newline
        print(chars, file=self.stream, end='', flush=True)
        self.last_line_width = len(chars)

    def _reset_line(self):
        """Replaces current shell output with spaces, so that the line can be overwritten."""
        print('\r' + ' ' * self.last_line_width, file=self.stream, end='', flush=True)

