import pandas as pd
import numpy as np
import datetime as dt  
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Any


# Example template:
def Rationale_1(df: pd.DataFrame) -> pd.DataFrame:
    """Add spend_income_ratio feature and plot scatter."""
    df = df.copy()
    df['spend_income_ratio'] = df['monthly_spend'] / df['income']
    df.plot.scatter(x='income', y='monthly_spend')
    plt.title('Income vs Monthly Spend')
    plt.show()
    return df

## Rationale for Feature 1
# The spend_income_ratio feature is created to understand the relationship between income and spending.
# By visualizing this relationship, we can identify potential outliers and trends in the data.


# TODO: Add another feature
def Rationale_2(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Add rolling_spend_mean feature and plot line."""
    df = df.copy()
    df['rolling_spend_mean'] = df['monthly_spend'].rolling(window).mean()
    df.plot.line(y='rolling_spend_mean')
    plt.title(f'Rolling Spend Mean (window={window})')
    plt.show()
    return df

## Rationale for Feature 2
# The rolling_spend_mean feature is created to capture the trend of spending over time.
# By visualizing the rolling mean, we can identify periods of increased or decreased spending behavior. 

# Optional: Add a feature to capture the change in spending behavior
def Rationale_3(df: pd.DataFrame) -> pd.DataFrame:
    """Add spend_change feature and plot line."""
    df = df.copy()
    df['spend_change'] = df['monthly_spend'].diff()
    df.plot.line(y='spend_change')
    plt.title('Spend Change Over Time')
    plt.show()
    return df

## Rationale for Feature 3
# The spend_change feature is created to understand how spending behavior is changing over time.
# By visualizing the change in spending, we can identify trends and potential issues in customer behavior.