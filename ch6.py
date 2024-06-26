'''Using bikes.db, find the 5 bikes (using "bike_id") that has the biggest 90% quantile of ride duration in the first quarter of 2017'''

import sqlite3
import pandas as pd 

conn = sqlite3.connect('./bikes.db')

query = '''SELECT  bike_id, duration FROM bike_rides WHERE year == 2017 & month in (1,2,3)'''

df = pd.read_sql(query)

desc = df['duration'].describe()

third_quantile = desc['75%'] - desc['max']

conn.execute("""SELECT bike_id FROM bike_rides WHERE duration == %s LIMIT 5;""", third_quantile).fetchall()

# Prescribed soln.

query = """SELECT bike_id, duration FROM bike_rides WHERE year == 2017 & month < 4;"""

df = pd.read_sql(query, conn)

out = df.groupby('bike_id')['duration'].quantile(.9)
print(out.sort_values(ascending = False)[:5])
