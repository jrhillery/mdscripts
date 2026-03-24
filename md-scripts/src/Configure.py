
from logging.config import dictConfig

from java.lang import System


class Configure(object):
    @staticmethod
    def logToSysErr():
        # type: () -> None
        """Configure logging to System.err"""
        dictConfig({
            "version": 1,
            "formatters": {
                "simple": {
                    "format": "%(asctime)s.%(msecs)03d %(message)s",
                    "datefmt": "%H:%M:%S"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "simple",
                    "stream": System.err
                }
            },
            "root": {
                "level": "DEBUG",
                "handlers": ["console"]
            }
        })

# end class Configure
