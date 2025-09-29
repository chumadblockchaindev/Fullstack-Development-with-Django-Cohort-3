# Data Structures

# data structures
# dta structures are ways to organize and store data for efficient access and modification.
# Common data structures in Python include lists, tuples, sets, and dictionaries.
# Lists
# [{1: "one"}, {2: "two"}]
# [[1,2], [3,4]]
# [(9,9), (2,5)]
# [1,2,3,4]
# ["hello", "good morning"]
# [1, "one", 3.3, True, [3, 4], {}, (0.9, 8)]
# Lists are ordered, mutable collections of items.
fruits = ["apple", "banana", "cherry", "orange", "grapes", "mango"]
# print(fruits)
# fruits.append("orange")  # Adding an item
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# fruits.remove("banana")  # Removing an item
# del fruits[0]
# print(fruits[0])
# print(fruits[-1])
# # fruits.clear()
# # print(fruits)
# fruits_copy = fruits.copy()
# print(fruits_copy)
# fruits.extend(range(5))
# print(fruits)
# print(fruits.index("grapes"))
# fruits.insert(2, "Cucumber")
# print(fruits)
# fruits.pop()
# print(fruits)
# # fruits.reverse()
# # print(fruits)
# del fruits[6 : ]
# print(fruits)
# fruits.sort()
# print(fruits)

# numbers = [49, 86, 84, 72, 90, 1, 5, 30, 1, 3, 71, 60, 63, 11, 8, 6, 73, 69, 82, 58]

# number_copy = numbers.copy()
# new_list = []

# for num in numbers:
#     if num % 2 == 0:
#         new_list.append(num)
#         number_copy.remove(num)

# print(numbers)
# print(number_copy)
# print(new_list)
# def sort_by_even(num):
#     return num % 2 == 0

# numbers.sort(key=sort_by_even, reverse=True)
# print(numbers)
# num1, num2 , *others= numbers
# print(num1, num2)
# print(others)

# print(len(numbers))
# for num in numbers:
#     print(num)

# Tuples

# 2️⃣ TUPLE (Immutable List)
# A tuple is like a list but cannot be changed after creation.
# coordinates = (10, 20)

# coordinates[0] = 15  # ❌ This would raise an error because tuples are immutable.
# print("Tuple:", coordinates)

# You can't change, add, or remove items from a tuple after it's created, but you can do a lot with it. A tuple is an immutable, ordered collection of items. Think of it as a fixed-length list that can't be modified.

# Common Tuple Operations
# Here's what you can actually do with a tuple:

# Access Items: You can get individual items or a range of items using indexing and slicing, just like with a list.


# my_tuple = ('apple', 'banana', 'cherry', 'date')
# print(my_tuple[1])   # Output: 'banana'
# print(my_tuple[1:3]) # Output: ('banana', 'cherry')
# # Unpack: You can assign the items of a tuple to variables in a single line. This is a very common and useful feature.


# fruits = ('apple', 'banana', 'cherry')
# fruit1, fruit2, fruit3 = fruits
# print(fruit2) # Output: 'banana'
# # Iterate: You can loop through a tuple using a for loop.


# for fruit in my_tuple:
#     print(fruit)
# # Concatenate and Repeat: You can join tuples together using the + operator and repeat a tuple using the * operator. Both operations create a new tuple.

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# new_tuple = tuple1 + tuple2  # new_tuple is (1, 2, 3, 4)
# repeated_tuple = tuple1 * 3   # repeated_tuple is (1, 2, 1, 2, 1, 2)
# # Check for an Item: You can use the in keyword to check if an item exists within a tuple.


# if 'cherry' in my_tuple:
#     print("Yes, 'cherry' is in the tuple.")
# # Use as a Dictionary Key: Because tuples are immutable, they can be used as keys in a dictionary. Lists cannot be used for this purpose. This is a major difference and a key use case.


# locations = {('New York', 'USA'): 1, ('Tokyo', 'Japan'): 2}
# print(locations[('New York', 'USA')]) # Output: 1
# # Built-in Functions: You can use functions like len(), min(), max(), and sum() on a tuple.


# numbers = (10, 5, 20)
# print(len(numbers)) # Output: 3
# print(max(numbers)) # Output: 20
# # The primary benefit of a tuple's immutability is that it makes your code safer. You can pass a tuple to a function and be confident that the function won't accidentally change the data.

# Dictionary

# A dictionary in Python is an unordered collection of data that stores
# items in key-value pairs. It's a fundamental data structure, similar
# to a real-world dictionary where you look up a word (the key) to find
# its definition (the value).

numbers = {1: "one", 2: "two", 3: "three"}
foods = {"rice": "carbohydrate", "beans": "protein", "fish": "vegetable"}
students = {1: ["leo", 22, "dark", 500000], 2: ["uche", 27, "dark", 1000000]}

# accessing values

# numbers[1] = "ten"
# print(numbers)
# foods["fish"] = "meat"
# print(foods)
# students[2][3] = 1200000
# print(students)

# if "beans" in foods:
#     print(foods["beans"])
# print(foods.get("beanss", "Food not found"))

# print(list(foods.keys()))
# print(list(foods.values()))
# print(list(foods.items()))
# foods.setdefault("meat", "protein")
# print(foods)

# # Initial dictionary with student information
# student_info = {
#     'name': 'Alice',
#     'age': 20,
#     'major': 'Physics'
# }

# # A second dictionary containing new information
# new_data = {
#     'age': 21,  # This key already exists, so its value will be updated
#     'gpa': 3.9, # This key is new, so it will be added
#     'major': 'Computer Science'
# }

# # Use the .update() method to merge the dictionaries
# student_info.update(new_data)

# print(student_info)

# Classwork
# What letter occours most in the word "Pneumonoultramicroscopicsilicovolcanoconiosis"

# long_word = "Pneumonoultramicroscopicsilicovolcanoconiosis"

# count = {}

# for letter in long_word:
#     count.setdefault(letter.lower(), 0)
#     count[letter.lower()] += 1


# new_items = list(count.items()) 

# mul = lambda x: x *3
# print(mul(4))

# def multi(x):
#     return x * 3

# print(multi(6))

# def get_num(x):
#     return x[1]

# new_items.sort(key=lambda x: x[1])
# print(new_items)
# print(new_items[-1])
# print(f"The letter \"{new_items[-1][0]}\" occours {new_items[-1][1]} times \n")

names_ages_dict = {
    'Liam': 18, 'Olivia': 19, 'Noah': 20, 'Emma': 17, 'Oliver': 16,
    'Charlotte': 15, 'Elijah': 14, 'Amelia': 13, 'James': 12, 'Ava': 11,
    'William': 10, 'Sophia': 9, 'Benjamin': 8, 'Isabella': 7, 'Lucas': 6,
    'Mia': 5, 'Henry': 4, 'Evelyn': 3, 'Theodore': 2, 'Harper': 1
}
# print(names_ages_dict.keys())
# print(sorted(names_ages_dict.values()))

