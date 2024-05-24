#A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
#the percent tip they want to leave. Then print both the tip amount and the total bill with the
#tip included

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