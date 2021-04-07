import io

from logmia.logger import LogmiaLogger


def test_logger_debug():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.debug('Something there is that doesn\'t love a wall')
    assert buf.getvalue() ==  '\x1b[22mSomething there is that doesn\'t love a wall\x1b[0m'


def test_logger_info():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.info('When the evening is spread out against the sky')
    assert buf.getvalue() ==  '\x1b[22mWhen the evening is spread out against the sky\x1b[0m\n'


def test_logger_debug_then_other():
    for level in ('info', 'warn', 'error'):
        buf = io.StringIO()
        logger = LogmiaLogger(stream=buf)
        logger.debug('Something there is that doesn\'t love a wall')
        getattr(logger, level)('When the evening is spread out against the sky')
        assert buf.getvalue() == (
            '\x1b[22mSomething there is that doesn\'t love a wall\x1b[0m\r'
            '                                           '
	    '\r\x1b[22mWhen the evening is spread out against the sky\x1b[0m\n'
        )


def test_logger_colors():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.critical('Forgive me they were delicious so sweet and so cold')
    assert buf.getvalue() ==  '\x1b[31mForgive me they were delicious so sweet and so cold\x1b[0m\n'
