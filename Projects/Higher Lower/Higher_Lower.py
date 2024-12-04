import random
def hoger_lager_game():
    random_number = random.randint(1,101)
    user_choice = False
    attempt = 8
    print("The Number guessing game: Guess a number between 1 and 100")
    while user_choice == False:
        choice = int(input(f"{attempt} attempt(s) left"))
        attempt -=1
        if attempt == 0:
            print("Lost!")
            break
        if choice == random_number:
            print(f"Good pick! The number was {random_number}")
            break
        elif choice > random_number:
            print("Lower")
        else:
            print("Higher")
hoger_lager_game()