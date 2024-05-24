#Write a program that generates a random number between 1 and 10 and prints your name
#that many times

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Print my name that many times
for _ in range(random_number):
    print("Caleb")
