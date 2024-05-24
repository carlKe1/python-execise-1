#The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
#number thereafter is the sum of the two preceding numbers. Write a program that asks the
#user how many Fibonacci numbers to print and then prints that many.
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . 

# Ask the user how many Fibonacci numbers to print
num_fibonacci = int(input("Enter the number of Fibonacci numbers to print: "))

# Initialize variables for the first two Fibonacci numbers
fibonacci_sequence = [1, 1]

# Generate Fibonacci numbers based on the user's input
for i in range(2, num_fibonacci):
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)

# Print the Fibonacci numbers
print("The first", num_fibonacci, "Fibonacci numbers are:")
for number in fibonacci_sequence:
    print(number, end=" ")
