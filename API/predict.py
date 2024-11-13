import pandas as pd
import joblib
from Preprocessing import DataProcessor

def predictions(input_data):
    model = joblib.load('API\\xgboost_model.joblib')
    
    preprocessor = DataProcessor()
    preprocessed_data = preprocessor.preprocess(input_data)
    prediction = model.predict(preprocessed_data)
    return {"prediction": f"{float(prediction[0]):.2f} €"}

    

    
