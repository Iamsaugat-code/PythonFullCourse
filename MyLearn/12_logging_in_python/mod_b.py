
import logging


def mod_function_B():
    logger = logging.getLogger(__name__)
    logger.info("Funcation B Started : ")
    logger.debug("This message from the functiona B :  ")
    logger.info("Funcation B is completed :")