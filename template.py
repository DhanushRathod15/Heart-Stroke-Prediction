import os
from pathlib import Path

list_of_files = [
    "heart_stroke/cloud_storage/__init__.py",
    "heart_stroke/cloud_storage/aws_storage.py",
    "heart_stroke/components/__init__.py",
    "heart_stroke/components/data_ingestion.py",
    "heart_stroke/components/data_transformation.py",
    "heart_stroke/components/data_validation.py",
    "heart_stroke/components/model_evaluation.py",
    "heart_stroke/components/model_pusher.py",
    "heart_stroke/components/model_trainer.py",
    "heart_stroke/configuration/__init__.py",
    "heart_stroke/configuration/aws_connection.py",
    "heart_stroke/configuration/mongo_db_connection.py",
    "heart_stroke/constant/__init__.py",
    "heart_stroke/constant/training_pipeline/__init__.py",
    "heart_stroke/constant/application.py",
    "heart_stroke/constant/database.py",
    "heart_stroke/constant/env_variables.py",
    "heart_stroke/constant/s3_bucket.py",
    "heart_stroke/data_access/__init__.py",
    "heart_stroke/data_access/heart_stroke_data.py",
    "heart_stroke/entity/__init__.py",
    "heart_stroke/entity/artifact_entity.py",
    "heart_stroke/entity/config_entity.py",
    "heart_stroke/entity/estimator.py",
    "heart_stroke/entity/s3_estimator.py",
    "heart_stroke/exception/__init__.py",
    "heart_stroke/logger/__init__.py",
    "heart_stroke/pipeline/__init__.py",
    "heart_stroke/pipeline/train_pipeline.py",
    "heart_stroke/pipeline/prediction_pipeline.py",
    "heart_stroke/utils/__init__.py",
    "heart_stroke/utils/main_utils.py",
    "heart_stroke/template.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file