import io

from logmia.sh import Sh


def test_basic_print():
    out = 'Nature always wears the colors of the spirit.'
    buf = io.StringIO()
    Sh(stream=buf).echo(out)
    assert '\x1b[22m' + out + '\x1b[0m' == buf.getvalue()


def test_reset_line():
    buf = io.StringIO()
    Sh(stream=buf).reset_line()
    assert buf.getvalue() == '\r\r'
