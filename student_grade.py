
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