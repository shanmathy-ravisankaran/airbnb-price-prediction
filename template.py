import os
from pathlib import Path

package_name = "Airbnb"

list_of_files = [
    ".github/workflows/main.yaml",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/Data_ingestion.py",
    f"src/{package_name}/components/Data_transformation.py",
    f"src/{package_name}/components/Model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/Training_pipeline.py",
    f"src/{package_name}/pipelines/Prediction_Pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/utils.py",
    "Notebook_Experiments/Airbnb_Price_Prediction.ipynb",
    "Notebook_Experiments/Exploratory_Data_Analysis.ipynb",
    "templates/index.html",
    "static/style.css",
    ".gitignore",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md",
    "Dockerfile"
]

