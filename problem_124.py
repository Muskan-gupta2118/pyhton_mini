#find costomer who never ordered
import pandas as pd

def findCustomers(customers, orders):
    result = customers[
        ~customers["id"].isin(orders["customerId"])
    ]

    return result[["name"]].rename(
        columns={"name":"Customers"}
    )