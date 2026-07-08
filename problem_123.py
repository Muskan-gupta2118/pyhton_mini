#finding employees salary is more than average salary
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C","D"],
    "Salary":[40000,50000,60000,70000]
})

avg = df["Salary"].mean()

result = df[df["Salary"] > avg]

print(result)