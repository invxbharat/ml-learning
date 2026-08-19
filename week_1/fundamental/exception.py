# exception handling

try:
    a = 10 / 0
except ZeroDivisionError as e:
    print("Error: ", e)

# multiple exceptions can be handled in a multiple except blocks

try:
    a = 10 / 'a'
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data type")
finally:
    print("This block will always execute")




# else with try

try:
    a = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No error occurred, result is: ", a)


#  multiple exceptions can be handled in a single except block
try:
    a = int('a')
except (TypeError, ValueError) as e:
    print(e)

# raising custom exceptions
age = 15
if age < 18:
    raise ValueError("Age must be 18 or above")

# create custom exception class

class CustomError(Exception):
    pass

if age < 18:
    raise CustomError("Age must be 18 or above")