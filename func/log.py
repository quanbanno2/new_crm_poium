import logging


def logFun(msg, level='info'):
    logger = logging.getLogger()
    logger.setLevel('INFO')

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    if level == 'info':
        return logger.info(msg)
    elif level == 'error':
        return logger.error(msg)
