# logmia

[![Build Status](https://travis-ci.com/tmckay/logmia.svg?branch=main)](https://travis-ci.com/tmckay/logmia)

## What

Combining less common logging features into a single library.

### Features

 + Collapsing log lines
 + Sticky log lines
 + Opinionated defaults
 + Handlers configured to do the right thing
 + CLI vs. logfile awareness

### Examples

    import logmia

    logger = logmia.get_logger()

    logger.debug('...')
    logger.info('...')  # replaces previous debug line and is sticky
