import io

from logmia.sh import Sh


def test_basic_print():
    out = 'Nature always wears the colors of the spirit.'
    buf = io.StringIO()
    Sh(stream=buf).echo(out)
    assert out == buf.getvalue()


def test_reset_line():
    buf = io.StringIO()
    Sh(stream=buf)._reset_line()
    assert buf.getvalue() == '\r'
