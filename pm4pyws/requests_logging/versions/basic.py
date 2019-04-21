import logging
from pm4pyws.requests_logging.interface.logginghandler import LoggingHandler


class BasicLoggingHandler(LoggingHandler):
    def __init__(self):
        """
        Create a basic logging handler
        """
        logging.basicConfig(
            filename='pm4pyws.log',
            level=logging.INFO,
            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )

        LoggingHandler.__init__(self)

    def log_exception_method(self, method_name, exception_str, request=None):
        """
        Log an exception happening inside a method

        Parameters
        ------------
        method_name
            Name of the method
        exception_str
            String describing the exception
        request
            (If provided) Flask HTTP request content
        """
        pass

    def debug(self, msg):
        """
        Logs a debug message

        Parameters
        -----------
        msg
            Message
        """
        logging.debug(msg)

    def info(self, msg):
        """
        Logs an info message

        Parameters
        ------------
        msg
            Message
        """
        logging.info(msg)

    def warning(self, msg):
        """
        Logs a warning message

        Parameters
        ------------
        msg
            Message
        """
        logging.warning(msg)

    def error(self, msg):
        """
        Logs an error message

        Parameters
        ------------
        msg
            Message
        """
        logging.error(msg)
