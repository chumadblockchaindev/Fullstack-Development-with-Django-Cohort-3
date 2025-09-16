# Conditional Statements, Loops and Functions

# if, elif, else statements

# allowed_age = 18
# user_age = int(input("Enter your age: "))

# if user_age < allowed_age:
#     print("Age not allowed")
# elif user_age > allowed_age:
#     print("Age is allowed")
# elif user_age == allowed_age:
#     print("You are exactly at the allowed age")
# else:
#     print("Invalid age")

# case = {
#     18: "You are exactly at the allowed age",
#     19: "Age is allowed",
#     20: "Age is allowed",
# }
# print(case.get(user_age, "Age not allowed"))


# if user_age >= allowed_age:
#     print("Age is allowed")
# else:
#     print("Age is not allowed")


# for loops, while loops
# Loop Loops through a sequence (like a list, tuple, dictionary, set, or string)
# word = "Hello"
# print(len(word))

# for letter in "Hello":
#     print(letter)

# print(range(5))

# for i in range(5):
#     print(i)

# number = 5

# while number >= 0:
#     print(number)
#     number = number - 1
number = 5
# Infinite loop
while True:
    print("number:", number)
    number = number - 1
    if number == 0:
        break


# break, continue, pass

# Week 4:


# Assignment1: Study Functions, Arguments & Return Values
# Assignment2: Loop through the word "Programming" and print each letter except the letter "m"

# Functions: 

# Defining functions

# Arguments & return values
