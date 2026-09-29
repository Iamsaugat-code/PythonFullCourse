
import logging

def mod_funcationA():
    logger = logging.getLogger(__name__)
    logger.info("Funcation A is started : ")
    logger.debug("This is the message from the A : ")
    logger.info("Funcation A is completed : ")