"""Find last time when there was an error in logs"""

import sqlite3 
from contextlib import closing
import pandas as pd 

def last_time_error(df):
    """Returns the most recent time, (last_time) an err. occured in df"""

    """Using usual python"""
    # last_time = None
    # for _, row in df.iterrows():
    #     if (row['status_code'] < 400): # if no err. we continue
    #         continue
    #     if not last_time or row['time'] > last_time: # Otherwise, if it's the first_time (i.e, last_time is not none) or the current time is 
    #                                                     # greater than the last_time 
    #         last_time = row['time'] # last time or most recent time is assigned the bigger current time.
    # return last_time

    """Using pandas"""

    return df[df['status_code'] >= 400]['time'].max() # this does not run, unlike the latter. 

def load_df(db_file):
    """Load DataFrame from database"""
    conn = sqlite3.connect(db_file, detect_types = sqlite3.PARSE_DECLTYPES)
    with closing(conn):
        return pd.read_sql('SELECT * FROM logs', conn)

"""This code is just a placeholder, serving only for code writing practice, doesn't really run, as there is no logs table or logs sqlite3 db."""
"""UPDATE: This code runs, this was previously successfully run from ipython, for reasons, yet unknown."""