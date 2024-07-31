import os
from heart_stroke.constant.s3_bucket import TRAINING_BUCKET_NAME

TARGET_COLUMN = "stroke"
PIPELINE_NAME: str = "heart_stroke"
ARTIFACT_DIR: str = "artifact"

# common file name

FILE_NAME: str = "heart_stroke.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")