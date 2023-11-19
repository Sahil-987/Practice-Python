import logging


logging.basicConfig(filename="basic_logging_logfile.log",
                    level=logging.DEBUG,
                    filemode='w',
                    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s | line no = %(lineno)s") # how the message is printing on the log file


# levels
logging.debug("this is a debug message")
logging.info("this is info message")
logging.warning("the warning is displayed here")
logging.error("the error message is displayed here")
logging.critical("the critical message is displayed here")