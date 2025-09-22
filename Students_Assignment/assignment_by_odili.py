# DATA STRUCTURES IN PYTHON


# # 1️⃣ LIST (Dynamic Array)
# # A list is an ordered collection that can store mixed data types.
# # It allows indexing, slicing, and modifications.
# fruits = ["apple", "banana", "cherry"]  # Creating a list
# fruits.append("mango")  # Add an item to the end
# fruits.remove("banana")  # Remove an item by value
# print("List:", fruits)  # Output: ['apple', 'cherry', 'mango']





# 3️⃣ DICTIONARY (Key-Value Pair)
# A dictionary stores data as key-value pairs.
student = {"name": "Alice", "age": 21, "grade": "A"}
student["age"] = 22  # Update value
print("Dictionary:", student)


# 4️⃣ SET (Unique Unordered Collection)
# A set stores unique items without duplicates.
numbers = {1, 2, 3, 3, 4}
numbers.add(5)  # Add an item
print("Set:", numbers)  # Output: {1, 2, 3, 4, 5}


# 5️⃣ STACK (Last-In-First-Out / LIFO)
# Think of a stack like a stack of plates: last plate added is removed first.
stack = []
stack.append(10)  # Push operation
stack.append(20)
stack.append(30)
print("Stack before pop:", stack)
stack.pop()  # Pop removes the last item
print("Stack after pop:", stack)  # Output: [10, 20]


# 6️⃣ QUEUE (First-In-First-Out / FIFO)
# Think of a queue like people in a line: first in line is served first.
from collections import deque
queue = deque()
queue.append("A")  # Enqueue
queue.append("B")
queue.append("C")
print("Queue before dequeue:", queue)
queue.popleft()  # Dequeue removes the first item
print("Queue after dequeue:", queue)  # Output: deque(['B', 'C'])


# ===============================
# ALGORITHMS IN PYTHON
# ===============================

# 7️⃣ LINEAR SEARCH
# Search for a value in a list by checking each element one by one.
def linear_search(data, target):
    """
    data: list of elements to search through
    target: the value to find
    Returns the index of target if found, else -1
    """
    for i in range(len(data)):        # Loop through each index in the list
        if data[i] == target:         # Check if current element matches target
            return i                   # Return the index where it was found
    return -1                          # Return -1 if not found

nums = [5, 3, 8, 4, 2]
print("Linear Search (find 8):", linear_search(nums, 8))  # Output: 2


# 8️⃣ BUBBLE SORT
# Sorts a list by repeatedly swapping adjacent elements if they are in the wrong order.
def bubble_sort(data):
    """
    data: list of numbers to sort
    Sorts the list in ascending order using Bubble Sort algorithm.
    Time Complexity: O(n^2) (slower for large lists)
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):  # Loop through unsorted part of the list
            if data[j] > data[j + 1]:  # Compare adjacent elements
                data[j], data[j + 1] = data[j + 1], data[j]  # Swap if out of order

numbers = [64, 25, 12, 22, 11]
bubble_sort(numbers)
print("Bubble Sorted List:", numbers)  # Output: [11, 12, 22, 25, 64]