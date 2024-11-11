# data_fetch.py
import yfinance as yf

def fetch_ticker_data(tickers, start="2010-01-01", end="2024-11-01"):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
        # Calculate summary statistics
    returns = data.pct_change().dropna()
    mean_returns = returns.mean().to_dict()
    volatility = returns.std().to_dict()
    cov_matrix = returns.cov().to_dict()
    
    return {"mean_returns": mean_returns, "volatility": volatility, "cov_matrix": cov_matrix}
