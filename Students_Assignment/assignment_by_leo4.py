#Modules
#A module is a single Python file (.py) that contains functions, classes, variables, and optionally, runnable code. It allows you to organize related code into separate files, making your programs more modular, reusable, and maintainable.
#You can create your own modules or use built-in and third-party modules.
#Creating a Module
#To create a module, simply write your Python code in a file with a .py extension.

#Step 1: Create a module file — math_utils.py
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#Step 2: Import and use it in another file — main.py
import math_utils as math_utils

print(math_utils.add(5, 3))      # Output: 8
print(math_utils.subtract(10, 4))  # Output: 6


#You can also import specific functions:

from lesson5.math_utils import add
print(add(2, 2))  # 4

#Types of Modules
# | Type             | Description               | Examples              |
# | ---------------- | ------------------------- | --------------------- |
# | **Built-in**     | Provided by Python itself | `math`, `os`, `sys`   |
# | **Third-party**  | Installed via `pip`       | `requests`, `pandas`  |
# | **User-defined** | Modules you create        | `math_utils.py`, etc. |

#Built-in Modules
#Already included with Python (no need to install).
#Examples:

import math
import random
import os


#User-defined Modules
#Created by you. Any .py file is a module.

# External Modules (Third-party)
# Installed via package managers like pip.
# Example:

# pip install requests


# Then use:

import requests

#different ways to import modules
# Import whole module
import math_utils as math_utils

# Import specific functions
from math_utils import add, subtract

# Import with alias
import math_utils as mu

# Import everything (not recommended)
from math_utils import *

