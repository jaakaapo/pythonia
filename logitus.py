import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\AapoJaakkola\\python\\logi.log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()
logger.info("Ensimmäinen logiteksti")
logger.error("virhe")
