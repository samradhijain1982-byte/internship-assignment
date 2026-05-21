# 1. Write a Python function to find the maximum of three numbers.

def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(maximum(10, 25, 15))

# 2. Write a Python function that takes a list and returns
#    a new list with distinct elements from the first list.

def distinct_list(lst):
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(distinct_list([1, 2, 2, 3, 4, 4, 5]))

# 3. Write a Python function to multiply all the numbers in a list.

def multiply_list(lst):
    result = 1

    for i in lst:
        result = result * i

    return result

print(multiply_list([1, 2, 3, 4]))

# 4. Write a Python function to calculate the factorial
#    of a number.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))

# 5. Write a Python program to reverse a string.

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# 6. Write a Python function to check whether
#    a number falls within a given range.

def check_range(num):
    if num in range(1, 11):
        print("Number is in range")
    else:
        print("Number is not in range")

check_range(5)

# 7. Write a Python function to Print Even Numbers
#    from a Given List.

def even_numbers(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)

even_numbers([1, 2, 3, 4, 5, 6])

# 8. Write a Python function that takes a number
#    as a parameter and checks whether the number
#    is prime or not.

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

prime(7)


# 9. Write a Python function that accepts a string
#    and counts the number of upper and lower case letters.

def count_case(text):
    upper = 0
    lower = 0

    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    print("Upper Case Letters:", upper)
    print("Lower Case Letters:", lower)

count_case("Hello PYTHON")

# File Handling Practice

# Write data in file
file = open("demo.txt", "w")
file.write("Hello Python")
file.close()

# Read data from file
file = open("demo.txt", "r")
print(file.read())

# Append data in file
file = open("demo.txt", "a")
file.write("\nWelcome")
file.close()

# Read updated file
file = open("demo.txt", "r")
print(file.read())
