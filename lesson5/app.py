# Exceptions in Python
# numbers = [1, 3]

# try:
#     print(numbers[4])
# except IndexError as error:
#     print("Error:", error)

# # Basic Error handling structure
# try: 
#     age = int(input("age: "))
# except ValueError as error:
#     print("You did not enter a valid age")
#     # print(type(error))
# else: 
#     print("No execution was thrown")
# print("Execution continues")

# # Handling different errors

# try: 
#     file = open("text.txt")
# except FileNotFoundError as error:
#     print("Error: ", error)
# finally:
#     file.close()



# # Using the with statement
# try: 
#     # with open("app.py") as file:
#     #     print("File Opened.")
#     age = int(input("age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError) as error:
#     print("Error: ", error)
# else: 
#     print("No execution was thrown")

# Raising exception & Cost of raising exception
# from time import sleep
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")
#     return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     # pass
#     sleep(3)
#     print(error)


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
# """

# code2 = """
# def calculate_xfactor(age):
#     if age < 0:
#         return None
#     return 10/age

# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """

# print("Code1 execution time", timeit(code1, number=10))
# print("Code2 execution time", timeit(code2, number=10))

# # Creating your own custom Errors

# class InsufficientDataError(Exception):
#     pass


# def get_full_list(*numbers):
#     if not numbers:
#         raise InsufficientDataError("The input list cannot be empty.")
    
#     return numbers

# try:
#     print(get_full_list())
# except InsufficientDataError as err:
#     print("Error: ", err)


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

# # # Example Usage and Handling
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
# A decorator is just a function that takes another function 
# as an argument, adds some functionality, and returns 
# the modified function.



def multiply_get_2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_get_2
def get_x(x):
    return x

# multiplied_x = multiply_get_x(get_x(5))

print(get_x(50))

def my_decorator(age=None, auth=False):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            greeting = ""
            if not auth:
                return "Please Login to continue"
            if int(age) < 18:
                greeting = "Hello, Master"
            greeting = "Hello, Mister"
            
            return greeting + func(*args, **kwargs)        
        return wrapper
    return actual_decorator

@my_decorator(age=27, auth=True)
def say_hello(name):
    return f"{name}"

print(say_hello("Chukwuma")) # Output: Something is happening before the function is called.




# Modules 


