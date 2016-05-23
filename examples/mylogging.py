from __future__ import print_function
import sys
import logging

import colorama

class LessThanFilter(logging.Filter):

    def __init__(self, max_level, name=""):
        super(LessThanFilter, self).__init__(name)
        self._max_level = max_level

    def filter(self, record):
        #non-zero return means we log this message
        return record.levelno < self._max_level


class ColoredStream( logging.StreamHandler ):

    """
    colorama constants
    use: colorama.Fore.RED + "some string"
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """

    colors = {
        'DEBUG': colorama.Fore.BLUE + colorama.Style.BRIGHT,
        'INFO': colorama.Style.NORMAL,
        'WARNING': colorama.Fore.YELLOW + colorama.Style.BRIGHT,
        'ERROR': colorama.Fore.RED,
        'CRITICAL': colorama.Fore.RED,
    }

    __init_called = False

    def __init__(self, stream=None, **kw):

        # make sure colorama.init() is called at least once (and once only)
        if not ColoredStream.__init_called:
            ColoredStream.__init_called = True
            colorama.init() # autoreset = True, doesn't appear to work for some reason

        # don't output color to pipes or files
        self._enabled = stream.isatty()

        return super(ColoredStream,self).__init__(stream, **kw)

    def emit(self, record):

        msg = self.format(record)

        if self._enabled:
            try:
                color = ColoredStream.colors[record.levelname]
            except KeyError:
                color = ''

            #print( color + msg + colorama.Style.RESET_ALL, file=self.stream )
            self.stream.write( color + msg + colorama.Style.RESET_ALL + '\n' )
            self.flush()
        else:
            self.stream.write( msg + '\n' )
            self.flush()


def create_logger():
    logger = logging.getLogger() # root logger
    logger.setLevel( logging.NOTSET )

    h1 = ColoredStream( sys.stdout )
    h1.setLevel( logging.INFO )
    h1.set_name( 'stdout' )

    # this handler would otherwise emit current level and higher
    h1.addFilter( LessThanFilter(h1.level+1) )

    h2 = ColoredStream(sys.stderr)
    h2.set_name( 'stderr' )
    h2.setLevel(logging.WARNING)

    logger.addHandler(h1)
    logger.addHandler(h2)

    return logger

logger = create_logger()
