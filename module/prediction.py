import numpy as np
import pickle

# Function to load the trained model
def load_model():
    with open('module/model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

# Function to preprocess user input
def preprocess_input(user_input):
    input_data = np.array([
        user_input['CITY'],
        user_input['BUILDING_TYPE'],
        user_input['FURNISH_LABEL'],
        user_input['BEDROOM_NUM'],
        user_input['BATHROOM_NUM'],
        user_input['BALCONY_NUM'],
        user_input['AREA']]
    ).reshape(1, -1)
    return input_data

# Function to predict price
def predict_price(input_data, key='predict'):
    loaded_model = load_model()
    predicted_price = loaded_model.predict(input_data)
    return predicted_price