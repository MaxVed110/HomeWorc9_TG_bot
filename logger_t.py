import logging


logger = logging.getLogger('Telephone_dictionary')
logger.setLevel(logging.DEBUG)
log_save = logging.FileHandler('logger.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_save.setFormatter(formatter)
logger.addHandler(log_save)


def logger_cls():
    with open('logger.log', 'w'):
        pass
