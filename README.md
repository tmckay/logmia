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

### Demo

    $ python -m logmia

### Examples

    import logmia

    logger = logmia.get_logger()

    logger.debug('Attempting to connect to example.com')
    logger.info('Connected to example.com')  # replaces previous debug line and is sticky

## Developing

### Run tests

    $ make test
