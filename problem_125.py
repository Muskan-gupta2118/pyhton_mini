#duplicate emails
import pandas as pd

def duplicate_emails(person):
    return person[
        person.duplicated(
            subset=["email"],
            keep=False
        )
    ][["email"]].drop_duplicates()