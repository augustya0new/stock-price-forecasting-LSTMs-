# Use official Python image
FROM python:3.9
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY src src
COPY dashboard dashboard
COPY models models

# Run Streamlit
CMD ["streamlit", "run", "dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
