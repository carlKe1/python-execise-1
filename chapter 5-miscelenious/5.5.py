#Ask the user to enter 10 test scores. Write a program to do the following:
#(a) Print out the highest and lowest scores.
#(c) Print out the second largest score.
#(d) If any of the scores is greater than 100, then after all the scores have been entered, print
#a message warning the user that a value over 100 has been entered.
#(e) Drop the two lowest scores and print out the average of the rest of them.

# Function to calculate the average of a list of scores
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to drop the lowest two scores from a list
def drop_lowest_scores(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[2:]

# Ask the user to enter 10 test scores
scores = []
for i in range(1, 11):
    score = float(input(f"Enter test score {i}: "))
    scores.append(score)

# Print the highest and lowest scores
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

# Check for scores greater than 100
if any(score > 100 for score in scores):
    print("Warning: A score over 100 has been entered.")

# Print the average of the scores
average_score = calculate_average(scores)
print("Average score:", average_score)

# Print the second largest score
sorted_scores = sorted(scores)
print("Second largest score:", sorted_scores[-2])

# Drop the lowest two scores and print the average of the rest
dropped_scores = drop_lowest_scores(scores)
average_after_dropping = calculate_average(dropped_scores)
print("Average after dropping lowest two scores:", average_after_dropping)