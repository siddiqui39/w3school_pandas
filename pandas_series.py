import pandas as pd

a = [1, 7, 2]

myvar= pd.Series(a)
print(myvar)
print(myvar[0])

b = [1, 7, 2]

myvar = pd.Series(b, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#create a dataframe from two series

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)