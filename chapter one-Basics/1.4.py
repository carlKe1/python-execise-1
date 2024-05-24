#Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the
#three numbers and print out the values of total and average

# Ask the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the sum of the three numbers
total = num1 + num2 + num3

# Calculate the average of the three numbers
average = total / 3

# Print out the values of total and average
print("The total is:", total)
print("The average is:", average)
