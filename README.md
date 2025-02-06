# Stock Price Forecasting with Transformer-Based Models

##  **Project Overview**
This project aims to **predict stock prices** using **Transformer-based models (LSTMs, TCNs, and ARIMA)** and compare their performance. The project involves **data preprocessing, feature engineering, model training, evaluation, and deployment as an API** using **FastAPI**. The system is containerized with **Docker** and supports CI/CD integration for seamless deployment.

## **Key Features**
- ✅ **Time Series Data Collection**: Fetches stock price data from Yahoo Finance.
- ✅ **Exploratory Data Analysis (EDA)**: Visualizes stock trends, seasonality, and volatility.
- ✅ **Feature Engineering**: Creates time-based features for improved forecasting.
- ✅ **Machine Learning Models**: Implements **Transformer, LSTM, ARIMA, and SARIMA** models.
- ✅ **Model Evaluation**: Compares models using **RMSE, MAPE, and MAE**.
- ✅ **FastAPI Deployment**: Provides a REST API for real-time predictions.
- ✅ **Dockerization**: Containerized environment for seamless execution.
- ✅ **Automated Testing & CI/CD**: GitHub Actions ensures reliable deployments.

---

## 📂 **Project Structure**
```
📂 stock-price-forecasting
│── 📜 README.md               <- Project overview, setup guide, API docs
│── 📜 requirements.txt        <- Dependencies for environment setup
│── 📜 .gitignore              <- Ignore unnecessary files (logs, data dumps)
│── 📂 data
│   ├── stock_prices.csv       <- Raw dataset (MSFT stock from Yahoo Finance)
│   ├── preprocessed.csv       <- Processed dataset
│── 📂 notebooks
│   ├── exploratory_analysis.ipynb  <- EDA, feature engineering
│   ├── model_training.ipynb        <- Model training, comparison
│   ├── prediction_visualization.ipynb <- Forecasting visualization
│── 📂 src
│   ├── config.py              <- Configuration settings (tickers, lookback period, etc.)
│   ├── data_loader.py         <- Fetch & preprocess stock data
│   ├── feature_engineering.py <- Creating features for time series modeling
│   ├── models.py              <- Transformer, LSTM, ARIMA, SARIMA models
│   ├── train.py               <- Training script for all models
│   ├── evaluate.py            <- Metrics comparison
│   ├── inference.py           <- Load trained models & make predictions
│   ├── main.py                <- FastAPI stock price prediction API
│── 📂 docker
│   ├── Dockerfile             <- Docker setup for API deployment
│   ├── docker-compose.yml     <- Container orchestration
│── 📂 tests
│   ├── test_data_loader.py    <- Unit tests for data fetching
│   ├── test_models.py         <- Unit tests for trained models
│── 📂 docs
│   ├── API_DOCS.md            <- API documentation with usage examples
│   ├── architecture.png       <- System design diagram
│── 📂 .github
│   ├── workflows
│       ├── ci_cd.yml          <- GitHub Actions for CI/CD
```

---

##  **Dataset**
- 📌 **Source**: [Yahoo Finance API](https://finance.yahoo.com/)
- 📌 **Data Includes**:
  - `Date`: Trading date.
  - `Open`, `High`, `Low`, `Close`: Stock prices.
  - `Volume`: Number of shares traded.

### 🔹 **Fetch Data**
```bash
python src/data_loader.py
```

---

## 🏗 **Installation & Setup**
### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/augustya0new/stock-price-forecasting-LSTMs-.git
cd stock-price-forecasting-LSTMs-
```

### 🔹 **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Run Exploratory Data Analysis (EDA)**
```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

### 🔹 **4. Train the Model**
```bash
python src/train.py
```

---

## 🚀 **Running the API Locally**
1️⃣ **Start FastAPI**
```bash
uvicorn src.main:app --reload
```

2️⃣ **Test API (Using cURL)**
```bash
curl -X POST "http://127.0.0.1:8000/predict"
```

---

## 📡 **Docker Deployment**
### 🔹 **1. Build Docker Image**
```bash
docker build -t stock-price-api .
```

### 🔹 **2. Run the Container**
```bash
docker run -p 8000:8000 stock-price-api
```

### 🔹 **3. Run with Docker Compose**
```bash
docker-compose up --build
```

---

## ✅ **Unit Testing & CI/CD**
Run unit tests before deployment.
```bash
pytest tests/
```

**CI/CD Pipeline (GitHub Actions)**
- Defined in `.github/workflows/ci_cd.yml`.
- Runs tests automatically on push.

---

## 📈 **Future Improvements**
- **Deploy on AWS/GCP** using Kubernetes.
- **Optimize ML model with hyperparameter tuning**.
- **Enhance Explainability using SHAP values**.
- **Integrate Stock News Sentiment Analysis**.

---

## ✨ **Contributions & Support**
- **Contributions**: Open a PR or issue.
- **License**: MIT License.
- **Contact**: kumaraugustya1@gmail.com | augustya0new

---
🚀 **Happy forecasting!** 🔥

