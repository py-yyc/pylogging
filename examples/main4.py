#!/usr/bin/env python

from raven import Client

client = Client('http://6d08f903f68345a7847623ec61a524fa:02042b1eddd1492db27892e36e86ec74@localhost:9000/2')

from raven.handlers.logging import SentryHandler
handler = SentryHandler(client)

from raven.conf import setup_logging
setup_logging(handler)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()

import logging
logger = logging.getLogger('main4')

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
