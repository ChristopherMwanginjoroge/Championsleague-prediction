from fastapi import FastAPI
import numpy as np
import tensorflow as tf
import joblib

app=FastAPI()

model=tf.keras.models.load_model("premier_league_points_model.h5")
scaler=joblib.load('scaler.pkl')

features=['W', 'D', 'L', 'GF', 'GA', 'GD']

@app.post("/predict")
def predit(data:dict):
    try:
        X=np.array([[data[f] for f in features]])
        X_scaled=scaler.transform(X)
        prediction=model.predict(X_scaled)

        return{
            "predicted_points":float(prediction[0][0])
        }
    
    except Exception as e:
        return {"error":str(e)}
    
    