
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt =  '%Y-%m-%d  %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),    # this open a file
        logging.StreamHandler()             # this make the file to write 
        
    ]
)

logger = logging.getLogger("Mathematical operation : ")


def add(a,b):
    logger.debug(f"addition of {a} + {b} = {a+b}")
    return a+b

def mul(a,b):
    logger.debug(f"multiplication of {a} x {b} = {a*b}")
    return a+b

def sub(a,b):
    logger.debug(f"subtraction of {a} - {b} = {a-b}")
    return a+b

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"division of {a} / {b} = {a/b}")
    except Exception :
        logger.error("canot divide by zero : ")

add(2,3)
sub(2,3)
mul(2,3)
divide(2,0)
        