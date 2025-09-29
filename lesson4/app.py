# OOP (Object oriented programming)
# OOP is a programming paradigm that organizes code into objects. These objects combine data (attributes)
# and behaviour (methods) into a single unit

# Key concepts of OOP
# Class: A blueprint/template for creating objects
# Objects: An instance of a class

# Constructor: A constructor is the first this method that runs automatically when a class is called 

# class Human:
#     """This is a Human class that represents the attributes and behaviour of humans"""

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         return f"{self.name} is eating\n"
    
#     def sleep(self):
#         return f"{self.name} is sleeping\n"

# human = Human("Chukwuma", 27)
# human1 = Human("Abigail", 12)

# print(human.name)
# print(human.age)
# print(human.eat())
# print(human.sleep())

# print(human1.name)
# print(human1.age)
# print(human1.eat())
# print(human1.sleep())

#Encapsulation is hiding data and restricting access to it

# Example 2

# class Car:
#     """This class represents a car"""

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.__year =  year # The double underscore makes the class private

#     def drive(self):
#         print(f"{self.brand} {self.model} is driving")

#     def __str__(self):
#         return f"This car is {self.brand} {self.model} and {self.__year}"

# car1 = Car("Toyota", "Corolla", 2025)
# car2 = Car("Tesla", "Model S", 2026)

# print(car1.brand)
# print(car1.__year) # This gives an Attribute error 
# print(car1)
# car1.drive()


# Inheritance

# Parent class
# class Mammals:
    
#     def __init__(self, name, age, skin_color):
#         self.name = name
#         self.age = age 
#         self.skin_color = skin_color
    
#     def eat(self):
#         return f"{self.name} is eating\n"
    
#     def sleep(self):
#         return f"{self.name} is sleeping\n"

# # Child 
# class Dog(Mammals):
#     """This is a Dog class that represents the attributes and behaviour of dogs"""
#     def __init__(self, name, age, skin_color):
#         super().__init__(name, age, skin_color)

#     def bark(self):
#         return f"{self.name} is barking"

# class Human(Mammals):
#     """This is a Human class that represents the attributes and behaviour of humans"""

#     def __init__(self, name, age, skin_color):
#         super().__init__(name, age, skin_color)

#     def eat(self):
#         return f"I'm eating egusi soup" 

#     def talk(self):
#         return f"My name is {self.name} and i'm {self.age} years old"


    
# human = Human("Ade", 45, "Dark")
# dog = Dog("Daisy", 1, "Black & Brown")
# print(dog.sleep())
# print(dog.eat())
# print(human.eat())


# Abstraction
# Abstraction means exposing only essential details while hiding the implementation.
# In python, abstraction can be achieved using abstract classes from the abc module.

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC): # Abstract Base Class
    
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return round(math.pi * self.radius ** 2, 4)

#     def circumference(self): 
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length * self.breadth
    
#     def perimeter(self):
#         return 2 * (self.length + self.breadth)
    
# circle = Circle(5)
# rectangle = Rectangle(6, 3)
# print(circle.area())
# print(circle.perimeter()) 
# print(rectangle.perimeter())
# print(rectangle.area())



# Magic methods

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name of this student is {self.name} and the age is {self.age}"
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
leo = Students("Leonard", 22)
martins = Students("Martin", 23)

print(leo)
print(martins)
print(leo == martins)
print(leo < martins)
