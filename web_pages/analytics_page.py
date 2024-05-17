import streamlit as st
import pandas as pd
from module.analytics import *


def analytics_page():
    st.title('Analytical Module')
    selected_graph = st.selectbox(
        "Select Graph",
        (
            "City",
            "Region",
            "Bedroom",
            "Bathroom",
            "Floor Category",
            "Building Type",
            "Area",
            "Price",
            "Balcony",
            "TOP usps",
            "Corner Property",
            "Furnish Label"
        )
    )
    
    df = pd.read_csv('web_pages/data.csv')
    
    if selected_graph == "City":
        st.plotly_chart(generate_city_counts(df))
    elif selected_graph == "Region":
        st.plotly_chart(generate_region_counts(df))
    elif selected_graph == "Bedroom":
        st.plotly_chart(generate_bedroom_distribution(df))
    elif selected_graph == "Bathroom":
        st.plotly_chart(generate_bathroom_distribution(df))
    elif selected_graph == "Floor Category":
        st.plotly_chart(generate_floor_category_distribution(df))
    elif selected_graph == "Building Type":
        st.plotly_chart(generate_building_type_distribution(df))
    elif selected_graph == "Area":
        st.plotly_chart(generate_area_distribution_plots(df)[0])
        st.plotly_chart(generate_area_distribution_plots(df)[1])
    elif selected_graph == "Price":
        st.plotly_chart(generate_price_distribution_plots(df)[0])
        st.plotly_chart(generate_price_distribution_plots(df)[1])
    elif selected_graph == "Balcony":
        st.plotly_chart(generate_balcony_counts_plot(df))
    elif selected_graph == "TOP usps":
        st.plotly_chart(generate_top_usps_plot(df))
    elif selected_graph == "Corner Property":
        st.plotly_chart(generate_corner_property_distribution_plot(df))
    elif selected_graph == "Furnish Label":
        st.plotly_chart(generate_furnish_label_distribution_plot(df))
    