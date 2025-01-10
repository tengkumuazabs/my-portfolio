import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts 
from st_keyup import st_keyup
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap
import os

st.set_page_config(
    page_title = 'Spatial Analysis on COVID-19',
    layout = 'wide'
)

# st.session_state.interval

if 'interval_confirmed' not in st.session_state:
    st.session_state.interval_confirmed = 'Daily'
    st.session_state.interval_deaths = 'Daily'
    st.session_state.interval_map = '500,000'
    st.session_state.country = 'Worldwide'

st.title('Spatial Analysis on  :red[COVID-19]')

data_dir = os.path.join(os.path.dirname(__file__), 'data')
df = pd.read_csv(os.path.join(data_dir, 'countries-aggregated.csv'))

worldwide_grouped = df.groupby('Date').sum()
worldwide_grouped['Country'] = 'Worldwide'
df = pd.concat([worldwide_grouped.reset_index(), df])

convert_date = False
if convert_date == False:
    df['Date'] = df.Date.astype('datetime64[ns]')
    df = df.set_index('Date')
    convert_date =True

# visualization start

st.markdown('Data valid as **April 2022**')
st.markdown("\n\n")
st.markdown("\n\n")

country_max = df.groupby('Country').max().reset_index().sort_values('Deaths', ascending=False)
country_max['Ratio'] = (country_max['Deaths'] / country_max['Confirmed'] * 100).round(2)

# import geopy
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent='app')

# lat, lon = [], []

# for country in country_max.Country.unique():
#     print(country)
#     location = geolocator.geocode(country)
#     lat.append(location.latitude)
#     lon.append(location.longitude)

# df = pd.DataFrame({
#     'Country': country_max.Country.unique(),
#     'Latitude': lat,
#     'Longitude': lon
# })

coordinates = pd.read_csv(os.path.join(data_dir, 'country_coordinates.csv'))
country_max['Latitude'], country_max['Longitude'] = coordinates.Latitude, coordinates.Longitude

col1, col2 = st.columns([1,3], border=True)

with col1:
    col1.metric("Total Cases Worldwide", "{:,}".format(df[df.Country == 'Worldwide'].Confirmed.max()))
    st.markdown("\n\n")
    col1.metric("\nHighest Cases in", country_max.iloc[1:2].Country.values[0] + ' ◦ ' + "{:,}".format(country_max.iloc[1:2].Confirmed.values[0]))
    st.markdown("---")
    col1.metric("Deaths Worldwide", "{:,}".format(df[df.Country == 'Worldwide'].Deaths.max()))
    st.markdown("\n\n")
    col1.metric("Highest Deaths in", country_max.iloc[1:2].Country.values[0] + ' ◦ ' + "{:,}".format(country_max.iloc[1:2].Deaths.values[0]))

with col2:
    options = ['25,000', '100,000', '500,000']
    selection = st.pills("Deaths Around the World More Than...", options, key='interval_map')

    selection = int(selection.replace(',', ''))

    def plot_map(interval):
        # st.markdown('**Deaths Around the World** (> ' + str("{:,}".format(interval)) + ' deaths)')
        st.map(country_max[(country_max.Country != 'Worldwide') & (country_max.Deaths >= interval)], 
            latitude='Latitude', longitude='Longitude', size='Deaths', zoom=1, height=350)
    
    plot_map(selection)

col1, col2, col3 = st.columns([2,2,2], border=True)

with col1:
    value = st_keyup("Country", key="0", placeholder='Enter country name...')

    if value:
        country_max_filtered = country_max[country_max.Country.str.lower().str.contains(value.lower())]

    else:
        country_max_filtered = country_max

    with st.container(height=270, border=False):
        col1x1, col1x2 = st.columns([2, 1])
    
        for country, deaths in zip(country_max_filtered.Country, country_max_filtered.Deaths):
            with col1x1:
                if st.button(country, use_container_width=True, type="secondary", key=country):
                    st.session_state.country = country
    
            with col1x2:
                st.button('**'+str(f'{deaths:,}'  )+'**', key=country+'count', disabled=True, type="tertiary", use_container_width=True)
    
    if st.session_state.country != '':
        st.markdown('\n')  
        st.error('Selected country: **' + st.session_state.country + '**')

with col2:
    if st.session_state.country == '':
        st.error('Please select a country', icon='⚠️')  
    
    else:
        df_country = []
        df_country = df[df.Country == st.session_state.country]
        
        fig = px.line(df_country, y=['Confirmed', 'Deaths'], color_discrete_sequence=["#262730", "red"], title='Confirmed Cases and Deaths Timeline')
        fig.update_layout(legend=dict(
            orientation="h"
        ), xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), yaxis_title=None, xaxis_title=None, legend_title=None) 
        fig.update_xaxes(rangeslider_visible=False)
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.add_scatter(x = [fig.data[0].x[-1]], y = [fig.data[0].y[-1]],
                            mode = 'markers + text',
                            marker = {'color':'#262730', 'size':5},
                            showlegend = False,
                            text = [f"{fig.data[0].y[-1]:,}"],
                            textposition='top left')
        fig.add_scatter(x = [fig.data[1].x[-1]], y = [fig.data[1].y[-1]],
                            mode = 'markers + text',
                            marker = {'color':'red', 'size':10},
                            showlegend = False,
                            text = [f"{fig.data[1].y[-1]:,}"],
                            textposition='top left')
        
        st.plotly_chart(fig, config= dict(
            displayModeBar = False)
        )

with col3:
    if st.session_state.country == '':
        st.error('Please select a country', icon='⚠️')  
    
    else:
        total_confirmed = df_country['Confirmed'].max()
        total_deaths = df_country['Deaths'].max()

        pie = px.pie(values=[total_confirmed, total_deaths], names=['Confirmed', 'Deaths'], 
                     color_discrete_sequence=["#262730", "red"], title='Fatality Ratio')
        pie.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-5,
            xanchor="center",
            x=0.5
        ))

        st.plotly_chart(pie, config= dict(
            displayModeBar = False)
        )

with st.container(border=True):

    if st.session_state.country != '':
        df = df[df.Country == st.session_state.country]
        df['Resample Confirmed'] = df['Confirmed'].diff().fillna(0).astype(int)
        df['Resample Recovered'] = df['Recovered'].diff().fillna(0).astype(int)
        df['Resample Deaths'] = df['Deaths'].diff().fillna(0).astype(int)

        tab1, tab2 = st.tabs(["Confirmed", "Deaths"])

        def plot_interval(interval, col, color):
            df_resample = df.resample(interval)[col].sum()

            fig = px.bar(df_resample, y=col, 
                        color_discrete_sequence=color)
            
            fig.update_layout(legend=dict(
                orientation="h"
            ), xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), yaxis_title=None, xaxis_title=None, legend_title=None) 
            fig.update_xaxes(rangeslider_visible=False)

            st.plotly_chart(fig, config= dict(
                displayModeBar = False)
            )

        with tab1:
            options = ["Daily", "Monthly", "Yearly"]
            selection = st.pills("Time Interval", options, key='interval_confirmed')

            if selection == 'Daily':
                plot_interval('D', 'Resample Confirmed', ["#262730"])

            elif selection == 'Monthly':
                plot_interval('ME', 'Resample Confirmed', ["#262730"])
            
            elif selection == 'Yearly':
                plot_interval('YE', 'Resample Confirmed', ["#262730"])

        with tab2:
            selection = st.pills("Time Interval", options, key='interval_deaths')

            if selection == 'Daily':
                plot_interval('D', 'Resample Deaths', ["red"])

            elif selection == 'Monthly':
                plot_interval('ME', 'Resample Deaths', ["red"])
            
            elif selection == 'Yearly':
                plot_interval('YE', 'Resample Deaths', ["red"])
    
    else:
        st.error('Please select a country', icon='⚠️') 

