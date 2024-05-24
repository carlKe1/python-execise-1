#Write a program that asks the user to enter an angle between −180◦
#and 180◦
#. Using an
#expression with the modulo operator, convert the angle to its equivalent between 0
#◦
#and
#360◦

# Ask the user to enter an angle between -180° and 180°
angle = float(input("Enter an angle between -180° and 180°: "))

# Convert the angle to its equivalent between 0° and 360° using the modulo operator
angle_0_to_360 = angle % 360

# Print the equivalent angle between 0° and 360°
print("Equivalent angle between 0° and 360°:", angle_0_to_360)

