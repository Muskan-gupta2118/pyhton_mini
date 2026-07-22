import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Marks":[80,70,90,100]
})

print(df)

#missing value
print(df.isnull())