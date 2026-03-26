-- Write a solution to find the employees who earn more than their managers.
-- Return the result table in any order.

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee,
    left_on = 'managerId',
    right_on = 'id',
    suffixes = ('_emp', '_mng'))

    result = merged[merged['salary_emp'] > merged['salary_mng']]

    return result[['name_emp']].rename(columns = { 'name_emp' : 'Employee'})
