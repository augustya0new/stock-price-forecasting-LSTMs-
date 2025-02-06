import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_features(df):
    df["year"] = pd.to_datetime(df["Date"]).dt.year
    df["month"] = pd.to_datetime(df["Date"]).dt.month
    df["day"] = pd.to_datetime(df["Date"]).dt.day
    df["weekday"] = pd.to_datetime(df["Date"]).dt.weekday
    return df

def scale_features(df):
    scaler = StandardScaler()
    df[["Open", "High", "Low", "Close", "Volume"]] = scaler.fit_transform(df[["Open", "High", "Low", "Close", "Volume"]])
    return df
