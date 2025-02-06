import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="MSFT", start="2010-01-01", end="2024-01-01"):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start, end=end)
    
    # Keep relevant columns
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df.reset_index(inplace=True)
    
    df.to_csv("data/stock_prices.csv", index=False)
    print(f"Data for {ticker} saved to data/stock_prices.csv")

if __name__ == "__main__":
    fetch_stock_data()
