import numpy as np

# Q1 Convert 1D Array to 2D Array

a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print("After conversion")
print(b)


# Q2 Print Array Attributes

print("\nAttributes")
print("Shape =", b.shape)
print("Dimension =", b.ndim)
print("Data Type =", b.dtype)
print("Item Size =", b.itemsize)


# Q3 Create 3x3 Array of All 9

a = np.full((3, 3), 9)

print("3x3 array")
print(a)


# Q4 Create 10 Evenly Spaced Values Between 25 and 125

a = np.linspace(25, 125, 10)

print("\nQ4")
print(a)


# Q5 Convert Python List into NumPy Array

lst = [10, 20, 30, 40, 50]

a = np.array(lst)

print("\nQ5")
print(a)


# Q6 Reverse a 1D NumPy Array

a = np.array([1, 2, 3, 4, 5])

print("\n Reverse")
print(a[::-1])


# Q7 Create 4x4x3 Array and Extract Value

a = np.arange(48).reshape(4, 4, 3)

print("\nQ7")
print(a[1, 0, 2])


# Q8 Create 4x4 Array and Extract Odd Rows and Even Columns

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("\nQ8")
print(a[0::2, 1::2])


# Q9 Slice First Two Rows and First Two Columns of Second Set from 4x4x3 Array

a = np.arange(48).reshape(4, 4, 3)

print("\nQ9")
print(a[:2, :2, 1])


# Q10 Replace Odd Numbers with -1

a = np.array([[23, 56, 78, 93],
              [71, 82, 13, 24]])

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] % 2 != 0:
            a[i][j] = -1

print("\nAfter replace odd no. by -1:")
print(a)


# Q11 Get Indices of Non-Zero Elements

a = np.array([1, 0, 2, 0, 3, 0, 4])

print("\nIndex of non zero element:")
print(np.nonzero(a))


# Q12 Arithmetic Operations on Two Arrays

a = np.array([10, 20, 30])

b = np.array([2, 4, 5])

print("\nOperations:")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)


# Q13 Add Two Arrays Element by Element

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print("\nAdd")
print(a + b)


# Q14 Multiply Two Arrays Element by Element

print("\n Multiplication")
print(a * b)


# Q15 Dot Product of Two Arrays

arr1 = np.array([15, 20, 25])

arr2 = np.array([10, 40, 37])

print("\nDot product")
print(np.dot(arr1, arr2))
