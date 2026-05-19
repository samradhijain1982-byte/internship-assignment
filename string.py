
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