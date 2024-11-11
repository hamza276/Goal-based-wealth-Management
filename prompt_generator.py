# prompt_generator.py
def create_llama_prompt(mean_returns, volatility, objective, risk_level, time_horizon, investment_amount):
    prompt = f"""
    You are a financial assistant tasked with optimizing sector weights for a diversified portfolio based on the following historical data.

    Historical Summary Data:
    - Mean Returns: {mean_returns}
    - Volatility: {volatility}
    
    Portfolio Objective: {objective}
    Risk Level: {risk_level}
    Time Horizon: {time_horizon}
    Investment Amount: ${investment_amount}

    Constraints:
    - Minimum allocation per sector: 0%
    - Maximum allocation per sector: 50%
    - The portfolio should have a balance between sectors to achieve the desired objective and risk level.

    **Output the optimized weights in JSON format** with sector names as keys and weights as values. The output should look exactly like this:
    {{
        "Industrials": weights in decimals, # example value
        "Healthcare": weights in decimals,  # example value
        "Technology": weights in decimals,  # example value
        ...
    }}
    Only output the JSON object with no additional text.
    """
    return prompt
