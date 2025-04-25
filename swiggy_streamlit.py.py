# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 08:41:28 2025

@author: sayan
"""

import numpy as np 
import pandas as pd
import pickle
import streamlit as st
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, KNNImputer, MissingIndicator
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder, MinMaxScaler, PowerTransformer, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,root_mean_squared_error
import pickle

load_model= pickle.load(open(r'C:\Users\sayan\Documents\PythonML\swiggy_model_pipe2.sav','rb'))


def main():
    st.set_page_config(page_title="Swiggy Delivery Time Predictor", layout="centered")
    st.title("🚴 Swiggy Delivery Time Predictor")
    st.markdown("""Enter the details  of the order to predict how long it will take to be delivered.""")

    age = st.slider("Delivery Person Age", 18, 55, 30)
    ratings = st.slider("Delivery Person Ratings", 1.0, 5.0, 4.5, 0.1)
    weather = st.selectbox("Weather Conditions", ['Sunny', 'Stormy', 'Sandstorms', 'Cloudy', 'Fog','Windy'])
    traffic = st.selectbox("Road Traffic Density", ['low', 'medium', 'high', 'jam'])
    vehicle_condition = st.slider("Vehicle Condition (0 = Poor, 2 = Excellent)", 0, 2, 1)
    type_of_order = st.selectbox("Type of Order", ['snack', 'meal', 'drinks', 'buffet'])
    type_of_vehicle = st.selectbox("Type of Vehicle", ['scooter', 'motorcycle', 'electric_scooter'])
    multiple_deliveries = st.slider("Multiple Deliveries",0,2 , step=1)
    festival = st.selectbox("Festival", ['Yes ', 'No '])
    city = st.selectbox("City", ['urban', 'semi-Urban', 'metropolitan'])
    pickup_time = st.slider("Pickup Time", 5,15,step=5)
    order_time_of_day = st.selectbox("Order Time of Day", ['Morning', 'Afternoon', 'Evening', 'Night'])
    is_weekend = st.text_input("Is it Weekend?")
    distance = st.slider("Distance (km)", 0.5, 50.0, step=0.1)
    distance_type = st.selectbox("Distance Type", ['short', 'medium', 'long','very long'])

    if st.button("Predict Delivery Time"):
        input_data = pd.DataFrame({
        'Delivery_person_Age': [age],
        'Delivery_person_Ratings': [ratings],
        'Weatherconditions': [weather],
        'Road_traffic_density': [traffic],
        'Vehicle_condition': [vehicle_condition],
        'Type_of_order': [type_of_order],
        'Type_of_vehicle': [type_of_vehicle],
        'multiple_deliveries': [multiple_deliveries],
        'Festival': [festival],
        'City': [city],
        'pickup_time': [pickup_time.strftime('%H:%M:%S')],
        'order_time_of_day': [order_time_of_day],
        'is_weekend': [is_weekend],
        'Distance': [distance],
        'distance_type': [distance_type]
    })

    prediction = load_model.predict(input_data)[0]
    st.success(f"Estimated Delivery Time: {round(prediction, 2)} minutes")
    
    
    
    
if __name__ == '__main__':
    main()
