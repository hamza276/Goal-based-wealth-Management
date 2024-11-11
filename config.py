# config.py

risk_level_mapping = {
    "Conservative": {"min_allocation": 0.05, "max_allocation": 0.20, "volatility_target": 0.25},
    "Medium": {"min_allocation": 0.05, "max_allocation": 0.35, "volatility_target": 0.30},
    "Aggressive": {"min_allocation": 0.05, "max_allocation": 0.50, "volatility_target": 0.45}
}

objective_mapping = {
    1: {"description": "Starting a Business", "growth_rate": 0.50, "risk_profile": "Aggressive"},
    2: {"description": "Retirement", "growth_rate": 0.07, "risk_profile": "Medium"},
    3: {"description": "Education", "growth_rate": 0.07, "risk_profile": "Medium"},
    4: {"description": "Wealth Accumulation", "growth_rate": 0.50, "risk_profile": "Aggressive"},
    5: {"description": "Buying a Home", "growth_rate": 0.04, "risk_profile": "Conservative"},
    6: {"description": "Travel", "growth_rate": 0.04, "risk_profile": "Conservative"}
}

time_horizon_mapping = {
    "0-2 years": {"adjustment_factor": 0.75, "risk_profile": "Conservative"},
    "3-7 years": {"adjustment_factor": 1.0, "risk_profile": "Moderate"},
    "8-10 years": {"adjustment_factor": 1.25, "risk_profile": "Aggressive"}
}

investment_constraints = {"min_investment": 5, "max_investment": "No Limit"}
