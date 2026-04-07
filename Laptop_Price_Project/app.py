import streamlit as st
import pandas as pd
import pickle

with open('laptop_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")
st.title("Laptop Price Prediction Tool")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        brand_name = st.selectbox('Brand', ['Acer', 'Asus', 'Dell', 'HP', 'Lenovo'])
        speed = st.number_input('Processor Speed (GHz)', value=2.5, step=0.1)
        ram = st.number_input('RAM Size (GB)', value=8, step=4)
        storage = st.number_input('Storage Capacity (GB)', value=512, step=128)

    with col2:
        screen = st.number_input('Screen Size (Inches)', value=15.6, step=0.1)
        weight = st.number_input('Weight (kg)', value=1.6, step=0.1)

    submit = st.form_submit_button("Predict Price")

if submit:
    mapping = {'Acer': 0, 'Asus': 1, 'Dell': 2, 'HP': 3, 'Lenovo': 4}
    brand = mapping[brand_name]

    perf_score = speed * ram
    weight_per_inch = weight / screen

    input_df = pd.DataFrame([[
        brand, speed, ram, storage, screen, weight, perf_score, weight_per_inch
    ]], columns=[
        'Brand', 'Processor_Speed', 'RAM_Size', 'Storage_Capacity', 
        'Screen_Size', 'Weight', 'Performance_Score', 'Weight_per_Inch'
    ])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    final_price = float(prediction[0])

    st.success(f"### Estimated Price: ₹ {round(final_price, 2)}")