import logging

log_format = (
    "%(asctime)s [%(levelname)s] - %(name)s - %(funcName)15s:%(lineno)d - %(message)s"
)

file_handler = logging.FileHandler("data/vsm.log")
file_handler.setLevel(logging.INFO)     # для реліза необхідно змінити на ERROR
file_handler.setFormatter(logging.Formatter(log_format))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)   # для дебага потрібно змінити на DEBUG
stream_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger