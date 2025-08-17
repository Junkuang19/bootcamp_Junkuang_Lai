import pandas as pd
import inspect

# View function parameter information
print(inspect.signature(pd.read_csv))
print(inspect.getdoc(pd.read_csv))