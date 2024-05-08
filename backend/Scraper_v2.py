import pandas as pd
import yfinance as yf
import requests
import pickle
import os
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np


def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = requests.get(url).content
    df_list = pd.read_html(html)
    sp500_df = df_list[0]  # Assuming the first table contains S&P 500 data

    tickers = sp500_df['Symbol'].tolist()
    return tickers


def data_crawling(tickers):

    # Define your cache filename
    cache_filename = 'sp500_data_cache.pkl'

    # Try to load from cache

    if os.path.isfile(cache_filename):
        cached_data = pd.read_pickle(cache_filename)
    else:
        cached_data = None

    ## code v2
    infodict = {}
    nested_dict = {}
    missinginfo = []
    counter = 0
    
    if cached_data is not None:
        # If data is found in cache, use it
        df = cached_data
    else:
        for i in tickers:
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

        df.index.name = 'Ticker'

        df.reset_index(inplace=True)

        df.rename(columns={df.columns[0]: 'Ticker'})

        df.to_csv("full_dataframe.csv")

        df.to_pickle(cache_filename)

    return df


def kmeans_clustering(X_scaled, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X_scaled)
    clusters = kmeans.labels_

    return clusters

def gmm_clustering(X_scaled, n_clusters):
    gmm = GaussianMixture(n_components=n_clusters, random_state=0)
    gmm.fit(X_scaled)

    # Predict the cluster for each ticker
    clusters = gmm.predict(X_scaled)
    return clusters


def clustering(df, co_names, n_clusters, algo = "kmeans"):


    #print("Dataframe : \n", df)



    # Extracting the features for clustering
    extracted_df = df[co_names]

    # Drop rows with nan value 
    cleaned_df = extracted_df.dropna()

    X = cleaned_df.values

    #print("Raw values of Dataframe : \n", X)

    # Standardizing the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    if algo == "gmm":
        clusters = gmm_clustering(X_scaled, n_clusters)
    elif (algo == "kmeans"):
        clusters = kmeans_clustering(X_scaled, n_clusters)


    # Extracting the features for clustering
    df = df[["Ticker"] + co_names]

    # Drop rows with nan value 
    df = df.dropna()

    # Add the cluster information to the original DataFrame
    df['Cluster'] = clusters

    for i in range(n_clusters):
        cluster_members = df[df['Cluster'] == i]['Ticker'].values
        #print(f"Cluster {i}: {', '.join(cluster_members)}")



    modifieddf = df.copy()



##### THIS IS WHAT I ADDED IN - JULIAN ARBELAEZ  #####


    print(df)
    # # Group by Cluster and calculate mean and standard deviation for each column
    numerical_columns = df.select_dtypes(include=[np.number])

    print(numerical_columns)
    cluster_means = numerical_columns.groupby('Cluster').transform('mean')
    print(cluster_means)
    cluster_std = numerical_columns.groupby('Cluster').transform('std')
    print(cluster_std)
    # # Calculate number of standard deviations away from the mean
    normalized_df = (df[co_names] - cluster_means) / cluster_std


    print("normalized_df")
    print(normalized_df)

    # Combine the Ticker and Cluster columns with the normalized values
    normalized_df[['Ticker', 'Cluster']] = df[['Ticker', 'Cluster']]


    # Pop the 'Ticker' column
    ticker_column = normalized_df.pop('Ticker')

    # Insert the 'Ticker' column at the first position
    normalized_df.insert(0, 'Ticker', ticker_column)

    print(normalized_df)


    # Calculate the average per row for columns 1 to 4
    modifieddf['Average'] = normalized_df.iloc[:, 1:-1].mean(axis=1)

    # Find the minimum value in the 'Average' column
    min_average = modifieddf['Average'].min()

    # Shift all 'Average' values to ensure all are positive
    modifieddf['node_size'] = modifieddf['Average'] - min_average


    print(modifieddf)

########

    return modifieddf





# url = "http://127.0.0.1:8080/columns"

# try:
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
#     columns_data = response.json()  # Parse response JSON
#     #print("Columns data:", columns_data)
# except requests.exceptions.RequestException as e:
#     print("Error:", e)



# # Extract values excluding numeric values
# values_list = []
# for item in columns_data['dimensions']:
#     values_list.append(item['dimension_name'])


# print(values_list)


def scraper_run(
    values_list, 
    n_clusters = 10
) -> pd:

    # Sourcing S&P 500 tickers from Wikipedia
    tickers = get_sp500_tickers()

    
    #### Get data from test dataframe


    
    # Get data from yahoo.
    df = data_crawling(tickers)

    # Clustering with args: columns, number of clusters 
    df = clustering(df, values_list, n_clusters)

    # df.to_json("financial_data_2.json", orient = "records")

    return df.to_json(orient = "records")



# print(scraper_run(values_list = ['beta', 'boardRisk', 'debtToEquity']))


