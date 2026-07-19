# 📊 Multi-Sector Credit Risk Assessment & Automated Scoring Engine

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://multi-sector-credit-scoring.streamlit.app/) | ![Python](https://img.shields.io/badge/Python-3.11+-blue.svg) | ![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B.svg) | ![Basel III Compliant](https://img.shields.io/badge/Framework-Basel%20III-green.svg) | ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An institutional-grade, production-ready credit decision engine built on a **modular, config-driven architecture**. This system simulates automated risk assessment frameworks utilized by international Microfinance Institutions (MFIs) and fintech platforms, aligning with the **Accion Credit Scoring Methodology**.

---

## 🚀 Live Demonstration
🔗 **[Launch Live App](https://multi-sector-credit-scoring.streamlit.app/)**

---

---

## 🛠️ Architectural Philosophy & Core Design Decisions

* **Modular Configuration Qatı (Config-Driven Core):** The entire application is segregated into a modular engine core (`credit_scoring.py`) and a vertical-specific risk parameter layer (`sector_config.py`). Adding a new lending sector (e.g., SME, Agri-loans) takes less than 5 minutes without changing the core computing script.
* **Regulatory Adherence & Explainability (Basel III Compliance):** Unlike black-box machine learning approaches that introduce regulatory friction, this system relies on an additive scorecard matrix approach (Logit transformation mapped to a standard $300 - 850$ credit score range). This guarantees **100% feature interpretability**, fully aligning with Central Bank preferences and Basel guidelines.
* **Dual-Impact Variable Modeling (LTV Dynamics):** In the asset-backed lending module (Lombard/Gold Loans), the Loan-to-Value (LTV) ratio is explicitly modeled as a dual-impact risk factor—simultaneously scaling behavioral default probability ($PD$) while dynamically reducing the post-default recovery efficiency ($LGD$).

---

## 📐 The Risk Mathematics

The application calculates the core banking risk metric, **Expected Loss ($EL$)**, using the standard international baseline formula:

$$EL = PD \times LGD \times EAD$$

Where:
* **$PD$ (Probability of Default):** Extracted via dynamic Logit linear coefficients mapped through a Sigmoid activation function.
* **$LGD$ (Loss Given Default):** Sector-specific. Modeled as a fixed industry average for unsecured loans, a dynamic asset depreciation curve for Auto Leasing, and a strict liquid cash-margin recovery function for Lombard products.
* **$EAD$ (Exposure at Default):** Modeled directly as the requested Loan Amount.

### 💰 Risk-Based Pricing (APR Recommendation)
The model dynamically recommends loan pricing by overlaying a calculated risk premium on top of a standardized base funding rate:

$$\text{Recommended Rate} = \text{Base Rate} + (PD \times \text{Risk Premium Weight})$$

---

## 💼 Vertical-Specific Risk Highlights

| Lending Sector | Risk Proxy Focus | LGD Model |
| :--- | :--- | :--- |
| **MSME** | Cash Flow Sustainability & Alternative Data (Utility Delays) | Unsecured Fixed (45%) |
| **Consumer Loans** | Employment Tenure, Debt Load (DTI), & Credit Bureau History | Unsecured Retail (60%) |
| **Lombard (Gold)** | Collateral Market Value Validation & LTV Margins | Dynamic Recovery Margin |
| **Auto Leasing** | Down Payment Equity Protection & Vehicle Depreciation Curves | Dynamic Asset Degradation Matrix |

---

## 💻 Local Setup & Installation

If you want to run this credit engine locally, clone this repository and follow the setup instructions below:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[adilgadirli]/multi-sector-credit-scoring.git
   cd multi-sector-credit-scoring
   pip install -r requirements.txt
   python -m streamlit run credit_scoring.py
