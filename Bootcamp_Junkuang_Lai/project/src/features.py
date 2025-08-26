import pandas as pd
import numpy as np
import datetime as dt  
import seaborn as sns
import matplotlib.pyplot as plt


# Example template:
def Rationale_1(df: pd.DataFrame) -> pd.DataFrame:
    """Add volume_high_ratio feature and plot scatter."""
    df = df.copy()
    df['volume_high_ratio'] = df['volume'] / df['high']
    df.plot.scatter(x='high', y='volume')
    plt.title('High vs Volume')
    plt.show()
    return df

## Rationale for Feature 1
# The volume_high_ratio feature is created to understand the relationship between high and volume.
# By visualizing this relationship, we can identify potential outliers and trends in the data.


# TODO: Add another feature
def Rationale_2(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Add rolling_high_mean feature and plot line."""
    df = df.copy()
    df['rolling_high_mean'] = df['high'].rolling(window).mean()
    df.plot.line(y='rolling_high_mean')
    plt.title(f'Rolling High Mean (window={window})')
    plt.show()
    return df

## Rationale for Feature 2
# The rolling_high_mean feature is created to capture the trend of high prices over time.
# By visualizing the rolling mean, we can identify periods of increased or decreased high prices behavior.

# Optional: Add a feature to capture the change in high prices behavior
def Rationale_3(df: pd.DataFrame) -> pd.DataFrame:
    """Add high_change feature and plot line."""
    df = df.copy()
    df['high_change'] = df['high'].diff()
    df.plot.line(y='high_change')
    plt.title('High Change Over Time')
    plt.show()
    return df

## Rationale for Feature 3
# The high_change feature is created to understand how high prices behavior is changing over time.
# By visualizing the change in high prices, we can identify trends and potential issues in customer behavior.