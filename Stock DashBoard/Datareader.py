import pandas_datareader.data as web

from datetime import datetime

start = datetime(2016, 9, 1)

end = datetime(2018, 9, 1)


#the api key is found in Account setting of yours in https://www.quandl.com/  -> you crewated an account and have an api key they give it to you.,
df = web.DataReader("EURONEXT/FP", "quandl", start, end,api_key="bsFBSfJyyHzpcsZrjrBa")

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL'] #'MSFT', '^GSPC'
# We would like all available data from 01/01/2017 until 12/31/2017.
start_date = '2017-01-01'
end_date = '2017-12-31'
df2 = web.DataReader(tickers, data_source='yahoo', start=start_date, end=end_date)

print(df.head())
print('\n')
print(df2.head())