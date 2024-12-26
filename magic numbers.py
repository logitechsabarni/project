import random


def number_guessing_game():
    # Define the range for the number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number between lower_bound and upper_bound
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialize the number of attempts
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    # Loop until the player guesses correctly
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


# Run the game
number_guessing_game()
