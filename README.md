# Sector Allocation Portfolio Optimization

This is a **Streamlit-based sector allocation tool** that enables users to determine optimal portfolio allocations across different market sectors based on selected **risk levels** and **time horizons**. Using **historical stock data** from Yahoo Finance, the app organizes sectors into three distinct categories, each containing four sectors with tailored weights, to help align investment preferences with specific risk tolerances and investment durations.

## Features

- **User-Defined Risk Levels**: Choose from Conservative, Moderate, and Aggressive risk levels, each applying different weightings to returns and volatility.
- **Time Horizon Customization**: Select between Short (0-2 years), Medium (3-7 years), and Long (8-10 years) investment horizons to adjust the impact of returns and volatility on sector scores.
- **Real-Time Data Fetching**: Retrieves historical adjusted closing prices from Yahoo Finance, computing average returns and volatility for each sector.
- **Category-Based Sector Allocation**: Divides sectors into three categories of four sectors each, ranked and weighted by calculated scores based on the selected risk profile and time horizon.
- **Interactive Visualizations**: Displays sector weights in intuitive tables and bar charts for each category, facilitating comparisons across sectors.

## Scoring Methodology

1. **Score Calculation**: For each sector, a score is computed based on historical returns and volatility, adjusted for the selected risk level and time horizon.
2. **Sorting and Allocation**: Sectors are sorted by score, and the top twelve sectors are divided into three categories of four sectors each.
3. **Weight Normalization**: Within each category, sector weights are normalized to sum to 1, allowing clear insights into allocation distribution.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hamza276/Sector-Weight-Allocation.git
   ```

2. **Install Requirements**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Requirements include:
   - `streamlit`
   - `yfinance`
   - `numpy`
   - `pandas`

4. **Run the App**:
   Start the Streamlit app with:
   ```bash
   streamlit run main.py
   ```


## Project Structure
 ```
sector-allocation-portfolio-optimization/
│
├── config.py               # Configuration settings (e.g., API keys)
├── data_fetch.py           # Functions to fetch data from Yahoo Finance
├── llama_client.py         # Interfacing with Llama model for sector weight optimization
├── main.py                 # Main Streamlit app file
├── prompt_generator.py     # Script to generate prompts for Llama model
├── requirements.txt        # Required Python packages
└── README.md               # Project README
 ```

## Future Improvements

- **Additional Risk Metrics**: Add risk-adjusted metrics such as the Sharpe ratio to enhance score calculations.
- **Sector Customization**: Allow users to select or deselect specific sectors for analysis.
- **Backtesting Capability**: Implement backtesting features to evaluate portfolio performance based on historical data.




