import sys
import os

import numpy as np
import pandas as pd

from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.my_project.exceptions import CustomException
from src.my_project.logger import logging
from src.my_project.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """This function is responsible for creating a data transformation pipeline."""
        try:
            numerical_features = ["reading score", "writing score"]
            categorical_features = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            logging.info(f"Numerical Columns: {numerical_features}")
            logging.info(f"Categorical Columns: {categorical_features}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", num_pipeline, numerical_features),
                    ("cat", cat_pipeline, categorical_features),
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            preprocessor_obj = self.get_data_transformer_object()

            target_column = "math score"
            numerical_features = ["reading score", "writing score"]

            ## divide train data into input and target features
            input_features_train = train_df.drop(columns=[target_column], axis=1)
            target_feature_train = train_df[target_column]

            ## divide test data into input and target features
            input_features_test = test_df.drop(columns=[target_column], axis=1)
            target_feature_test = test_df[target_column]

            logging.info(
                "Applying preprocessing object on training and testing dataframes"
            )

            input_features_train_arr = preprocessor_obj.fit_transform(
                input_features_train
            )
            input_features_test_arr = preprocessor_obj.transform(input_features_test)

            train_arr = np.c_[input_features_train_arr, np.array(target_feature_train)]

            test_arr = np.c_[input_features_test_arr, np.array(target_feature_test)]

            logging.info("Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj,
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
