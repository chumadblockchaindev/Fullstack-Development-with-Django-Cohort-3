# #study functions, arguments and return values
# # Function is a block of reusable code that performs a specific task.

# #Defining a function
# def greet(name):
#     """This function greets the person passed as a parameter."""
#     return f"Hello, {name}!"
    
# #Calling a function
# greeting = greet("Alice")
# print(greeting)  # Output: Hello, Alice!


# #Arguments
# #argumenta are the values passed to a function when it is called.

# #Positional Arguments
# #These are passed to a function in the correct order.

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Alice", 30)

# #Keyword Arguments
# #You specify the name of the argument during the function call.

# greet(age=25, name="Bob")

# #Order doesn’t matter when you use keyword arguments.

# #Default Arguments
# #You can provide default values in the function definition.

# def greet(name, age=18):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Charlie")  # age defaults to 18

# def food(name, classification=None):
#     if classification == "fast food":
#         print(f"{name} is classified as {classification}")
#     elif classification == "dessert":
#         print(f"{name} is classified as {classification}")
#     else:
#         print(f"{name} has no specific classification")


# #Variable-Length Arguments
# #args – Arbitrary Positional Arguments

# #Allows you to pass multiple positional arguments as a tuple.

# def add_numbers(*args):
#     print(sum(args))

# add_numbers(1, 2, 3, 4)  # Output: 10

# #kwargs – Arbitrary Keyword Arguments
# #Allows you to pass multiple keyword arguments as a dictionary.

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="Paris")

# #Positional-Only and Keyword-Only Arguments (Python 3.8+)
# #Positional-only (/): Arguments must be passed positionally.
# #Keyword-only (*): Arguments must be passed as keywords.

# def func(a, b, /, c, *, d):
#     print(a, b, c, d)

# func(1, 2, 3, d=4)  
# # func(a=1, b=2, c=3, d=4) Error: a and b must be positional

# #Return Values
# #return value is the value that a function gives back after execution. using the return statement inside a function.

# def add(x, y):
#     return x + y

# result = add(5, 3)
# print(result)  # Output: 8

# #returning multiple values
# def get_name_and_age():
#     return "Alice", 30  

# name, age = get_name_and_age()
# print(name)  # Output: Alice    
# print(age)   # Output: 30


# #loop through the word programming and prinnt each letter except letter 'm'
# word = "programming"

# for letter in word:
#     if letter != 'm':
#         print(letter)


# #Tuples
# #Tuples are ordered, immutable collections of items.
# coordinates = (10, 20)
# print(coordinates[0])  # Output: 10
# #coordinates[0] = 15  # This will raise an error because tuples are immutable

# #Sets
# #Sets are unordered collections of unique items.
# unique_numbers = {1, 2, 3, 4}
# unique_numbers.add(5)  # Adding an item
# print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
# unique_numbers.remove(2)  # Removing an item
# print(unique_numbers)  # Output: {1, 3, 4, 5}

# #Dictionaries
# #Dictionaries are unordered collections of key-value pairs.
# person = {"name": "Alice", "age": 30}
# print(person["name"])  # Accessing a value by key, Output: Alice
# person["city"] = "New York"  # Adding a new key-value pair
# print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# del person["age"]  # Removing a key-value pair
# print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

# #Algorithms
# #Algorithms are step-by-step procedures or formulas for solving a specific problem.
# #Common algorithms include sorting, searching, and mathematical computations.
# #Sorting Algorithms
# #arranges data in a specific order (e.g., ascending or descending).
# #Bubble Sort
# #bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# #searching Algorithms
# #searching algorithms are used to find specific elements within a data structure.
# #Linear Search
# #linear search checks each element in the list sequentially until it finds the target value or reaches the end of the list.
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index of the target
#     return -1  # Target not found
# #Binary Search
# #binary search works on sorted lists by repeatedly dividing the search interval in half.
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid  # Return the index of the target
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1  # Target not found

# #Mathematical Algorithms
# #These algorithms perform mathematical computations, such as finding the greatest common divisor (GCD) or
# #calculating Fibonacci numbers.
# #Euclidean Algorithm for GCD
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# #Fibonacci Sequence
# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         next_value = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_value)
#     return fib_sequence[:n]


