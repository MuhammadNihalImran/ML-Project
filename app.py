from src.my_project.logger import logging
from src.my_project.exceptions import CustomException
from src.my_project.components.data_ingestion import DataIngestion

# from src.my_project.utils.dataclass import DataIngestionConfig
from src.my_project.components.data_transformation import (
    DataTransformation,
    DataTransformationConfig,
)

import sys


if __name__ == "__main__":
    logging.info("Application started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys) from e

    logging.info("Application finished")
