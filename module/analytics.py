import plotly.graph_objs as go
import plotly.express as px

def generate_city_counts(df):
    city_counts = df['CITY'].value_counts(ascending=True)
    data = [go.Bar(y=city_counts.index, x=city_counts.values, orientation='h', marker=dict(color='mediumseagreen'))]
    layout = go.Layout(title='City Counts', xaxis=dict(title='Count'), yaxis=dict(title='City'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_region_counts(df):
    region_counts = df['LOCALITY'].value_counts(ascending=True)[-10:]
    data = [go.Bar(y=region_counts.index, x=region_counts.values, orientation='h', marker=dict(color='royalblue'))]
    layout = go.Layout(title='Most Frequent Regions: Top 10', xaxis=dict(title='Count'), yaxis=dict(title='Region'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_bedroom_distribution(df):
    bedroom_counts = df['BEDROOM_NUM'].value_counts().sort_index()
    data = [go.Bar(x=bedroom_counts.index.astype(str), y=bedroom_counts.values, marker=dict(color='goldenrod'))]
    layout = go.Layout(title='Number of Bedrooms Distribution', xaxis=dict(title='Number of Bedrooms'), yaxis=dict(title='Count'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_bathroom_distribution(df):
    bathroom_counts = df['BATHROOM_NUM'].value_counts().sort_index()
    data = [go.Bar(x=bathroom_counts.index.astype(str), y=bathroom_counts.values, marker=dict(color='goldenrod'))]
    layout = go.Layout(title='Number of Bathrooms Distribution', xaxis=dict(title='Number of Bathrooms'), yaxis=dict(title='Count'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_floor_category_distribution(df):
    floor_cat_counts = df['FLOOR_CATEGORY'].value_counts(ascending=True)
    data = [go.Bar(y=floor_cat_counts.index, x=floor_cat_counts.values, orientation='h', marker=dict(color='goldenrod'))]
    layout = go.Layout(title='Distribution of Floor Category', xaxis=dict(title='Count'), yaxis=dict(title='Building Type'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_building_type_distribution(df):
    building_type_counts = df['BUILDING_TYPE'].value_counts(ascending=True)
    data = [go.Bar(y=building_type_counts.index, x=building_type_counts.values, orientation='h', marker=dict(color='goldenrod'))]
    layout = go.Layout(title='Distribution of Building Type', xaxis=dict(title='Count'), yaxis=dict(title='Building Type'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_area_distribution_plots(df):
    fig_box = px.box(df, x='AREA', orientation='h', title='Distribution of Area (Boxplot)')
    fig_hist = px.histogram(df, x='AREA', nbins=20, title='Distribution of Area (Histogram)')
    return fig_box, fig_hist

def generate_price_distribution_plots(df):
    fig_box = px.box(df, x='PRICE', orientation='h', title='Distribution of Price (Boxplot)')
    fig_hist = px.histogram(df, x='PRICE', nbins=20, title='Distribution of Price (Histogram)')
    return fig_box, fig_hist
    
def generate_balcony_counts_plot(df):
    balcony_counts = df['BALCONY_NUM'].value_counts(ascending=True)
    data = [go.Bar(y=balcony_counts.index, x=balcony_counts.values, orientation='h', marker=dict(color='mediumseagreen'))]
    layout = go.Layout(title='Balcony Counts', xaxis=dict(title='Count'), yaxis=dict(title='Number of Balcony'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_top_usps_plot(df):
    top_usps_cleaned = df['TOP_USPS'].str.replace(r'[\[\]"\']', '', regex=True).str.split(', ').explode().str.lower()
    top_usps_top_20 = top_usps_cleaned.value_counts(ascending=True)[-20:]
    
    data = [go.Bar(y=top_usps_top_20.index, x=top_usps_top_20.values, orientation='h', marker=dict(color='khaki'))]
    layout = go.Layout(title='Top 20 Most Frequent Amenities/Features', xaxis=dict(title='Frequency'), yaxis=dict(title='Amenity/Feature'))
    fig = go.Figure(data=data, layout=layout)
    return fig

def generate_corner_property_distribution_plot(df):
    corner_property_counts = df['CORNER_PROPERTY'].value_counts()
    labels = ['No', 'Yes']
    sizes = corner_property_counts.values
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, textinfo='label+percent',
                             insidetextorientation='radial', hole=0.3)])
    
    fig.update_traces(hoverinfo='label+percent', textfont_size=12,
                  marker=dict(colors=['goldenrod', 'mediumseagreen'],
                              line=dict(color='#000000', width=2)))
    
    fig.update_layout(title="Distribution of Corner Property")
    
    return fig

def generate_furnish_label_distribution_plot(df):
    furnish_label_counts = df['FURNISH_LABEL'].value_counts()
    labels = ['Unfurnished', 'Furnished', 'Semi-Furnished']
    sizes = furnish_label_counts.values
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, textinfo='label+percent',
                             insidetextorientation='radial', hole=0.3)])
    
    fig.update_traces(hoverinfo='label+percent', textfont_size=12,
                  marker=dict(colors=['goldenrod', 'mediumseagreen', 'royalblue'],
                              line=dict(color='#000000', width=2)))
    
    fig.update_layout(title="Distribution of Furnish Label")
    
    return fig