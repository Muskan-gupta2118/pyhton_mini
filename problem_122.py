#merge dataframes

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A ","B","C"]
})

marks = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[80,90,85]
})

result = pd.merge(
    students,
    marks,
    on="ID"
)

print(result)