#Write a program that swaps the values of three variables x, y, and z, so that x gets the value
#of y, y gets the value of z, and z gets the value of x.

# Take input from the user for x, y, and z
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
z = input("Enter the value of z: ")

# Swap the values of x, y, and z
temp = x
x = y
y = z
z = temp

# Print the swapped values
print("After swapping:")
print("x =", x)
print("y =", y)
print("z =", z)
