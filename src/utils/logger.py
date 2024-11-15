import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Set up a logger.
    :param name: Logger name
    :param log_file: Log file path
    :param level: Logging level
    """
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
