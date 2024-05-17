import streamlit as st
from module.prediction import *

# Predict page functions
def predict_page():
    st.title('Residential Apartment Price Prediction')

    # Dropdown options
    city_options = ['Ahmedabad West', 'Ahmedabad North', 'Ahmedabad East', 'Gandhinagar', 'Ahmedabad South']
    building_type_options = ['Mid-rise buildings', 'Low-rise buildings', 'High-rise buildings', 'Skyscrapers']
    furnish_label_options = ['Unfurnished', 'Semifurnished', 'Furnished']
    bedroom_num_options = [1, 2, 3, 4]
    bathroom_num_options = [1, 2, 3, 4, 5, 6]
    balcony_num_options = [0, 1, 2, 3, 4]

    # User inputs
    user_input = {
        'CITY': st.selectbox('CITY', city_options),
        'BUILDING_TYPE': st.selectbox('BUILDING_TYPE', building_type_options),
        'FURNISH_LABEL': st.selectbox('FURNISH_LABEL', furnish_label_options),
        'BEDROOM_NUM': st.selectbox('BEDROOM_NUM', bedroom_num_options),
        'BATHROOM_NUM': st.selectbox('BATHROOM_NUM', bathroom_num_options),
        'BALCONY_NUM': st.selectbox('BALCONY_NUM', balcony_num_options),
        'AREA': st.text_input('AREA')
    }

    if st.button('Predict Price', key='Predict Price'):
        input_data = preprocess_input(user_input)
        predicted_price = predict_price(input_data)
        if predicted_price is not None:
            st.success(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
        else:
            st.error("Please fill all the required fields.")
