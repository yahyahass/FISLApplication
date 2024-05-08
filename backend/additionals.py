import pandas as pd


df = pd.read_json('financial_data_2.json')
print(df)


# Group by Cluster and calculate mean and standard deviation for each column
cluster_means = df.groupby('Cluster').transform('mean')
# print(cluster_means)
cluster_std = df.groupby('Cluster').transform('std')
# print(cluster_std)
# Calculate number of standard deviations away from the mean
normalized_df = (df[['revenuePerShare', 'revenueGrowth', 'regularMarketVolume', 'marketCap']] - cluster_means) / cluster_std

# Combine the Ticker and Cluster columns with the normalized values
normalized_df[['Ticker', 'Cluster']] = df[['Ticker', 'Cluster']]


# Pop the 'Ticker' column
ticker_column = normalized_df.pop('Ticker')

# Insert the 'Ticker' column at the first position
normalized_df.insert(0, 'Ticker', ticker_column)



# Print the DataFrame showing the number of standard deviations away from the mean
# print(normalized_df)


# Calculate the average per row for columns 1 to 4
normalized_df['Average'] = normalized_df.iloc[:, 1:5].mean(axis=1)

# Print the DataFrame with the new 'Average' column
print(normalized_df)