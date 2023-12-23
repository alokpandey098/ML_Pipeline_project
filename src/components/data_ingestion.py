import numpy as np
import pandas as pd
import os, sys
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts","train.csv")
    test_data_path = os.path.join("artifacts","test.csv")
    raw_data_path = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started...")
        try:
            logging.info("Data reading starting...")
            data = pd.read_csv(os.path.join("notebook/data","incom_data.csv"))

            logging.info("Data saving in raw file started...")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Data saving in raw file completed...")

            logging.info("Train test data splitting stage started")
            train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False,header = True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False,header = True)
            logging.info("Data splitting in train test completed successfully")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
               
        except Exception as e:
            logging.info("Error occured in data ingestion stage")
            raise CustmeException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()