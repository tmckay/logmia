import sys


class Sh:
    """Provides a layer on top of normal shell output. This extra
    layer allows for manipulating log output on the shell e.g.
    removing printed output."""
    def __init__(self, stream=sys.stderr):
        self.stream = stream

    def echo(self, chars):
        print(chars, file=self.stream)
