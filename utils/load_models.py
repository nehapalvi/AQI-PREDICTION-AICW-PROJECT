import joblib
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_name):

    if model_name == "XGBoost":
        return joblib.load("models/xgb_model.pkl")

    elif model_name == "LSTM":
        return keras_load_model("models/lstm_model.keras")