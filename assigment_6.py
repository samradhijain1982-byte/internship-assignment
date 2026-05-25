import pandas as pd

# 1. Pandas Series

print("----- Series from Dictionary -----")

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

s1 = pd.Series(d)

print(s1)


print("\n----- Series from List -----")

l = [100, 200, 300, 400]

s2 = pd.Series(l)

print(s2)


print("\n----- Access Elements of Series -----")

print("First Element :", s2[0])

print("Second Element :", s2[1])



# 2. DataFrames


print("\n----- DataFrame from 2D List -----")

data = [
    [1, "Akshat", 20],
    [2, "Rahul", 21],
    [3, "Neha", 22]
]

df1 = pd.DataFrame(data, columns=["ID", "Name", "Age"])

print(df1)


print("\n----- DataFrame from Dictionary -----")

d1 = {
    "Name": ["Akshat", "Rahul", "Neha"],
    "City": ["Ahmedabad", "Delhi", "Mumbai"]
}

df2 = pd.DataFrame(d1)

print(df2)


print("\n----- DataFrame using List of Lists -----")

data2 = [
    [101, "Python"],
    [102, "Java"],
    [103, "AI"]
]

df3 = pd.DataFrame(data2, columns=["Code", "Course"])

print(df3)


print("\n----- DataFrame using List of Tuples -----")

data3 = [
    (1, "Laptop"),
    (2, "Mobile"),
    (3, "Tablet")
]

df4 = pd.DataFrame(data3, columns=["ID", "Product"])

print(df4)


print("\n----- DataFrame from List of Dicts -----")

data4 = [
    {"Name": "Akshat", "Marks": 90},
    {"Name": "Rahul", "Marks": 85},
    {"Name": "Neha", "Marks": 88}
]

df5 = pd.DataFrame(data4)

print(df5)



# 3. Data Iteration

print("\n----- Iterate Rows -----")

for index, row in df5.iterrows():
    print(index, row["Name"], row["Marks"])


print("\n----- Select Rows with Condition -----")

print(df5[df5["Marks"] > 85])


print("\n----- Select Row using iloc -----")

print(df5.iloc[1])


print("\n----- Limited Rows with Columns -----")

print(df5.loc[0:1, ["Name", "Marks"]])


print("\n----- Drop Rows with Condition -----")

df6 = df5[df5["Marks"] >= 88]

print(df6)


print("\n----- Insert Row at Given Position -----")

new_row = pd.DataFrame([{"Name": "Aman", "Marks": 95}])

df7 = pd.concat([df5.iloc[:1], new_row, df5.iloc[1:]]).reset_index(drop=True)

print(df7)


print("\n----- Create List from DataFrame Rows -----")

list1 = df5.values.tolist()

print(list1)
