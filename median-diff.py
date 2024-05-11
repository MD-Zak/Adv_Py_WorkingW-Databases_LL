"""This code will find the median difference, of top two prices.
We will use this program to find which operation consume more time."""

import pandas as pd

def second(values):
    """Returns the second highest value
    >>> second([1, 5, 2, 9, 6]):
    6
    """
    top, second = -1, -1
    for value in values:
        if (value > top):
            top, second = value, top
        elif(value > second):
            second = value
    return second

def median_diff(csv_file):
    # df = pd.DataFrame({'price' : lyst})
    # df.index = range(1, len(df) + 1 )
    # df = df.reset_index().rename(columns = {'index': 'id'})
    df = pd.read_csv(csv_file)
    top1 = df.groupby('id')['price'].max()
    top2 = df.groupby('id')['price'].apply(second)
    diff = top1-top2
    return diff.median()