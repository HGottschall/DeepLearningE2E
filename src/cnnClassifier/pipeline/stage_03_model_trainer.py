from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_trainer import Training
from src.cnnClassifier import logger

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        ...

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed. Error: {e}")
        raise e
