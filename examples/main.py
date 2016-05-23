#!/usr/bin/env python

from mylogging import logger

def enable_debug():
    import logging
    # 'stdout' is the name of a handler defined in .logger
    loggers = filter( lambda h: h.get_name() == 'stdout', logger.handlers )
    loggers[0].setLevel( logging.DEBUG )

logger.debug("debug message")
enable_debug()
logger.debug("debug message")

logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
