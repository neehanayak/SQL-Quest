"""
Find the names of the customer that are either:
1. referred by any customer with id != 2.
2. not referred by any customer.
Return the result table in any order.
"""

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    return df[['name']]
