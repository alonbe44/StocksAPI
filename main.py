import yfinance as yf
import pandas as pd
from urllib.parse import urlparse

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

def get_stock_data(ticker_list):
    for symbol in ticker_list:
        try:
            stock = yf.Ticker(symbol)
            print("website = "+stock.info.get("website"))  # e.g., 'https://www.apple.com/'
            price = stock.history(period="1d")["Close"].iloc[-1]
            print(f"{symbol}: ${price:.2f}")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

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



print(get_clearbit_logo_from_yfinance("AAPL"))