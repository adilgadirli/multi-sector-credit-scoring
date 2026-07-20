import unittest
import pandas as pd


def calculate_risk_score(df):
    """Calculates risk score based on DTI, Delinquency, and Collateral Coverage."""
    score = 100

    # Debt-to-Income (DTI) Impact
    if "dti" in df.columns:
        score -= (df["dti"] * 40).fillna(0)

    # Delinquency Impact
    if "delinquency_30d" in df.columns:
        score -= (df["delinquency_30d"] * 15).fillna(0)

    # Collateral Coverage Impact
    if "collateral_coverage" in df.columns:
        score += ((df["collateral_coverage"] - 1.0) * 20).fillna(0)

    return score.clip(0, 100)


def categorize_risk(score):
    """Categorizes score into risk tiers."""
    if score >= 75:
        return "Low Risk"
    elif score >= 50:
        return "Medium Risk"
    else:
        return "High Risk"


class TestCreditScoring(unittest.TestCase):

    def test_low_risk_customer(self):
        data = pd.DataFrame([{
            "dti": 0.20,
            "delinquency_30d": 0,
            "collateral_coverage": 1.2
        }])
        score = calculate_risk_score(data).iloc[0]
        category = categorize_risk(score)

        self.assertGreaterEqual(score, 75)
        self.assertEqual(category, "Low Risk")

    def test_high_risk_customer(self):
        data = pd.DataFrame([{
            "dti": 0.80,
            "delinquency_30d": 3,
            "collateral_coverage": 0.5
        }])
        score = calculate_risk_score(data).iloc[0]
        category = categorize_risk(score)

        self.assertLess(score, 50)
        self.assertEqual(category, "High Risk")

    def test_score_boundaries(self):
        # Extreme negative conditions should clip at 0
        data_bad = pd.DataFrame([{
            "dti": 5.0,
            "delinquency_30d": 10,
            "collateral_coverage": 0.0
        }])
        score_bad = calculate_risk_score(data_bad).iloc[0]
        self.assertEqual(score_bad, 0)


if __name__ == "__main__":
    unittest.main()