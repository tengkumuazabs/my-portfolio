import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts 
from st_keyup import st_keyup

st.set_page_config(
    page_title = 'Spatial Analysis on COVID-19',
    layout = 'wide'
)

st.title('Spatial Analysis on  :red[COVID-19]')

df = pd.read_csv(r'data/countries-aggregated.csv')

worldwide_grouped = df.groupby('Date').sum()
worldwide_grouped['Country'] = 'Worldwide'
df = pd.concat([worldwide_grouped.reset_index(), df])

convert_date = False
if convert_date == False:
    df['Date'] = df.Date.astype('datetime64[ns]')
    df = df.set_index('Date')
    convert_date =True

# df['Ratio'] = (df['Deaths'] / df['Confirmed'] * 100).round(2)

# visualization start

st.error('Data valid as **April 2022**')

country_max = df.groupby('Country').max().reset_index().sort_values('Confirmed', ascending=False)
country_max['Ratio'] = (country_max['Deaths'] / country_max['Confirmed'] * 100).round(2)
# country_max = country_max.sort_values('Country')


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

# df.to_csv('country_coordinates.csv', index=False)

coordinates = pd.read_csv('data/country_coordinates.csv')
country_max['Latitude'], country_max['Longitude'] = coordinates.Latitude, coordinates.Longitude

# st.write(country_max)

col1, col2, col3, col4 = st.columns(4, border=False)
col1.metric("Total Cases", "{:,}".format(df[df.Country == 'Worldwide'].Confirmed.max()))
col2.metric("Highest Cases in", country_max.iloc[1:2].Country.values[0] + ': ' + "{:,}".format(country_max.iloc[1:2].Confirmed.values[0]))
col3.metric("Deaths", "{:,}".format(df[df.Country == 'Worldwide'].Deaths.max()))
col4.metric("Highest Deaths in", country_max.iloc[1:2].Country.values[0] + ': ' + "{:,}".format(country_max.iloc[1:2].Deaths.values[0]))

with st.container(height=400):
    st.markdown('**Deaths Around the World**')
    st.map(country_max[country_max.Country != 'Worldwide'], latitude='Latitude', longitude='Longitude', size='Deaths', zoom=1)

col1, col2, col3 = st.columns([2,2,2], border=True)
country_button = ''

with col1:
    
    # country_max = df.groupby('Country').max().reset_index().sort_values('Confirmed', ascending=False)
    value = st_keyup("Country", key="0")

    if value:
        country_max_filtered = country_max[country_max.Country.str.lower().str.contains(value.lower())]

    else:
        country_max_filtered = country_max

    with st.container(height=320, border=False):
        col1x1, col1x2 = st.columns([2, 1])
    
        for country, confirmed in zip(country_max_filtered.Country, country_max_filtered.Confirmed):
            with col1x1:
                if st.button(country, use_container_width=True, type="secondary"):
                    country_button = country
    
            with col1x2:
                st.button('**'+str(f'{confirmed:,}'  )+'**', disabled=True, type="tertiary", use_container_width=True)

with col2:
    if country_button == '':
        st.error('Please select a country')  
    
    else:
        df_country = []
        df_country = df[df.Country == country_button]
        
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
    if country_button == '':
        st.error('Please select a country')  
    
    else:
        # st.write(df_country)
        total_confirmed = df_country['Confirmed'].max()
        total_deaths = df_country['Deaths'].max()

        pie = px.pie(values=[total_confirmed, total_deaths], names=['Confirmed', 'Deaths'], 
                     color_discrete_sequence=["#262730", "red"], title='Fatality Ratio')
        pie.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        st.plotly_chart(pie, config= dict(
            displayModeBar = False)
        )

