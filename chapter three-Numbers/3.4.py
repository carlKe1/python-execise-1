#Write a program that generates a random decimal number between 1 and 10 with two decimal
#places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.

import random

# Generate a random integer between 100 and 1000 (inclusive)
random_integer = random.randint(100, 1000)

# Convert the random integer to a decimal number with two decimal places
random_decimal = random_integer / 100

# Print the random decimal number
print("Random decimal number:", random_decimal)
