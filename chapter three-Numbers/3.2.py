#Write a program that generates a random number, x, between 1 and 50, a random number y
#between 2 and 5, and computes x
#y

import random

# Generate random numbers x and y
x = random.randint(1, 50)
y = random.randint(2, 5)

# Compute the result of x^y
result = x ** y

# Print the values of x, y, and the result
print("x is:", x)
print("y is:", y)
print("x^y is:", result)
