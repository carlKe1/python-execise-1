#Ask the user to enter a number. Print out the square of the number, but use the sep optional
#argument to print it out in a full sentence that ends in a period. Sample output is shown
#below

# Ask the user to enter a number
number = float(input("Enter a number: "))

# Calculate the square of the number
square = number ** 2

# Print out the square in a full sentence ending in a period
print("The square of", number, "is", square, ".")
