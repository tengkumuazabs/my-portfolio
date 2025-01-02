import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts 

st.set_page_config(
    page_title = 'Spatial Analysis on COVID-19',
    layout = 'wide'
)

st.title("Spatial Analysis on COVID-19")

df = pd.read_csv(r'data/countries-aggregated.csv')
convert_date = False

if convert_date == False:
    df['Date'] = df.Date.astype('datetime64[ns]')
    df = df.set_index('Date')
    convert_date =True

country = st.selectbox(
    "Select a country",
    (df.Country.unique()),
    index=None,
)

st.write("You selected:", country)

df_country = df[df.Country == country]

# st.write(df_country.Deaths.resample('ME').sum())
st.line_chart(df_country.Deaths.resample('ME').sum(), y='Deaths')

# st.write(df_country)
