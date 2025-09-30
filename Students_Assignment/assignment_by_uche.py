# Decorators

# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
# Decorators are often used for logging, access control, instrumentation, and caching.
# In Python, decorators are implemented as functions (or classes) that return a new function (or callable) that wraps the original function.
# Decorators are applied to functions using the "@" symbol above the function definition.


# Practical Use Cases for Decorators
# Decorators are used extensively in the Python ecosystem for clean, reusable functionality:

# Logging: Automatically logging when a function is called, what arguments it received, and what it returned.
# Authentication/Authorization: In web frameworks (like Flask or Django), decorators check if a user is logged in or has the correct permissions before executing a view function.
# Timing/Profiling: Measuring how long a function takes to execute.
# Caching (@functools.lru_cache): Storing the results of a function call so that the next time the function is called with the same arguments, the cached result is returned instantly.
# Built-in Decorators: Python provides built-in decorators like @property, @classmethod, and @staticmethod to modify the behavior of class methods.

# Example 1
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() # Output: Something is happening before the function is called.

# Example 2
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles to the ice cream!")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")
    
get_ice_cream("chocolate") # Output: Adding sprinkles to the ice cream! Here is your chocolate ice cream!

# Abstract Decorator Example
def decorator_with_args(decorator_arg1, decorator_arg2):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {decorator_arg1}, {decorator_arg2}")
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@decorator_with_args("arg1", "arg2")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Output: Decorator arguments: arg1, arg2 Hello, Alice!  