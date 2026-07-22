#Dataframes

import pandas as pd

data = {
    "Name": ["Muskan", "Aman", "utkarsh"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)