import pandas as pd
import streamlit as st
from libraries import *



st.set_page_config(page_title='Covid Dashboard', page_icon="💉")


countries = ['Australia', 'China','India','Italy', 'Japan', 'USA', 'UK', 'Sri Lanka', 'Spain', 'Brazil']
country_code = {'Australia': 'au', 'China': 'cn', 'India': 'in', 'Italy':'it', 'Japan': 'jp', 'USA': 'us', 'UK': 'gb', 'Sri Lanka': 'lk', 'Spain': 'es', 'Brazil':'br'}

data_types = ['cases', 'deaths', 'recovered']

country = st.sidebar.selectbox('Pick a country', countries)



days = st.sidebar.slider('Pick your days', min_value=1,max_value=90)


data_type = st.sidebar.multiselect('Pick data types', data_types)

st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")


with st.sidebar.expander("About"):
         st.write( "Developed by Dinuja de Silva")

with st.sidebar.expander("Version"):
    st.write("1.0.1")







cases_df = get_historic_cases(country,days)

deaths_df = get_historic_deaths(country,days)

recoveries_df = get_historic_recoveries(country,days)

historic_df = pd.concat([cases_df,deaths_df,recoveries_df],axis=1).astype(int)

daily_cases_df = get_daily_cases(country,days)

daily_deaths_df = get_daily_deaths(country,days)

daily_recoveries_df = get_daily_recoveries(country,days)

daily_df = pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)

yesterday_deaths = get_yesterday_deaths(country)

yesterday_recoveries = get_yesterday_recoveries(country)

st.title('Covid Dashboard')

st.metric('Country', country)

st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

st.metric('Total Cases', yesterday_cases)

st.metric('Total Deaths', yesterday_deaths)

st.metric('Total recovered', yesterday_recoveries)

st.bar_chart(daily_df[data_type])
with st.spinner('Fishing for Data'):
     time.sleep(5)
st.success('Done!')
           




lib_code_contents = '''
import requests
import pandas as pd

def get_historic_cases(country, days):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  cases_df = pd.DataFrame(data=data['timeline']['cases'].values(), 
                    index=data['timeline']['cases'].keys(),
                    columns=['cases'])

  return cases_df

def get_historic_deaths(country, days):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  deaths_df = pd.DataFrame(data=data['timeline']['deaths'].values(), 
                    index=data['timeline']['deaths'].keys(),
                    columns=['deaths'])

  return deaths_df

def get_historic_recoveries(country, days):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  recoveries_df = pd.DataFrame(data=data['timeline']['recovered'].values(), 
                    index=data['timeline']['recovered'].keys(),
                    columns=['recovered'])

  return recoveries_df

def get_yesterday_cases(country):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['cases'].values())[0]

  return count 

def get_yesterday_deaths(country):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['deaths'].values())[0]

  return count 

def get_yesterday_recoveries(country):

  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['recovered'].values())[0]

  return count 

def get_daily_cases(country,days):

    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['cases'].values(), 
                    index=data['timeline']['cases'].keys(),
                    columns=['cases'])
    daily = cumilative.diff().fillna(0)
    return daily 
    
def get_daily_deaths(country,days):

    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['deaths'].values(), 
                    index=data['timeline']['deaths'].keys(),
                    columns=['deaths'])
    daily = cumilative.diff().fillna(0)
    return daily 

def get_daily_recoveries(country,days):

    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['recovered'].values(), 
                    index=data['timeline']['recovered'].keys(),
                    columns=['recovered'])
    daily = cumilative.diff().fillna(0)
    return daily 

'''
st.download_button('Tap to download the library code', lib_code_contents)

application_code_contents = '''
import pandas as pd
import streamlit as st
from libraries import *




st.set_page_config(page_title='Covid Dashboard', page_icon="💉")


countries = ['Australia', 'China','India','Italy', 'Japan', 'USA', 'UK', 'Sri Lanka', 'Spain', 'Brazil']


data_types = ['cases', 'deaths', 'recovered']

country = st.sidebar.selectbox('Pick a country', countries)



days = st.sidebar.slider('Pick your days', min_value=1,max_value=90)


data_type = st.sidebar.multiselect('Pick data types', data_types)

st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")


with st.sidebar.expander("About"):
         st.write( "Developed by Casual Coders")

with st.sidebar.expander("Version"):
    st.write("1.0.1")


cases_df = get_historic_cases(country,days)

deaths_df = get_historic_deaths(country,days)

recoveries_df = get_historic_recoveries(country,days)

historic_df = pd.concat([cases_df,deaths_df,recoveries_df],axis=1).astype(int)

daily_cases_df = get_daily_cases(country,days)

daily_deaths_df = get_daily_deaths(country,days)

daily_recoveries_df = get_daily_recoveries(country,days)

daily_df = pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)

yesterday_deaths = get_yesterday_deaths(country)

yesterday_recoveries = get_yesterday_recoveries(country)

st.title('Covid Dashboard')

st.metric('Country', country)

st.metric('Total Cases', yesterday_cases)

st.metric('Total Deaths', yesterday_deaths)

st.metric('Total recovered', yesterday_recoveries)

st.area_chart(daily_df[data_type])
'''
st.download_button('Tap to download the application code', application_code_contents)

