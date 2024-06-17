import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You will choose a range and try to guess the number I'm thinking of.")
    
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid integers for the range.")

    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

number_guessing_game()
