import io

from logmia.logger import LogmiaLogger


def test_logger_debug():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.debug('Something there is that doesn\'t love a wall')
    buf.getvalue() ==  'Something there is that doesn\'t love a wall\r'
