#Write a program that asks the user to enter a number and prints the sum of the divisors of
#that number. The sum of the divisors of a number is an important function in number theory
# Function to calculate the sum of divisors of a number


def sum_of_divisors(number):
    divisor_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum

# Ask the user to enter a number
try:
    number = int(input("Enter a number: "))
    
    # Calculate and print the sum of divisors of the entered number
    print("The sum of divisors of", number, "is:", sum_of_divisors(number))
except ValueError:
    print("Invalid input! Please enter a valid integer.")
