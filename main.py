import streamlit as st
from web_pages.predict_page import predict_page
from web_pages.recommendation_page import recommendation_page
from web_pages.analytics_page import analytics_page

def main():
    st.sidebar.title('Navigation')    
    selected_option = st.sidebar.radio('Select an option', ('Price Prediction', 'Recommender System', 'Analytics'))

    if selected_option == 'Price Prediction':
        predict_page()
    elif selected_option == 'Recommender System':
        recommendation_page()
    elif selected_option == 'Analytics':
        analytics_page()

        
if __name__ == '__main__':
    main()
