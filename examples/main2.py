#!/usr/bin/env python

import logging
import logging.config

# older api, does not support filters
logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('main2')

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
