import random

def guess_number(X, Y):
    random_number = random.randint(X, Y)
    print(f"I'm thinking of a number between {X} and {Y}. Can you guess what it is?")

    num_guesses = 0
    guess = None

    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
            num_guesses += 1

            if guess < random_number:
                print("Too low! Try a higher number.")
            elif guess > random_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {num_guesses} guesses.")
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    X = 1  
    Y = 100 
    guess_number(X, Y)

