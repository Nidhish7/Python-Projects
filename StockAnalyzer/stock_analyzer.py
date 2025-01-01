# Importing Required Libraries

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Function to get tickers of S&P 500 companies

def get_sp500_tickers():
    tables = pd.read_html(url)
    sp500_table = tables[0]

    tickers = sp500_table['Symbol'].tolist()
    return tickers

# Function to fetch and plot stock data

def fetch_and_plot_stock_data(ticker, start_date, end_date):
    # Fetching stock data from Yahoo Finance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Printing the first few rows of the data to confirm it's correct
    print(stock_data.head())

    # Plot the stock's closing price
    stock_data['Close'].plot(title=f'{ticker} Stock Price', figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.show()


# Function to validate the date format

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# Main Entry point

if __name__ == "__main__":

    tickers = get_sp500_tickers()
    print("Here are some companies that you can search for:")
    print(tickers)

    ticker = input("Please enter the stock ticker symbol (eg: AAPL for Apple, MSFT for Microsoft etc.").upper()

    while True:
        start_date = input("Please enter the start date in YYYY-MM-DD format: ")
        if validate_date(start_date):
            break
        else:
            print("Invalid Date format. Please use the format YYYY-MM-DD")

    while True:
        end_date = input("Please enter the end date in YYYY-MM-DD format: ")
        if validate_date(end_date):
            break
        else:
            print("Invalid Date format. Please use the format YYYY-MM-DD")

    # Call the function to fetch the data and plot the chart
    fetch_and_plot_stock_data(ticker, start_date, end_date)
