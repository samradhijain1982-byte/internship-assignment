import numpy as np

# Q1 Combine 1D and 2D Array

a = np.array([1, 2, 3])

b = np.array([[4, 5, 6],
              [7, 8, 9]])

c = np.vstack((a, b))

print("Q1")
print(c)


# Q2 Flatten 2D Array

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\nQ2")
print(a.flatten())


# Q3 Reverse Array

a = np.array([10, 20, 30, 40, 50])

print("\nQ3")
print(a[::-1])


# Q4 NumPy Operations

a = np.array([[10, 20, 30],
              [40, 50, 60]])

print("\nQ4")

print("Maximum =", np.max(a))
print("Minimum =", np.min(a))

r, c = a.shape
print("Rows =", r)
print("Columns =", c)

print("All Elements:")
for i in a:
    for j in i:
        print(j, end=" ")

print("\nSpecific Element =", a[1][2])

s = 0
for i in a:
    for j in i:
        s = s + j

print("Sum =", s)

x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition =", x + y)
print("Subtraction =", x - y)
print("Multiplication =", x * y)
print("Division =", x / y)


# Q5 Iterate 3D Array using for loop and nditer

a = np.array([[[1, 2],
               [3, 4]],
              
              [[5, 6],
               [7, 8]]])

print("\nQ5")

print("Using For Loop")
for i in a:
    for j in i:
        for k in j:
            print(k, end=" ")

print("\nUsing nditer")
for i in np.nditer(a):
    print(i, end=" ")


# Q6 Average of Two Arrays

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

avg = (arr1 + arr2) / 2

print("\n\nQ6")
print(avg)


# Q7 Mean Median Mode of Two 2D Arrays

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

c = np.concatenate((a, b))

print("\nQ7")

print("Mean =", np.mean(c))
print("Median =", np.median(c))

value, count = np.unique(c, return_counts=True)
mode = value[np.argmax(count)]

print("Mode =", mode)
