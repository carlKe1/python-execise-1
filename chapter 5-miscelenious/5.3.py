# An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
#instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
#numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
#divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
#tells them if it is squarefree or not.

# Function to check if a number is squarefree
def is_squarefree(number):
    # Iterate from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        # Check if i is a divisor of the number
        if number % (i * i) == 0:
            return False
    return True

# Ask the user to enter an integer
try:
    number = int(input("Enter an integer: "))
    if number < 1:
        print("Please enter a positive integer.")
    elif is_squarefree(number):
        print(number, "is squarefree.")
    else:
        print(number, "is not squarefree.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
