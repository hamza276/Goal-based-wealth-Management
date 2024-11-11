# main.py
import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

# Define sector tickers and corresponding industries directly using tickers as keys
sector_tickers = {
    "XLI": "Industrials",
    "XLV": "Healthcare",
    "XLK": "Technology",
    "XLRE": "Real Estate",
    "XLB": "Basic Materials",
    "XLF": "Financials",
    "XLU": "Utilities",
    "XLY": "Consumer Cyclicals",
    "XLP": "Consumer Non-Cyclicals",
    "XLE": "Energy"
}

# Risk level preferences
risk_level_mapping = {
    "Conservative": {"volatility_weight": 0.7, "return_weight": 0.3},
    "Moderate": {"volatility_weight": 0.5, "return_weight": 0.5},
    "Aggressive": {"volatility_weight": 0.3, "return_weight": 0.7}
}

# Time horizon adjustments (example settings, you can customize further)
time_horizon_mapping = {
    "Short (0-2 years)": {"volatility_adjustment": 1.0, "return_adjustment": 0.8},
    "Medium (3-7 years)": {"volatility_adjustment": 0.9, "return_adjustment": 1.0},
    "Long (8-10 years)": {"volatility_adjustment": 0.8, "return_adjustment": 1.2}
}

# Streamlit interface for user input
st.title("Top 4 Sectors Selection Based on Returns, Risk, and Time Horizon")
st.sidebar.header("Portfolio Parameters")

# User input for risk level
risk_levels = list(risk_level_mapping.keys())
selected_risk_level = st.sidebar.selectbox("Select Risk Level", risk_levels)

# User input for time horizon
time_horizons = list(time_horizon_mapping.keys())
selected_time_horizon = st.sidebar.selectbox("Select Time Horizon", time_horizons)

# Fetch data
def fetch_data(tickers):
    data = yf.download(list(tickers.keys()), start="2020-01-01", end="2023-01-01")['Adj Close']
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    volatility = returns.std()
    cov_matrix = returns.cov()
    return mean_returns, volatility, cov_matrix

mean_returns, volatility, cov_matrix = fetch_data(sector_tickers)

# Calculate score based on return, volatility, risk, and time horizon adjustments
def calculate_scores(mean_returns, volatility, risk_params, horizon_params):
    scores = {}
    for ticker in mean_returns.index:
        # Adjusted risk and return weights based on time horizon
        adjusted_return_weight = risk_params["return_weight"] * horizon_params["return_adjustment"]
        adjusted_volatility_weight = risk_params["volatility_weight"] * horizon_params["volatility_adjustment"]
        
        # Risk-adjusted score
        score = (adjusted_return_weight * mean_returns[ticker] - adjusted_volatility_weight * volatility[ticker])
        scores[ticker] = score
    return scores

# Get the top 4 sectors based on the scores
risk_params = risk_level_mapping[selected_risk_level]
horizon_params = time_horizon_mapping[selected_time_horizon]
sector_scores = calculate_scores(mean_returns, volatility, risk_params, horizon_params)
top_4_sectors = sorted(sector_scores, key=sector_scores.get, reverse=True)[:4]

# Calculate weights based on normalized scores
total_score = sum(sector_scores[ticker] for ticker in top_4_sectors)
weights = {ticker: sector_scores[ticker] / total_score for ticker in top_4_sectors}

# Display results
st.subheader(f"Top 4 Sectors for {selected_risk_level} Risk Level and {selected_time_horizon} Time Horizon")
top_sectors_df = pd.DataFrame({
    "Industry": [sector_tickers.get(ticker, "Unknown Industry") for ticker in top_4_sectors],
    "Ticker": top_4_sectors,
    "Weight": [weights[ticker] for ticker in top_4_sectors],
    "Score": [sector_scores[ticker] for ticker in top_4_sectors],
    "Return": [mean_returns[ticker] for ticker in top_4_sectors],
    "Volatility": [volatility[ticker] for ticker in top_4_sectors]
})

# Display DataFrame with calculated weights
st.write(top_sectors_df)

# Visualize weights in a bar chart
st.bar_chart(top_sectors_df.set_index("Industry")["Weight"])
