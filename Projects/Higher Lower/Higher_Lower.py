import random


def higher_lower_game():
    random_number = random.randint(1, 100)
    attempts = 8
    print("\nThe Number Guessing Game: Guess a number between 1 and 100,\nor enter 'quit' to end the game. \n")
    while attempts > 0:
        choice = input(f"You have {attempts} attempt(s) left. Enter your guess: ")
        if choice.lower() == "quit":
            print("Thank you for playing, Bye!")
            break
        if not choice.isdigit():
            print("Please enter a valid number or 'quit' to exit.")
            continue
        choice = int(choice)
        attempts -= 1
        if choice == random_number:
            print(f"Good pick! The number was {random_number}. You won!")
            break
        elif choice > random_number:
            print("Lower!")
        else:
            print("Higher!")
        if attempts == 0:
            print(f"You're out of attempts! The number was {random_number}. Better luck next time!")


higher_lower_game()
