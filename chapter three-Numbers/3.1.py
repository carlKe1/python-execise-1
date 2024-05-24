#Write a program that generates and prints 50 random integers, each between 3 and 6

import random

# Generate and print 50 random integers between 3 and 6
for _ in range(50):
    random_integer = random.randint(3, 6)
    print(random_integer, end=" ")
