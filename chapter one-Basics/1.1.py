def year_turn_100():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    current_year = 2024
    year_100 = current_year + (100 - age)
    print(f"Hi {name}, you will turn 100 years old in the year {year_100}.")

year_turn_100()