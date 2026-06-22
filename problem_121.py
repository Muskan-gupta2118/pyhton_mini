import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Marks":[80,np.nan,70,90]
})

print(df)

#missing value
print(df.isnull())