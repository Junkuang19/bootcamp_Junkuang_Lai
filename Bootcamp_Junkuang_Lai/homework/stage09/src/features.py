import pandas as pd
import numpy as np
import datetime as dt  
import seaborn as sns
import matplotlib.pyplot as plt

# Example template:
df['spend_income_ratio'] = df['monthly_spend'] / df['income']  # TODO: Your feature
# Add rationale in markdown below
df.plot.scatter(x='income', y='monthly_spend')

## Rationale for Feature 1
# The spend_income_ratio feature is created to understand the relationship between income and spending.
# By visualizing this relationship, we can identify potential outliers and trends in the data.


# TODO: Add another feature
df['rolling_spend_mean'] = df['monthly_spend'].rolling(3).mean()
df.plot.line(y='rolling_spend_mean')

## Rationale for Feature 2
# The rolling_spend_mean feature is created to capture the trend of spending over time.
# By visualizing the rolling mean, we can identify periods of increased or decreased spending behavior. 

# Optional: Add a feature to capture the change in spending behavior
df['spend_change'] = df['monthly_spend'].diff()
df.plot.line(y='spend_change')

## Rationale for Feature 3
# The spend_change feature is created to understand how spending behavior is changing over time.
# By visualizing the change in spending, we can identify trends and potential issues in customer behavior.