import logging

# how to create logger object
# how to add python file name in log file
## 2 methods 
## 1. sys (compand line arguments)
## 2. __name__
## 



logging.basicConfig(filename="loggerobj.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s | line no = %(lineno)s")


logger = logging.getLogger(__name__)

logger.info("info message!")
logger.debug("debug message!")