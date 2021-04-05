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
    for level in ('info', 'warn', 'error', 'critical'):
        buf = io.StringIO()
        logger = LogmiaLogger(stream=buf)
        logger.debug('Something there is that doesn\'t love a wall')
        getattr(logger, level)('When the evening is spread out against the sky')
        buf.getvalue() ==  'Something there is that doesn\'t love a wall\rWhen the evening is spread out against the sky\n'


