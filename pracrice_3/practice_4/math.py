# math.py

import math
import random

# Built-in functions
print("Min:", min(5, 10, 2))
print("Max:", max(5, 10, 2))
print("Abs:", abs(-7))
print("Round:", round(3.14159, 2))
print("Power:", pow(2, 3))

# math module
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))
print("Sin(0):", math.sin(0))
print("Pi:", math.pi)
print("Euler:", math.e)

# random module
print("Random float:", random.random())
print("Random int:", random.randint(1, 10))

items = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(items))

random.shuffle(items)
print("Shuffled list:", items)