from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        ...

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed. Error: {e}")
        raise e
