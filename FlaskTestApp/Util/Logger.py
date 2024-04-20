import inspect
import logging
import os

from FlaskTestApp.Util.Read_INI_File import read_config_ini


def getLogger():
    # Create the logs directory if it doesn't exist
    logs_dir = read_config_ini()['Logs']['logs_dir']
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler(os.path.join(logs_dir, 'logfile.log'))
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger
