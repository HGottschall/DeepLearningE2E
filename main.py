from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed. Error: {e}")
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed. Error: {e}")
    raise e