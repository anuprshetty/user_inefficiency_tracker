import logging
from pathlib import Path
import os
import data


def generate_log(log_folder_name):
    print("\nLog Information : ")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    log_folder_absolute_path = Path(os.getcwd()) / log_folder_name
    if not os.path.exists(log_folder_absolute_path):
        os.mkdir(log_folder_absolute_path)
    log_file_name = data.workflow_name + ".log"
    log_file_absolute_path = Path(log_folder_absolute_path) / log_file_name
    print("Log file Absolute Path : ", log_file_absolute_path)
    with open(log_file_absolute_path, "w") as LOG_FILE:
        LOG_FILE.write(
            "DATE TIME,LOG LEVEL NAME,USER ID,CURRENT STEP,NEXT STEP,STEP TIME\n"
        )
    formatter = logging.Formatter(
        "%(asctime)s,%(levelname)s,%(message)s", datefmt="%d-%m-%Y %H-%M-%S"
    )
    file_logger = logging.FileHandler(filename=log_file_absolute_path)
    file_logger.setFormatter(formatter)
    logger.addHandler(file_logger)
    console_logger = logging.StreamHandler()
    logger.addHandler(console_logger)
    return logger


logger_obj = generate_log(log_folder_name="logs")
