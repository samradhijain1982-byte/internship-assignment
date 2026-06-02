import numpy as np

# ==================================================
# Q1) Replace NaN with 0 and interchange rows and columns
# ==================================================

arr1 = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

arr1 = np.nan_to_num(arr1, nan=0)

print("Q1 Output:")
print("NaN replaced with 0:")
print(arr1)

print("\nTranspose (Rows and Columns Interchanged):")
print(arr1.T)

# ==================================================
# Q2) Move axes of 3D array to new positions
# ==================================================

arr2 = np.arange(24).reshape(2, 3, 4)

moved_arr = np.moveaxis(arr2, 0, 2)

print("\n\nQ2 Output:")
print("Original Shape:", arr2.shape)
print("New Shape:", moved_arr.shape)
print(moved_arr)

# ==================================================
# Q3) Replace NaN values with average of columns
# ==================================================

arr3 = np.array([
    [1, np.nan, 3],
    [4, 5, np.nan],
    [7, 8, 9]
])

col_mean = np.nanmean(arr3, axis=0)

inds = np.where(np.isnan(arr3))
arr3[inds] = np.take(col_mean, inds[1])

print("\n\nQ3 Output:")
print(arr3)

# ==================================================
# Q4) Replace negative values with 0 in NumPy array
# ==================================================

arr4 = np.array([6, -8, 73, -110, 0, 94])

arr4[arr4 < 0] = 0

print("\n\nQ4 Output:")
print(arr4)
