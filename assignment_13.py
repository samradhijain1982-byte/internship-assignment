import numpy as np

# Q1 Replace NaN with 0 and Interchange Rows and Columns

a = np.array([[6, -8, 73, -110],
              [np.nan, -8, 0, 94]])

a = np.nan_to_num(a, nan=0)

print("Q1")
print(a)

print("Transpose:")
print(a.T)


# Q2 Move Axes of 3D Array

a = np.arange(24).reshape(2, 3, 4)

b = np.moveaxis(a, 0, 2)

print("\nQ2")
print(b)


# Q3 Replace NaN Values with Column Average

a = np.array([[1, np.nan, 3],
              [4, 5, np.nan],
              [7, 8, 9]])

mean = np.nanmean(a, axis=0)

index = np.where(np.isnan(a))

a[index] = np.take(mean, index[1])

print("\nQ3")
print(a)


# Q4 Replace Negative Values with Zero

a = np.array([6, -8, 73, -110, 0, 94])

a[a < 0] = 0

print("\nQ4")
print(a)


# Q5 Average, Mean, Median and Mode

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

avg = (arr1 + arr2) / 2

print("\nQ5")
print("Average Array =", avg)

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

c = np.concatenate((a, b))

print("Mean =", np.mean(c))
print("Median =", np.median(c))

value, count = np.unique(c, return_counts=True)
mode = value[np.argmax(count)]

print("Mode =", mode)


# Q6 Solve Equations Using linalg() and Inverse Matrix

# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

X = np.linalg.solve(A, B)

print("\nQ6 Using linalg.solve()")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])

A_inv = np.linalg.inv(A)

X2 = np.dot(A_inv, B)

print("\nUsing Inverse Matrix")
print("x =", X2[0])
print("y =", X2[1])
print("z =", X2[2])
