# Q1. Create a CSV file for address book.
# CSV file should have columns: Name, Address, Mobile, Email.
# Insert 2-3 dummy records entered by the user.

import csv

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Address", "Mobile", "Email"])

    n = int(input("Enter number of records: "))

    for i in range(n):
        print(f"\nEnter details for person {i+1}")
        name = input("Name: ")
        address = input("Address: ")
        mobile = input("Mobile: ")
        email = input("Email: ")

        writer.writerow([name, address, mobile, email])

print("Data saved successfully in address_book.csv")



# Q2. Practice DATABASE
# 1. Create Database
# 2. Create 2-3 Tables
# 3. Insert Some Records
# 4. Perform Different Select Operations
# 5. Update Some Data
# 6. Delete Some Data

import sqlite3


conn = sqlite3.connect('db1.db')


sql = '''
create table employee(
id integer primary key,
name varchar(40),
salary integer
)
'''
conn.execute(sql)


sql = 'insert into emp values(1,"Himanshu",25000)'
conn.execute(sql)

sql = 'insert into emp values(2,"Rahul",30000)'
conn.execute(sql)

sql = 'insert into emp values(3,"Aman",35000)'
conn.execute(sql)

conn.commit()

# Select All Records
sql = 'select * from emp'
res = conn.execute(sql)

print("All Records")
for row in res:
    print(row)

# Select with Condition
sql = 'select * from emp where salary > 25000'
res = conn.execute(sql)

print("\nSalary Greater Than 25000")
for row in res:
    print(row)

# Update Data
sql = 'update emp set name = "Samriddhi" where id = 1'
conn.execute(sql)
conn.commit()

# Delete Data
sql = 'delete from emp where id = 3'
conn.execute(sql)
conn.commit()

# Final Records
sql = 'select * from emp'
res = conn.execute(sql)

print("\nFinal Records")
for row in res:
    print(row)

conn.close()
