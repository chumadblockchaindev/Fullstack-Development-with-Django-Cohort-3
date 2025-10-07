from ecormerce.shopping.sales import calc_shipping, cal_tax
# from sales import *
from ecormerce.shopping import sales
import sys


# Importing and using modules

# calc_shipping()
# cal_tax
# sales.calc_shipping()

# Module search path
# print(sys.path)

# Packages
# When we add __init__.py file to a folder, Python would treat the folder as a package
# A package is a container for one or more modules. A package is mapped to a directory 
# and a module is mapped to a file

# Sub-packages

# Intra-package



# The dir function
print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)