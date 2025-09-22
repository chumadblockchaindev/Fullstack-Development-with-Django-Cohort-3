# # study type conversion and logical operators comparison operations case
# #type conversion is the process of converting one data type to another data type 

# #implicit type coversion (type casting)
# #Python automatically converts one data type to another when it makes sense to do so, such as when performing operations between different types. This is also known as "type coercion".
# #Example of Implicit Conversion:
# x = 5    # integer
# y = 2.5  # float

# # Implicit conversion of integer to float
# z = x + y
# print(z)  # Output: 7.5 (float)


# #Explicit Type Conversion (Type Casting)
# #Explicit conversion requires the use of built-in functions to convert from one type to another. Python provides several functions for this.

# #int(): Converts a number or a string to an integer.
# #float(): Converts a number or a string to a float.
# #str(): Converts an object to a string.
# #list(): Converts an iterable to a list.
# #tuple(): Converts an iterable to a tuple.
# #set(): Converts an iterable to a set.
# #bool(): Converts a value to a boolean (True or False).

# # Convert float to integer
# x = 5.7
# y = int(x)
# print(y)  # Output: 5

# # Convert integer to string
# x = 10
# y = str(x)
# print(y)  # Output: '10'

# # Convert string to float
# x = "3.14"
# y = float(x)
# print(y)  # Output: 3.14

# # Convert string to integer
# x = "100"
# y = int(x)
# print(y)  # Output: 100

# #Type Conversion for Collections
# #Convert a list to a tuple or set:
# my_list = [1, 2, 3, 4]
# my_tuple = tuple(my_list)
# my_set = set(my_list)

# print(my_tuple)  # Output: (1, 2, 3, 4)
# print(my_set)    # Output: {1, 2, 3, 4}

# #Convert a string to a list:
# my_string = "hello"
# my_list = list(my_string)

# print(my_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# #Common Pitfalls in Type Conversion
# #String to Number: If you try to convert a non-numeric string to an integer or float, you'll get an error.

# x = "abc"
# y = int(x)  # Raises ValueError: invalid literal for int() with base 10: 'abc'

# #Boolean Conversion:
# #bool(0) returns False, and any non-zero number returns True.
# #An empty string ("") or an empty collection ([], (), {}) converts to False, while non-empty versions convert to True.
# bool(0)      # False
# bool(None)  # False
# bool(-10)      # True
# bool(1)     # True
# bool("")     # False
# bool("abc")  # True
# bool([ ])   # False

# #Example with Multiple Conversions
# x = "123.45"  # string

# # Convert to float
# y = float(x)
# print(y)  # Output: 123.45 (float)

# # Convert to int (this will truncate the decimal part)
# z = int(y)
# print(z)  # Output: 123 (int)

# # Convert back to string
# w = str(z)
# print(w)  # Output: '123' (string)


#Logical Operators
#lodical operators combine conditional statements and return a boolean value (True or False)

#and- returns True if both statements are true
#or- returns True if one of the statements is true
#not- reverses the result, returns False if the result is true and vice versa
# print(1 and 0)
# print(1 or 0)
# print(not 1)
# print(not 0)
x = 7

# and operator
print(x > 5 and x < 10)  # True (7 is greater than 5 AND less than 10)

# or operator
print(x < 5 or x > 10)   # False (7 is neither less than 5 nor greater than 10)

# not operator
print(not(x == 7))       # False (x == 7 is True, so not True -> False)
print(not(x == 5))       # True  (x == 5 is False, so not False -> True)

#How Logical Operators Work with Non-Boolean Values
#In Python, logical operators can also be used with non-boolean values, and they return one of the operands:

#and: Returns the first Falsey value or the last value if all are true.
#or: Returns the first Truthy value.
#not: Always returns True or False.
print(0 and 5)  # Output: 0 (because 0 is Falsey)
print(5 and 0)  # Output: 0 (0 is Falsey)
print(5 and 10) # Output: 10 (both True, so returns last)
print(0 or 5)   # Output: 5 (first Truey value)
print("" or "Hello") # Output: Hello ("" is Falsey)
print(not "")   # Output: True (not Falsey value)


#Comparison Operators
#Comparison operators compare two values and return a boolean result (True or False).
a = 10
b = 20
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
print(a == b)  # Equal to
print(a != b)  # Not equal to

#Comparison operators are often used in control flow statements like if, while, or loops:
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Chained Comparisons
x = 15
print(10 < x < 20)  # True (checks if x is between 10 and 20)
