from datetime import timedelta

import yfinance as yf
import pandas as pd
from urllib.parse import urlparse

from flask import jsonify
from flask_jwt_extended import create_access_token

# Example: FAANG stocks
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]
faang_plus = ["AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "META", "NVDA", "TSLA", "NFLX", "ADBE"]
dow_30 = [
    "AAPL", "MSFT", "JPM", "V", "PG", "UNH", "HD", "INTC", "IBM", "KO",
    "MCD", "MMM", "GS", "AXP", "BA", "CAT", "CVX", "CSCO", "DIS", "JNJ",
    "MRK", "NKE", "PFE", "TRV", "VZ", "WBA", "WMT", "DOW", "HON", "AMGN"
]
top_market_cap = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "BRK-B", "TSLA", "LLY", "JPM",
    "UNH", "V", "JNJ", "WMT", "MA", "AVGO", "PG", "HD", "XOM", "MRK"
]
def get_single_Stock_Data(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    print(f"{ticker}: ${price:.2f}")
    return f"{price}  USD "



def get_stock_data(ticker_list):
    stock_data = {}  # Use a dictionary, not a list
    for symbol in ticker_list:
        try:
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")["Close"].iloc[-1]
            stock_data[symbol] = price  # Store symbol: price pair
        except Exception as e:
            stock_data[symbol] = f"Error: {e}"  # Store error message for the symbol
    return stock_data


def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(url, header=0)
    tickers = table[0]['Symbol'].tolist()
    # Handle Yahoo Finance formatting
    tickers = [ticker.replace('.', '-') for ticker in tickers]
    return tickers

# sp500_tickers = get_sp500_tickers()
#
# print(f"Loaded {len(sp500_tickers)} S&P 500 tickers.")
# get_stock_data(sp500_tickers)



def get_clearbit_logo_from_yfinance(ticker):
    stock = yf.Ticker(ticker)
    website = stock.info.get("website")
    if website:
        domain = urlparse(website).netloc
        return f"https://logo.clearbit.com/{domain}"
    return None

sp500_tickers = get_sp500_tickers()

def get_stock_logo(ticker):
    for logo in tickers:
        print(get_clearbit_logo_from_yfinance(logo))

def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    # Get historical market data (example: last 6 months)
    hist = stock.history(period="6mo", interval="1d")
    pd.set_option('display.max_columns', None)
    return str(hist)
# get_stock_logo(faang_plus)
# hist = ticker.history(period="5d", interval="1h")



# def generate_token(identity: str, expires_hours: int = 1):
#     """
#     Generate a JWT token for the given identity (e.g., username).
#
#     :param identity: The user identity (usually username or user ID).
#     :param expires_hours: Token expiration time in hours.
#     :return: JWT access token string.
#     """
#     return create_access_token(identity=identity, expires_delta=timedelta(hours=expires_hours))
#
#
# print(generate_token("admin"))