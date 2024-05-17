import streamlit as st
from module.recommendation import *

def display_similar_apartments(similar_apartments):
    st.markdown("<h2 style='text-align: center; color: #0066cc;'>Recommended Similar Apartments</h2>", unsafe_allow_html=True)
    
    for index, row in similar_apartments.iterrows():
        st.markdown(f"<h3 style='color: #009933;'>Description</h3>", unsafe_allow_html=True)
        st.write(row['DESCRIPTION'])
        
        st.markdown(f"<h3 style='color: #009933;'>Location</h3>", unsafe_allow_html=True)
        st.write(f"**City:** {row['CITY']}")
        st.write(f"**Locality:** {row['LOCALITY']}")
        
        st.markdown(f"<h3 style='color: #009933;'>Details</h3>", unsafe_allow_html=True)
        st.write(f"**Bedrooms:** {row['BEDROOM_NUM']}")
        st.write(f"**Bathrooms:** {row['BATHROOM_NUM']}")
        st.write(f"**Balconies:** {row['BALCONY_NUM']}")
        st.write(f"**Floor Category:** {row['FLOOR_CATEGORY']}")
        st.write(f"**Building Type:** {row['BUILDING_TYPE']}")
        st.write(f"**Area:** {row['AREA']:,.2f}sq.ft")
        st.write(f"**Price:** ₹{row['PRICE']}")
        st.write(f"**Furnish Label:** {row['FURNISH_LABEL']}")
        st.markdown(f"**Details URL:** [{row['PROP_DETAILS_URL']}]({row['PROP_DETAILS_URL']})", unsafe_allow_html=True)
        
        st.write("---")
        
def recommendation_page():
    st.title('Residential Apartment Recommender System')
    user_input_url = st.text_input('Enter Property Details URL')
    if st.button('Get Similar Apartments'):
        similar_apartments = recommend_similar_apartments(user_input_url)
        display_similar_apartments(similar_apartments)

