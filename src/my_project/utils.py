import os
import sys
import pandas as pd
import numpy as np

import pymysql
import pickle

from src.my_project.logger import logging
from src.my_project.exceptions import CustomException

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading data from MySQL database")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, database=db)
        logging.info("Connected to MySQL database successfully", mydb)

        df = pd.read_sql_query("SELECT * FROM Students", mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e, sys) from e


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Object saved successfully")
    except Exception as e:
        raise CustomException(e, sys) from e
