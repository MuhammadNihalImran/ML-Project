import os
import sys
import pandas as pd

from src.my_project.logger import logging
from src.my_project.exceptions import CustomException
from src.my_project.utils import read_sql_data

from dataclasses import dataclass

from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(os.path.join("notebook/data", "raw.csv"))

            logging.info("reading completed mysql database")
            # Here you would typically connect to your MySQL database and fetch data
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys) from e
