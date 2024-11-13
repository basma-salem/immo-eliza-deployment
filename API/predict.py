import pandas as pd
import joblib
from API.Preprocessing import DataProcessor

def predictions(input_data):
    model = joblib.load('API\\xgboost_model.joblib')
    
    preprocessor = DataProcessor()
    preprocessed_data = preprocessor.preprocess(input_data)
    prediction = model.predict(preprocessed_data)
    return {"prediction": float(prediction[0])}

    

    