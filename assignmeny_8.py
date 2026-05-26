import pandas as pd

# 1 Convert Date Strings to TimeSeries
# -----------------------------------

print("----- Date String to TimeSeries -----")

dates = ["2025-01-10", "2025-02-15", "2025-03-20"]

ts = pd.to_datetime(dates)

print(ts)

# 2 Merge and Join DataFrames
# -----------------------------------

print("\n----- DataFrames -----")

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Akshat", "Rahul", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Marks": [85, 90, 88]
})

print("\nDataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)


# Inner Merge
# -----------------------------------

print("\n----- Inner Merge -----")

inner_merge = pd.merge(df1, df2, on="ID", how="inner")

print(inner_merge)

# Left Join
# -----------------------------------

print("\n----- Left Join -----")

left_join = pd.merge(df1, df2, on="ID", how="left")

print(left_join)

print("\nMissing values become NaN where matching ID is not found.")

# Right Join
# -----------------------------------

print("\n----- Right Join -----")

right_join = pd.merge(df1, df2, on="ID", how="right")

print(right_join)

# Index Based Join
# -----------------------------------

print("\n----- Index Based Join -----")

df1_index = df1.set_index("ID")

df2_index = df2.set_index("ID")

join_df = df1_index.join(df2_index)

print(join_df)

# Merge with Multiple Keys
# -----------------------------------

print("\n----- Merge with Multiple Keys -----")

d1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Course": ["Python", "Java", "AI"],
    "Fees": [1000, 2000, 3000]
})

d2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Course": ["Python", "Java", "AI"],
    "Duration": ["2 Month", "3 Month", "4 Month"]
})

multi_merge = pd.merge(d1, d2, on=["ID", "Course"])

print(multi_merge)

# 3 Concatenate and Merge
# -----------------------------------

print("\n----- Concatenate and Merge -----")

df3 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Aman", "Riya"]
})

df4 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Karan", "Sneha"]
})

df5 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "City": ["Ahmedabad", "Delhi", "Mumbai", "Pune"]
})

concat_df = pd.concat([df3, df4])

print("\nConcatenated DataFrame")
print(concat_df)

final_merge = pd.merge(concat_df, df5, on="ID")

print("\nMerged DataFrame")
print(final_merge)

# Difference Between join() and merge()
# -----------------------------------

print("""
1. merge() is used to combine DataFrames using common columns.

2. join() is mainly used to combine DataFrames using index.

3. merge() works like SQL joins.

4. join() is simpler for index based joining.
""")
