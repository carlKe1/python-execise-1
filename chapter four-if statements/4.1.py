#Write a program that asks the user to enter a length in centimeters. If the user enters a negative
#length, the program should tell the user that the entry is invalid. Otherwise, the program
#should convert the length to inches and print out the result. There are 2.54 centimeters in an
#inch

# Ask the user to enter a length in centimeters
length_cm = float(input("Enter a length in centimeters: "))

# Check if the entered length is negative
if length_cm < 0:
    print("Invalid entry! Length cannot be negative.")
else:
    # Convert the length to inches
    length_inches = length_cm / 2.54
    
    # Print the result
    print("Length in inches:", length_inches)
