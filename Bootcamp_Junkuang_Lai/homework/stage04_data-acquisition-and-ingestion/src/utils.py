import numpy as np
from datetime import datetime
from typing import Any

# Calculate mean and standard deviation
def calc_mean_std(function: Any):
    arr = np.array(function)
    return arr.mean(), arr.std()

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called at {datetime.now()}")
        # Print output for debugging, result display, and information output
        return func(*args, **kwargs)
    return wrapper

@log_call
def calc_mean_std_logged(function: Any):
    return calc_mean_std(function)

calc_mean_std_logged([1, 2, 3, 4, 5])