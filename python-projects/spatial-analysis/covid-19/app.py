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

# add_diff = False
# if add_diff == False:
    # df['Daily Confirmed'] = df['Confirmed'].diff().fillna(0).astype(int)
    # df['Daily Recovered'] = df['Recovered'].diff().fillna(0).astype(int)
    # df['Daily Deaths'] = df['Deaths'].diff().fillna(0).astype(int)

# df['Ratio'] = (df['Deaths'] / df['Confirmed'] * 100).round(2)

# visualization start

st.markdown('Data valid as **April 2022**')
st.markdown("\n\n")
st.markdown("\n\n")

# st.markdown("---")

country_max = df.groupby('Country').max().reset_index().sort_values('Deaths', ascending=False)
country_max['Ratio'] = (country_max['Deaths'] / country_max['Confirmed'] * 100).round(2)
# country_max = country_max.sort_values('Country')

# st.write(df)

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

coordinates = pd.read_csv(os.path.join(data_dir, 'country_coordinates.csv'))
country_max['Latitude'], country_max['Longitude'] = coordinates.Latitude, coordinates.Longitude

# st.write(country_max)

# with col1:
#     st.header("{:,}".format(df[df.Country == 'Worldwide'].Confirmed.max()))
#     st.markdown('Confirmed Cases')

# with col2:
#     st.header("{:,}".format(df[df.Country == 'Worldwide'].Deaths.max()))
#     st.markdown('Deaths')

# with col3:
#     st.header(country_max.iloc[1:2].Country.values[0])
#     st.markdown('Country with Highest Confirmed Cases')
#     st.markdown(":red[**{:,}".format(country_max.iloc[1:2].Confirmed.values[0]) + '**]')

# with col4:
#     st.header(country_max.iloc[1:2].Country.values[0])
#     st.markdown('Country with Highest Deaths')
#     st.markdown(":red[**{:,}".format(country_max.iloc[1:2].Deaths.values[0]) + '**]')

# st.markdown('\n')    
# st.markdown('\n')

col1, col2 = st.columns([1,3], border=True)

with col1:
    col1.metric("Total Cases Worldwide", "{:,}".format(df[df.Country == 'Worldwide'].Confirmed.max()))
    st.markdown("\n\n")
    col1.metric("\nHighest Cases in", country_max.iloc[1:2].Country.values[0] + ' ◦ ' + "{:,}".format(country_max.iloc[1:2].Confirmed.values[0]))
    # st.markdown("\n\n")
    st.markdown("---")
    col1.metric("Deaths Worldwide", "{:,}".format(df[df.Country == 'Worldwide'].Deaths.max()))
    st.markdown("\n\n")
    col1.metric("Highest Deaths in", country_max.iloc[1:2].Country.values[0] + ' ◦ ' + "{:,}".format(country_max.iloc[1:2].Deaths.values[0]))

with col2:
# with st.container(height=400):
    st.markdown('**Deaths Around the World** (> 50,000 deaths)')
    st.map(country_max[(country_max.Country != 'Worldwide') & (country_max.Deaths >= 50000)], 
           latitude='Latitude', longitude='Longitude', 
           size='Deaths', zoom=1, height=400)

    # st.write(country_max)
    # m = folium.Map(location=[0,0], zoom_start=2, tiles="CartoDB dark_matter")
    
    # death_heatmap = country_max[country_max.Country != 'Worldwide'][['Latitude', 'Longitude', 'Confirmed']].values.tolist()
    # HeatMap(death_heatmap).add_to(m)  

    # st_data = st_folium(m, width=1350, height=370) 

col1, col2, col3 = st.columns([2,2,2], border=True)
country_button = ''

# st.write(country_max.isna().sum())

with col1:
    
    # country_max = df.groupby('Country').max().reset_index().sort_values('Confirmed', ascending=False)
    value = st_keyup("Country", key="0", placeholder='Enter country name...')

    if value:
        country_max_filtered = country_max[country_max.Country.str.lower().str.contains(value.lower())]

    else:
        country_max_filtered = country_max

    with st.container(height=270, border=False):
        col1x1, col1x2 = st.columns([2, 1])
    
        for country, deaths in zip(country_max_filtered.Country, country_max_filtered.Deaths):
            with col1x1:
                if st.button(country, use_container_width=True, type="secondary"):
                    country_button = country
    
            with col1x2:
                st.button('**'+str(f'{deaths:,}'  )+'**', key=country, disabled=True, type="tertiary", use_container_width=True)
    
    if country_button != '':
        st.markdown('\n')  
        st.error('Selected country: **' + country_button + '**')

with col2:
    if country_button == '':
        st.error('Please select a country', icon='⚠️')  
    
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
        st.error('Please select a country', icon='⚠️')  
    
    else:
        # st.write(df_country)
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

# col1 = st.columns(1, border=True)

with st.container(border=True):
    if country_button != '':
        df = df[df.Country == country_button]
        df['Daily Confirmed'] = df['Confirmed'].diff().fillna(0).astype(int)
        df['Daily Recovered'] = df['Recovered'].diff().fillna(0).astype(int)
        df['Daily Deaths'] = df['Deaths'].diff().fillna(0).astype(int)
        # st.bar_chart(data=df[df.Country == country_button], y='Daily Confirmed')

        tab1, tab2 = st.tabs(["Confirmed", "Deaths"])

        with tab1:
            fig = px.bar(df[df.Country == country_button], y='Daily Confirmed', 
                        color_discrete_sequence=["#262730"], title='Daily Confirmed')
            
            fig.update_layout(legend=dict(
                orientation="h"
            ), xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), yaxis_title=None, xaxis_title=None, legend_title=None) 
            fig.update_xaxes(rangeslider_visible=False)

            st.plotly_chart(fig, config= dict(
                displayModeBar = False)
            )

        with tab2:
            fig = px.bar(df[df.Country == country_button], y='Daily Deaths', 
                        color_discrete_sequence=["red"], title='Daily Deaths')
            
            fig.update_layout(legend=dict(
                orientation="h"
            ), xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), yaxis_title=None, xaxis_title=None, legend_title=None) 
            fig.update_xaxes(rangeslider_visible=False)

            st.plotly_chart(fig, config= dict(
                displayModeBar = False)
            )
    
    else:
        st.error('Please select a country', icon='⚠️') 