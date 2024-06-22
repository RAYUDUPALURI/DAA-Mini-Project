import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You need to guess a number in the specified range.")

    while True:
        try:
            X = int(input("Enter the lower bound of the range (X): "))
            Y = int(input("Enter the upper bound of the range (Y): "))
            if X >= Y:
                print("Upper bound (Y) must be greater than lower bound (X). Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers for X and Y.")

    secret_number = random.randint(X, Y)
    print(f"A random number between {X} and {Y} has been chosen. Start guessing!")

    num_guesses = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            num_guesses += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {secret_number} correctly.")
                print(f"It took you {num_guesses} guesses.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
