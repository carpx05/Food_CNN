from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    roboflow_api_key = os.getenv("ROBOFLOW_API_KEY")
    roboflow_workspace = os.getenv("ROBOFLOW_WORKSPACE")
    roboflow_project = os.getenv("ROBOFLOW_PROJECT")
    dataset_version = os.getenv("DATASET_VERSION")
