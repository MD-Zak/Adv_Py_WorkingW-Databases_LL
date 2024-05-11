"""The challenge is to optimize the script that finds how many bikes rides in 2016 were on a holiday/weekend afternoon.

- Afternoon : Between Noon and 6pm
- Weekend : Saturday or Sunday
- Holiday : Any holiday from the 2016_holiday list.
"""
import pandas as pd
from calendar import SATURDAY, SUNDAY

# 2016 holiday list
holiday_list = [
    '2016-01-01',  # new year
    '2016-01-18',  # MLK
    '2016-05-30',  # memorial
    '2016-07-04',  # independence
    '2016-09-05',  # labor
    '2016-11-11',  # veterans
    '2016-11-24',  # thanksgiving
    '2016-12-26',  # christmas
]

def load_df(file_name):
    """Loads the df from a csv file"""
    return pd.read_csv(file_name, parse_dates = {'time': ['Checkout Date', 'Checkout Time']})
    # return pd.read_csv(file_name, parse_dates = 'Checkout Date', parse_time = 'Checkout Time')

# def is_2016(s):
#     """Checks if the year is 2016"""
#     ts = pd.to_datetime(s)
#     return ts.year == 2016

# def is_weekend(s):
#     """Checks if the day is a weekend"""
#     ts = pd.to_datetime(s)
#     return ts.day_name() == 'Saturday' or ts.day_name() == "Sunday"

# def is_afternoon(s):
#     """Checks if the time is after noon"""
#     ts = pd.to_datetime(s)
#     return ts.hour >= 12 and ts.hour < 18

# def is_holiday(s):
#     """Checks if the date is a 2016 holiday"""
#     ts = pd.to_datetime(s)
#     day = ts.strftime("%Y-%m-%d") # to holiday_list format.
#     return day in holiday_list

def vacation_rides(df):
    """Returns how many rides were on a holiday afternoon"""
    # result = pd.DataFrame()
    # for _, row in df.iterrows():
    # # for row in df.itertuples(index = False):
    #     # date, time = row[3], row[4]
    #     date, time = row['Checkout Date'], row["Checkout Time"]
    #     if not is_2016(date):
    #         continue 
    #     if (is_holiday(date) or is_weekend(date)) and is_afternoon(time):
    #         # result = result.append(row, ignore_index = True)
    #         result = pd.DataFrame.from_records(row)

    #     if not (df[df['Checkout Date'].apply(is_2016)]):
    #         continue

    #     if (df[df['Checkout Date'].apply(is_holiday)] or df[df['Checkout Date'].apply(is_weekend)]) and df[df['Checkout Time'].apply(is_afternoon)]:
    #         result = pd.DataFrame(row)

    # My soln:  result = df[[(df['Checkout Date'].apply(is_holiday) | df['Checkout Date'].apply(is_weekend)) & df['Checkout Time'].apply(is_afternoon)]]
    # return result 

    year_mask = df['time'].dt.year == 2016

    day_mask = ((df['time'].dt.floor('d').isin(holiday_list))| (df['time'].dt.weekday.isin([SATURDAY, SUNDAY])))

    time_mask = ((df['time'].dt.hour >= 12) & (df['time'].dt.hour < 18))

    return df[year_mask & day_mask & time_mask]s
