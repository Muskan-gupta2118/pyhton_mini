#duplicate emails
import pandas as pd

def duplicate_emails(person):
    return person[
        person.duplicated(
            subset=["emails"],
            keep=False
        )
    ][["email :"]].drop_duplicates()