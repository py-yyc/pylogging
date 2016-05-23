#!/usr/bin/env python

import sys
import logging

from mylogging import ColoredStream

def logconf( project_name, debug ):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'thread_verbose': {
                'format': '%(levelname)-5s %(asctime)s %(name)s:%(lineno)d %(process)d %(thread)d: %(message)s'
            },
            'verbose': {
                'format': '%(levelname)-5s %(asctime)s %(name)s:%(lineno)d: %(message)s'
            },
            'simple': {
                'format': '%(levelname)-5s %(name)s:%(lineno)d: %(message)s',
            },
        },
        'filters': {
        },
        'handlers': {
            'null': {
                'class':'logging.NullHandler',
            },
            'stderr':{
                'level': 'WARNING',
                'formatter': 'verbose',
                'class': 'mylogging.ColoredStream',
                'stream': 'ext://sys.stderr'
            },
            'stdout':{
                'level': 'DEBUG',
                'formatter': 'simple',
                'class': 'mylogging.ColoredStream',
                'stream': 'ext://sys.stdout'
            },
            'logfile': {
                'level': 'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': '%s.log' % project_name,
                'mode': 'w',
                'maxBytes': 1000,
                'backupCount': 2,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            '': { # root
                'handlers': ['logfile'],
                'level': 'DEBUG' if debug else 'INFO',
            },
            project_name: {
                'handlers': ['stdout','stderr'],
                'propagate': True,
                'level': 'DEBUG' if debug else 'INFO',
            },
        },
    }

import logging.config
logging.config.dictConfig( logconf('main3', True) )

# create logger
logger = logging.getLogger('main3')

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
