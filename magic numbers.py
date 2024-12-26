import random


def number_guessing_game():
    
    lower_bound = 1
    upper_bound = 100

    
    secret_number = random.randint(lower_bound, upper_bound)

    
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))

            # Increment the attempt counter
            attempts += 1

            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Please enter a valid integer.")
            
number_guessing_game()
