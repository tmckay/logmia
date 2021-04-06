import io

from logmia.logger import LogmiaLogger


def test_logger_debug():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.debug('Something there is that doesn\'t love a wall')
    buf.getvalue() ==  'Something there is that doesn\'t love a wall\r'


def test_logger_info():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.info('When the evening is spread out against the sky')
    buf.getvalue() ==  'When the evening is spread out against the sky\n'


def test_logger_debug_then_other():
    for level in ('info', 'warn', 'error'):
        buf = io.StringIO()
        logger = LogmiaLogger(stream=buf)
        logger.debug('Something there is that doesn\'t love a wall')
        getattr(logger, level)('When the evening is spread out against the sky')
        buf.getvalue() ==  '\x1b[22mSomething there is that doesn\'t love a wall\rWhen the evening is spread out against the sky\x1b[0m\n'


def test_logger_colors():
    buf = io.StringIO()
    logger = LogmiaLogger(stream=buf)
    logger.critical('Forgive me they were delicious so sweet and so cold')
    buf.getvalue() ==  '\x1b[22mForgive me they were delicious so sweet and so cold\x1b[0m\n'


