""""Calculate the minimal and maximum distance driven from the data at taxi.csv.xz
Consume as little memory as possible and don't load more than 50,000 rows at a time"""


import pandas as pd

# returns a TextFileReader as an iterator obj.  of size 50_000 at most, as chunksize is used.

# max_trip =[]
# min_trip = []

# for df in dfs:
#     max_trip.append(df.max())
#     min_trip.append(df.min())

# print(pd.concat(max_trip).groupby(level = 0).max())
# print(pd.concat(min_trip).groupby(level = 0).min())

# Prescribed soln.

min_dist, max_dist = float(0), float(0)
# dfs = pd.read_csv('./taxi.csv.xz', usecols = ['trip_distance'], chunksize = 50_000) 

for df in pd.read_csv('./taxi.csv.xz', usecols = ['trip_distance'], chunksize = 50_000) :
    desc = df['trip_distance'].describe()
    min_dist = min(min_dist, desc['min'])
    max_dist = max(max_dist, desc['max'])

print('min: ', min_dist, 'max: ', max_dist)

