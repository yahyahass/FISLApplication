import pandas as pd
import yfinance as yf
import requests
import pickle
import os
# from sklearn.mixture import GaussianMixture
# from sklearn.preprocessing import StandardScaler


def save_to_cache(data, filename='cache.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_from_cache(filename='cache.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None


def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = requests.get(url).content
    df_list = pd.read_html(html)
    sp500_df = df_list[0]  # Assuming the first table contains S&P 500 data

    tickers = sp500_df['Symbol'].tolist()
    return tickers

def startBuilder():
    # Sourcing S&P 500 tickers from Wikipedia
    tickers = get_sp500_tickers()

    infodict = {}
    nested_dict = {}
    missinginfo = []
    counter = 0
    for i in tickers[:4]:## To remove  
        company = yf.Ticker(i)  #Accessing the Yahoo Finance API
        if not not company.info.keys():
            for a in company.info.keys():
                nested_dict[a] = company.info[a]

            infodict[i] = nested_dict

            nested_dict = {}
        else:
            missinginfo.append(i)
            infodict[i] = ""
        counter += 1
        print(counter)
    df = pd.DataFrame.from_dict(infodict, orient = 'index')
    df.to_csv("full_dataframe.csv")

    



