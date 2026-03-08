def generate_features(borrower):
    income = borrower["income"]
    debt = borrower["existing_debt"]
    employment_length = borrower["employment_length"]
    credit_history = borrower["credit_history_years"]
    delinquencies = borrower["delinquencies"]
    
    debt_to_income = debt / income
    
    income_stability = employment_length / 10
    
    credit_maturity = credit_history / 10
    
    delinquency_ratio = delinquencies / (credit_history + 1)
    
    features = {
        "debt_to_income": debt_to_income,
        "income_stability": income_stability,
        "credit_maturity": credit_maturity,
        "delinquency_ratio": delinquency_ratio
    }

    return features