import pandas as pd

data = {
    "calories": [420, 330, 430],
    "duration": [50, 40, 54]
}
#load data into DataFrame object
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0,1]]) #result is a dataframe

a = {
    "calories": [420, 330, 430],
    "duration": [50, 40, 54]
}
 df1 = pd.DataFrame(a, index = ["day1", "day2", "day3"])
 print(df1)

 #locate named indexes
 print(df1.loc["day2"])

 #load files
 df2 = pd.read_csv('data.csv')