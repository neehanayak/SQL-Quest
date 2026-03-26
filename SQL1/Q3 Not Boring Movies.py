# Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
# Return the result table ordered by rating in descending order.

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id']%2 == 1) & (cinema['description'] != 'boring')]
    return df.sort_values(by = 'rating', ascending = False)
