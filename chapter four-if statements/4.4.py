#A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
#items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
#program that asks the user how many items they are buying and prints the total cost.

# Ask the user how many items they are buying
num_items = int(input("How many items are you buying? "))

# Calculate the total cost based on the number of items
if num_items < 10:
    total_cost = num_items * 12
elif 10 <= num_items <= 99:
    total_cost = num_items * 10
else:
    total_cost = num_items * 7

# Print the total cost
print("Total cost:", total_cost)
