
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

