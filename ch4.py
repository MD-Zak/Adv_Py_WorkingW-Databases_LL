"""" What is the median trip duration from 2017 on all active kiosks up until now"""

import pandas as pd 

df = pd.read_csv('./austin-bikes.csv.xz')

df_kiosks = pd.read_csv('./austin-kiosk.csv', index_col = "Kiosk ID") # set index to Kiosk id for faster merge
# df_kiosks.set_index("Kiosk ID")

# df = pd.concat(df_kiosks)
ndf = pd.merge(df, df_kiosks, left_on = "Checkout Kiosk ID", right_index = True)

# Use query for selecting data
active_2017 = ndf.query('Year >= 2017 & `Kiosk Status` == "active" & `Trip Duration Minutes` > 0')

# Use built-in median
print(active_2017['Trip Duration Minutes'].median())