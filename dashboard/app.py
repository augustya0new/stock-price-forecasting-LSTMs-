import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from src.inference import predict_prices, load_model

# Load trained model
MODEL_PATH = "models/trained_model.pth"
model = load_model(MODEL_PATH)

# Streamlit UI
st.title("Stock Price Prediction Dashboard")
st.sidebar.header("User Input")

# Select stock ticker
ticker = st.sidebar.text_input("Enter Stock Symbol (e.g., MSFT)", "MSFT")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch stock data
def fetch_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    return df

st.write(f"Fetching data for {ticker} from {start_date} to {end_date}...")

df = fetch_stock_data(ticker, start_date, end_date)
if df.empty:
    st.warning("No data found! Please try a different date range.")
else:
    # Generate predictions
    df["Prediction"] = predict_prices(model, df)

    # Plot actual vs. predicted
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Close"], label="Actual Price", color="blue")
    plt.plot(df["Date"], df["Prediction"], label="Predicted Price", color="red", linestyle="dashed")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title(f"Stock Price Prediction for {ticker}")
    plt.legend()
    st.pyplot(plt)

    # Display data
    st.write("### Data Preview")
    st.dataframe(df.tail())

st.sidebar.write("Built with ❤️ using Streamlit")
