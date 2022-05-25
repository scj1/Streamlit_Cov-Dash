import pandas as pd
import streamlit as st
from libraries import *



st.set_page_config(page_title='Covid Dashboard', page_icon="💉")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
   .sidebar .sidebar-content {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)





countries = ['Australia', 'China','India','Italy', 'Japan', 'USA', 'UK', 'Sri Lanka', 'Spain', 'Brazil']
country_code = {'Australia': 'au', 'China': 'cn', 'India': 'in', 'Italy':'it', 'Japan': 'jp', 'USA': 'us', 'UK': 'gb', 'Sri Lanka': 'lk', 'Spain': 'es', 'Brazil':'br'}

data_types = ['cases', 'deaths', 'recovered']

country = st.sidebar.selectbox('Pick a country', countries)



days = st.sidebar.slider('Choose your number days', min_value=1,max_value=90)


data_type = st.sidebar.multiselect('Pick your  data types', data_types)

st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")


with st.sidebar.expander("About"):
         st.write( "Developed by Casual Coders of Meu Labs ")

with st.sidebar.expander("Version"):
    st.write("2.1.5")







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

st.title('🧫Covid Dashboard💉')

col1, col2 = st.columns(2)
column1, column2, column3 = st.columns(3)
col1.metric(label='Country', value=country)
col2.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")
column1.metric('Total Cases', yesterday_cases)
column2.metric('Total Deaths', yesterday_deaths)
column3.metric('Total recovered', yesterday_recoveries)



st.info('You must pick Data types and the number of Days you want to see!')

st.line_chart(daily_df[data_type])

st.video('https://www.youtube.com/watch?v=oqFn6AHoJZQ')

st.warning('Please wear a Mask and Stay Safe!')

st.subheader("Thank You for using our Covid Dashboard")



st.info('Below buttons are to download these codes')
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

st.write("You can change font with below radio")
t = st.radio("Change font!", [True, False])

if t:
    st.markdown(
        """
        <style>
@font-face {
  font-family: 'Tangerine';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap" rel="stylesheet;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

    html, body, [class*="css"]  {
    font-family: 'Monsterrat';
    font-size: 48px;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )
