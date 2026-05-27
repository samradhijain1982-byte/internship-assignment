
# QUESTION 1
# Explore Regex Patterns


import re

print("====== REGEX VALIDATION ======")

# Email Validation
email = input("\nEnter Email: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# Mobile Number Validation
mobile = input("\nEnter Mobile Number: ")

mobile_pattern = r'^[6-9]\d{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# String Validation
text = input("\nEnter String: ")

string_pattern = r'^[A-Za-z]+$'

if re.match(string_pattern, text):
    print("String contains only alphabets")
else:
    print("Invalid String")


# Password Validation
password = input("\nEnter Password: ")

password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")




# QUESTION 2
# Explore Datetime Functions and Pandas

import pandas as pd
from datetime import datetime, timedelta

print("\n\n====== DATETIME & PANDAS ======")

# Current Date and Time
now = datetime.now()

print("\nCurrent Date and Time :", now)

# Formatting Date
print("Formatted Date :", now.strftime("%d-%m-%Y"))

# Add 5 Days
future_date = now + timedelta(days=5)

print("Date after 5 days :", future_date)

# Create DataFrame
data = {
    "Name": ["Hardik", "Rahul", "Aman"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("\nDataFrame")
print(df)

# Average Marks
average = df["Marks"].mean()

print("\nAverage Marks :", average)



# QUESTION 3
# CSV File Import, Data Cleaning and Analysis

print("\n\n====== CSV DATA ANALYSIS ======")

# Create Sample Data
student_data = {
    "Name": ["Hardik", "Rahul", "Aman", "Priya", "Neha"],
    "Age": [21, 22, 20, 21, None],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Jaipur", "Delhi", "Mumbai", "Pune", "Delhi"]
}

# Create DataFrame
students_df = pd.DataFrame(student_data)

# Save CSV File
students_df.to_csv("students.csv", index=False)

# Read CSV File
df = pd.read_csv("students.csv")

print("\nOriginal Data")
print(df)

# Check Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Fill Missing Values
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("\nData After Cleaning")
print(df)

# Analysis
print("\nAverage Marks :", df["Marks"].mean())

print("Highest Marks :", df["Marks"].max())

print("Lowest Marks :", df["Marks"].min())

# Students with Marks > 85
high_marks = df[df["Marks"] > 85]

print("\nStudents with Marks Greater than 85")
print(high_marks)
