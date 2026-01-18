import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

df.dropna(inplace = True)
print(df.to_string())

# filling empty cell with data

df.fillna(130, inplace = True)
df.fillna({"Calories": 130}, inplace = True)

x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace = True)
y = df["Calories"].median()
df.fillna({"Calories": y}, inplace = True)
z = df["Calories"].mode()[0]
df.fillna({"Calories": z}, inplace = True)

df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
print(df.to_string())