import os
import joblib
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_name):

    # get project root (where main.py is)
    base_path = os.getcwd()

    if model_name == "XGBoost":
        model_path = os.path.join(base_path, "models", "xgb_model.pkl")
        print("Loading from:", model_path)
        return joblib.load(model_path)
