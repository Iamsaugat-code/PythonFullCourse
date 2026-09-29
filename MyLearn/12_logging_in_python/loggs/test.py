
from myapp import logging

def addition(a,b):
    logging.debug("This is the message for 1 debuggin : ")
    return a+b

logging.debug("This is the second debugging : ")

addition(4,5)