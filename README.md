# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Human traders often fall victim to emotional decision-making, leading to poor trade execution and avoidable losses. By automating trading strategies, we can eliminate emotional bias and ensure disciplined adherence to predefined rules.

This project aims to develop a Python-based trading bot using IBridgePy to execute strategies with precision, minimizing human error. Success will be measured by backtesting strategies against the SPY ETF benchmark—if a strategy outperforms SPY, the project is deemed successful.

## Stakeholder & User
Primary Stakeholder & User: Myself (academic & potential end-user)
Deliverables:
Performance metrics (profit/loss)
Visualizations of strategy returns over time

## Useful Answer & Decision
The project will identify historically profitable strategies through backtesting. While past performance does not guarantee future success, these strategies serve as predictive models.
Deliverables Include:
Quantitative performance metrics
Comparative performance charts

## Assumptions & Constraints
Assumptions:
Historical pricing data is accurate and reliable.
Constraints:
Time: Limited to a 2-week bootcamp (live trading not feasible).
Data: Dependent on IB API's available stock price history.

## Known Unknowns / Risks
Historical Bias: Backtested success ≠ future profitability.
Data Limitations: Restricted to accessible market data.

## Lifecycle Mapping
Goal → Stage → Deliverable
Set up IBridgePy → Installation → Functional API Integration
Develop Strategies → Coding → Backtested Trading Logic
Evaluate Performance → Analysis → Strategy Profit Comparisons

## Repo Plan
/data/ – Market datasets
/src/ – Strategy codebase
/notebooks/ – Analysis & backtesting
/docs/ – Project documentation

Update Cadence: Regular commits aligned with development progress.
