import logging
import os
import traceback
from logging import handlers


class FRLogger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(FRLogger, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name: str, level: int):
        self.__logger = logging.getLogger(name)
        self.__level = level
        self.__name = name
        self.__logger.setLevel(logging.DEBUG)
        self.__formatter = logging.Formatter("%(asctime)-15s %(levelname)s > %(module)s: %(message)s")

        if not os.path.isdir("./.logs"):
            os.makedirs("./.logs")

        if not any([isinstance(h, handlers.TimedRotatingFileHandler) for h in self.__logger.handlers]):
            file_handler = handlers.TimedRotatingFileHandler(f"./.logs/{self.__name}.log", "MIDNIGHT",
                                                             1, encoding="utf-8")
            file_handler.setFormatter(self.__formatter)
            file_handler.setLevel(logging.DEBUG)
            self.__logger.addHandler(file_handler)

        if not any([isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
                    for h in self.__logger.handlers]):
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.__formatter)
            console_handler.setLevel(self.__level)
            self.__logger.addHandler(console_handler)

    def debug(self, msg: str):
        return self.__logger.debug(msg)

    def error(self, msg: str):
        return self.__logger.error(msg)

    def critical(self, msg: str):
        return self.__logger.critical(msg)

    def exception(self, msg: str):
        return self.__logger.error(msg + f"Exception:\n ***\n{traceback.format_exc()}\n***")

    def warning(self, msg: str):
        return self.__logger.warning(msg)

    def info(self, msg: str):
        return self.__logger.info(msg)


taskr_logger = FRLogger("TaskrApp", "WARN")