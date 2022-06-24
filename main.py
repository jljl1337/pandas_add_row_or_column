import pandas as pd
import numpy as np


df = pd.DataFrame()
for row in ['r1', 'r2']:
    for col in ['c1', 'c2', 'c2']:
        try:
            df.loc[row, col] += 1
        except:
            df.loc[row, col] = 1
            df = df.replace(np.nan, 0)
        print(df)
