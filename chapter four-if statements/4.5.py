#Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them
#whether they got it right or wrong and what the correct answer is.
#Question 1: 3 x 4 = 12
#Right!
#Question 2: 8 x 6 = 44
#Wrong. The answer is 48.
#Question 10: 7 x 7 = 49
#Right.

import random

# Function to generate a random multiplication question and check the answer
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    user_answer = int(input(f"What is {num1} x {num2}? "))
    if user_answer == answer:
        print("Right!")
    else:
        print(f"Wrong. The answer is {answer}.")

# Main function to ask the player ten randomly generated multiplication questions
def main():
    print("Welcome to the Multiplication Game!")
    print("You will be asked ten randomly generated multiplication questions.")
    print("Let's begin!\n")
    for i in range(1, 11):
        print(f"Question {i}: ", end="")
        generate_question()

# Call the main function
main()
