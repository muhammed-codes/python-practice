import math

# ==========================================
# Lesson 3: Operators & Conditionals
# ==========================================
# Assignment Operators
# Arithmetic Operators
# Combining assignment and arithmetic operators

initial_value = 10.0
initial_value += 5.0 # This line adds 5.0 to the initial_value, resulting in 15.0.
initial_value -= 3.24 # This line subtracts 3.24 from the initial_value, resulting in 11.76.
initial_value *= 2.0 # This line multiplies the initial_value by 2.0, resulting in 23.52.
print(initial_value)

initial_value /= 4.0 # This line divides the initial_value by 4.0, resulting in 5.88.
print(round(initial_value)) # This line rounds the initial_value to whole numbers, resulting in 6.

# Tenary Operators
print("You are eligible to vote." if initial_value >= 18 else "You are not eligible to vote.") 

# ==========================================
# Lesson 4: Strings, Data Types & Math
# ==========================================
# naming conventions for files in python is all lowercase letters with underscores between words. For example, my_file.py is a valid file name.

# ways to assign strings to variables
# Literal assignments 
first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name) # Concatenation of strings 
print(type(first_name)) 
print(type(last_name) == str) # Checking the type of the variable first_name and last_name
print(isinstance(first_name, str)) # Checking if first_name is an instance of str

# Constructor function - this function is used to create a new string object from a given value
# age = int(input("Enter your age: "))
# level = str(input("Enter your level: "))

# Casting - this is the process of converting a variable from one data type to another
# birth_month = str(input("Enter your month of birth: "))

# String index value
print(first_name[0]) # prints the first character of the string first_name
print(last_name[-1]) # prints the last character of the string last_name
print(first_name[1:4]) # prints the characters from index 1 to 3 of the string first_name
print(last_name[1:]) # prints the characters from index 1 to the end of the string last_name

# Multiple lines
statement_from_president = """Elo fokan bale.
Nigeria will soon be a great nation.
Vote Tinubu as your next president."""
print(statement_from_president)

# Escaping special characters - use \ to escape special caracters in a string.
my_string = """I am a \"Python\" developer.
I'm 3 \t years old. The '\\t' is a tab character that adds a horizontal space in the string.
I love programming in Python. \n""" # the \n is a newline character that adds a new line in the string.
print(my_string)

# string methods
new_string = "i love shukroh, but ahmad no gree give me shukroh."
print(new_string.upper()) # converts the string to uppercase
print(new_string.lower()) # converts the string to lowercase
print(new_string.title()) # converts the first character of each word to uppercase
print(new_string.capitalize()) # converts the first character of the string to uppercase
print(new_string.replace("shukroh", "hikmah")) # replaces all occurrences of "shukroh" with "hikmah"

# boolean methods
print(new_string.startswith("i love")) # returns True if the string starts with "i love", otherwise returns False
print(new_string.endswith("shukroh.")) # returns True if the string ends with "shukroh.", otherwise returns False
print(new_string.isalpha()) # returns True if all characters in the string are alphabetic, otherwise returns False
print(new_string.isdigit()) # returns True if all characters in the string are digits, otherwise returns False
print(new_string.isalnum()) # returns True if all characters in the string are alphanumeric, otherwise returns False

my_value = True
y = bool(False)

# len() function - this function returns the number of characters in a string, including spaces and special characters.
print(len(new_string)) # returns the number of characters in the string new_string

new_string += "                    ."
new_string = "               " + new_string
print(new_string.lstrip()) # removes any leading and trailing whitespace from the string new_string at the left side of the string
print(new_string.rstrip()) # removes any leading and trailing whitespace from the string new_string at the right side of the string
print(new_string.strip()) # removes any leading and trailing whitespace from the string new_string at both sides of the string


# complex data types - these are data types that can hold multiple values. Examples of complex data types are lists, tuples, sets, and dictionaries.
comp_value = 5+5j # this is a complex number with a real part of 5 and an imaginary part of 5. The "j" indicates that the number is imaginary.
print(comp_value.real) # prints the real part of the complex number
print(comp_value.imag) # prints the imaginary part of the complex number
print(type(comp_value)) # prints the type of the complex number

# Built-in functions for numbers
print(abs(-5)) # returns the absolute value of -5, which is 5
round (5.678, 2) # the round function rounds a number to a specified number of decimal places. In this case, it rounds 5.678 to 2 decimal places, resulting in 5.68.
print(pow(2, 3)) # raises 2 to the power of 3, resulting in 8
print(max(1, 2, 3, 4, 5)) # returns the maximum value from the given numbers, which is 5
print(min(1, 2, 3, 4, 5)) # returns the minimum value from the given numbers, which is 1


# the math module provides access to mathematical functions and constants. It is a built-in module in Python that can be imported and used in your code.
print(math.sqrt(16)) # returns the square root of 16, which is 4.0
print(math.pi)
print(math.ceil(4.2)) # returns the smallest integer greater than or equal to 4.2, which is 5
print(math.floor(4.8)) # returns the largest integer less than or equal to 4.8, which is 4