# Exceptions in Python
# numbers = [1, 3]

# try:
#     print(numbers[4])
# except IndexError as error:
#     print("Error:", error)

# Basic Error handling structure
# try: 
#     age = int(input("age: "))
# except ValueError as error:
#     print("You did not enter a valid age")
#     # print(type(error))
# else: 
#     print("No execution was thrown")
# print("Execution continues")

# Handling different errors

# try: 
#     file = open("text.txt")
# except FileNotFoundError as error:
#     print("Error: ", error)
# finally:
#     file.close()



# Using the with statement
# try: 
#     with open("app.py") as file:
#         print("File Opened.")
#     age = int(input("age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age")
# else: 
#     print("No execution was thrown")

# Raising exception & Cost of raising exception
# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")
#     return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
#     # print(error)
# """

# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10/age

# age_factor = calculate_xfactor(-1)

# if age_factor ==None:
#     pass
# """

# print("Code1 execution time", timeit(code1, number=10000))
# print("Code2 execution time", timeit(code2, number=10000))

# Creating your own custom Errors

class InsufficientDataError(Exception):
    pass

data_list = []
if not data_list:
    raise InsufficientDataError("The input list cannot be empty.")


# Adding Custom Data and Messages

# class MinimumValueError(Exception):
#     """Raised when an input value is below a specified minimum."""
#     def __init__(self, received_value, min_required, message="Value is below the minimum threshold."):
#         self.received_value = received_value
#         self.min_required = min_required
        
#         # Override the default message
#         full_message = f"{message} Received: {received_value}, Required: {min_required}."
        
#         # Call the base class constructor
#         super().__init__(full_message)

# # Example Usage and Handling
# def set_volume(level):
#     if level < 1:
#         raise MinimumValueError(received_value=level, min_required=1)
#     print(f"Volume set to {level}.")

# try:
#     set_volume(0)
# except MinimumValueError as e:
#     # 1. Print the custom error message
#     print(f"Error: {e}") 
    
#     # 2. Access the custom stored data
#     print(f"Action failed because {e.received_value} is less than {e.min_required}.")



# Decorators




# Modules 


