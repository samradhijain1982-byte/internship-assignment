# Dictionary Example

student = {
    "name": "Khushi",
    "age": 20,
    "course": "BCA"
}
print(student)

print("Name:", student["name"])

student["city"] = "Jaipur"

print(student)

# Tuple Example

numbers = (10, 20, 30, 40)

print(numbers)

print(numbers[1])

print(len(numbers))

# Set Example

fruits = {"apple", "banana", "mango"}

print(fruits)

fruits.add("orange")

print(fruits)


#math_operation.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))

#palindrome.py

#

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse Number =", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
