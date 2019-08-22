"""rpi_clock_weather:: A tkinter clock and weather reporting on the tens."""

import logging
import logging.handlers

__author__ = 'The Author'
__version__ = 'v0.0.1'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s:%(lineno)-8d %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("rpi_clock_weather")
syslog_handler = logging.handlers.SysLogHandler()
logger.addHandler(syslog_handler)

