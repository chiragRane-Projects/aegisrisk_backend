import random
import pandas as pd

def generate_synthetic_borrowers(n=1000):

    records = []

    for _ in range(n):

        income = random.randint(25000, 150000)

        existing_debt = random.randint(0, income * 2)

        employment_length = random.randint(0, 20)

        credit_history_years = random.randint(0, 15)

        delinquencies = random.randint(0, 5)

        debt_to_income = existing_debt / max(income, 1)

        income_stability = employment_length / 20

        credit_maturity = credit_history_years / 15

        delinquency_ratio = delinquencies / max(credit_history_years, 1)

        record = {
            "debt_to_income": debt_to_income,
            "income_stability": income_stability,
            "credit_maturity": credit_maturity,
            "delinquency_ratio": delinquency_ratio
        }

        records.append(record)

    df = pd.DataFrame(records)

    return df