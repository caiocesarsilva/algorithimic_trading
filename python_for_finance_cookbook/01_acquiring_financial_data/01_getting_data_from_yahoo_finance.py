#Import the libraries
import pandas as pd
import yfinance as yf

#Download the data
df = yf.download("AAPL", 
                 start = "2011-01-01", 
                 end = "2021-12-31", 
                 progress = False)

#Inspect the downloaded data
print(f"Downloaded {len(df)} rows of data.")
print(df)