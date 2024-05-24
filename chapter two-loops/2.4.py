#Write a program that asks the user for their name and how many times to print it. The program should print out the user’s name the specified number of times

# Ask the user for their name and the number of times to print it
name = input("Enter your name: ")
times = int(input("Enter the number of times to print your name: "))

# Print the name the specified number of times
for _ in range(times):
    print(name)