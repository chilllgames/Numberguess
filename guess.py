import random

def number_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while attempts > 0:
        guess = int(input("Take a guess: "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number_to_guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        attempts -= 1
        print("Attempts left:", attempts)

    if attempts == 0:
        print("Sorry, you ran out of attempts. The correct number was:", number_to_guess)

# Run the number guessing game
number_guessing_game()
