import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.inference import load_model, predict_prices

class Backtest:
    def __init__(self, initial_cash=10000, transaction_fee=0.001):
        """
        Initialize backtesting parameters.
        :param initial_cash: Starting cash balance.
        :param transaction_fee: Fee per transaction (e.g., 0.1% per trade).
        """
        self.cash = initial_cash
        self.shares = 0
        self.transaction_fee = transaction_fee
        self.trade_log = []
    
    def simulate_trading(self, data):
        """
        Run backtesting simulation.
        :param data: DataFrame with stock prices & predictions.
        """
        for i in range(1, len(data)):
            prev_price = data.iloc[i - 1]["Close"]
            curr_price = data.iloc[i]["Close"]
            signal = data.iloc[i]["Prediction"]

            # Buy Signal
            if signal == 1 and self.cash > 0:
                self.shares = self.cash / (curr_price * (1 + self.transaction_fee))
                self.cash = 0
                self.trade_log.append((data.index[i], "BUY", curr_price))
            
            # Sell Signal
            elif signal == -1 and self.shares > 0:
                self.cash = self.shares * curr_price * (1 - self.transaction_fee)
                self.shares = 0
                self.trade_log.append((data.index[i], "SELL", curr_price))

        # Final Portfolio Value
        final_value = self.cash + (self.shares * data.iloc[-1]["Close"])
        return final_value

    def backtest(self, df):
        """
        Execute the backtest and compare with buy-and-hold strategy.
        """
        df["Strategy_Return"] = df["Prediction"].shift(1) * df["Close"].pct_change()
        df["Cumulative_Strategy_Return"] = (1 + df["Strategy_Return"]).cumprod()
        df["Cumulative_Buy_Hold"] = (1 + df["Close"].pct_change()).cumprod()

        self.plot_results(df)
        return df

    def plot_results(self, df):
        """
        Visualize strategy performance.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df["Cumulative_Strategy_Return"], label="Trading Strategy", color="blue")
        plt.plot(df.index, df["Cumulative_Buy_Hold"], label="Buy & Hold", color="red", linestyle="dashed")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return")
        plt.legend()
        plt.title("Backtesting Results: Trading Strategy vs. Buy & Hold")
        plt.show()
