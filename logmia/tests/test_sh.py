import io

from logmia.sh import Sh


def test_basic_print():
    out = 'Nature always wears the colors of the spirit.'
    buf = io.StringIO()
    Sh(stream=buf)).print(out)
    assert out == buf.getvalue()
