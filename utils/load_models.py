import pickle
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_name):

    if model_name == "XGBoost":
        return pickle.load(open("models/xgb_model.pkl", "rb"))

    elif model_name == "Random Forest":
        return pickle.load(open("models/rf_model.pkl", "rb"))

    elif model_name == "LSTM":
        return keras_load_model("models/lstm_model.keras")