#study functions arguments and return values
# Function is a block of reusable code that performs a specific task.


# def get_food_name():
#     return "Shawarma"

# food_nanme = get_food_name()
# print(food_nanme)


# # Defining a function with parameters
# def greet(name):
#     """This function greets the person passed as a parameter."""
#     return f"Hello, {name}!"
    
# # Calling a function
# print(greet("Alice"))
# print(greet("Bob")) 


# #Arguments
# #argumenta are the values passed to a function when it is called.

# #Positional Arguments
# #These are passed to a function in the correct order.

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Alice", 30)  # Correct order

# #Keyword Arguments
# #You specify the name of the argument during the function call.

# greet(age=25, name="Bob")

# #Order doesn’t matter when you use keyword arguments.

#Default Arguments
#You can provide default values in the function definition.

# def food(name, classification=None):
#     if classification == "Fast Food":
#         print(f"{name} is classified as {classification}.")
#     elif classification == "Dessert":
#         print(f"{name} is classified as {classification}.")
#     else:
#         print(f"{name} has no specific classification.")

# food("Pizza", "Fast Food")
# food("Ice Cream", "Dessert")
# food("Salad")  # classification defaults to None



# def greet(name, age=18):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Charlie")  # age defaults to 18

#Variable-Length Arguments
#args – Arbitrary Positional Arguments

#Allows you to pass multiple positional arguments as a tuple.

# def add_numbers(*number):
#     print(number)
#     for n in number:
#         print(f"{n} \n")
#     print(sum(number))

# add_numbers(1, 2, 3, 4)  # Output: 10

#kwargs – Arbitrary Keyword Arguments
#Allows you to pass multiple keyword arguments as a dictionary.

def students_info(**kwargs):
    print(kwargs)

students_info(name="Uche", age=25, city="Agbor")

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="Paris")

#Positional-Only and Keyword-Only Arguments (Python 3.8+)
#Positional-only (/): Arguments must be passed positionally.
#Keyword-only (*): Arguments must be passed as keywords.

def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(1, 2, 3, d=4)  
# func(a=1, b=2, c=3, d=4) Error: a and b must be positional

#Return Values
#return value is the value that a function gives back after execution. using the return statement inside a function.

def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8

#returning multiple values
def get_name_and_age():
    return "Alice", 30  

name, age = get_name_and_age()
print(name)  # Output: Alice    
print(age)   # Output: 30


#loop through the word programming and prinnt each letter except letter 'm'
word = "programming"

for letter in word:
    if letter != 'm':
        print(letter)
