from src.my_project.logger import logging
from src.my_project.exceptions import CustomException
from src.my_project.components.data_ingestion import DataIngestion
# from src.my_project.utils.dataclass import DataIngestionConfig

import sys


if __name__ == "__main__":
    logging.info("Application started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Train data saved at: {train_data_path}")
        logging.info(f"Test data saved at: {test_data_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys) from e

    logging.info("Application finished")
