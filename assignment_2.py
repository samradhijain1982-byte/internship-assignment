
# student_result.py
name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

mark1 = int(input("Enter marks of Subject 1: "))
mark2 = int(input("Enter marks of Subject 2: "))
mark3 = int(input("Enter marks of Subject 3: "))
mark4 = int(input("Enter marks of Subject 4: "))
mark5 = int(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = total / 5

print("\n----- RESULT -----")
print("Student Name :", name)
print("Class :", student_class)
print("Total Marks :", total)
print("Percentage :", percentage, "%")

#string.py
str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

result = str1 + " " + str2

print("\nConcatenated String:", result)

print("\nLower Case:", result.lower())

print("Upper Case:", result.upper())

print("Title Case:", result.title())

print("Swap Case:", result.swapcase())

print("Capitalize:", result.capitalize())


print("Center:", result.center(50, '*'))

print("Count of 'a':", result.count('a'))

print("Endswith 'a':", result.endswith('a'))

print("Find 'a':", result.find('a'))

print("Is Alphanumeric:", result.isalnum())

print("Is Digit:", result.isdigit())

print("Is Numeric:", result.isnumeric())

print("Is Space:", result.isspace())

print("Replace:", result.replace("a", "@"))

#assignment_operator.py

a = 10
print("Initial Value of a:", a)

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

a %= 3
print("After %= :", a)

a **= 2
print("After **= :", a)

a //= 2
print("After //= :", a)

#student_grade.py

name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

mark1 = int(input("Enter marks of Subject 1: "))
mark2 = int(input("Enter marks of Subject 2: "))
mark3 = int(input("Enter marks of Subject 3: "))
mark4 = int(input("Enter marks of Subject 4: "))
mark5 = int(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = total / 5

if percentage >= 60:
    grade = 'A'

elif percentage >= 50 and percentage < 60:
    grade = 'B'

elif percentage >= 40 and percentage < 50:
    grade = 'C'

elif percentage >= 33 and percentage < 40:
    grade = 'D'

else:
    grade = 'Fail'

print("\n----- RESULT -----")
print("Student Name :", name)
print("Class :", student_class)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
print("Grade :", grade)
