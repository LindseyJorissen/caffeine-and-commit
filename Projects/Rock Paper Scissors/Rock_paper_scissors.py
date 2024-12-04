import random
import time
def rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]
    computer_move = random.randint(0, 2)
    keuze_speler = int(input("(0) Rock, (1) Paper, (2) Scissors, ... ?"))
    print()
    for choice in choices:
        print(choice)
        time.sleep(0.8)
    print()
    print(f"Computer: {choices[computer_move]}")
    print(f"Player: {choices[keuze_speler]}")
    if keuze_speler == computer_move:
        print("It's a TIE")
    elif (keuze_speler == 0 and computer_move == 2) or \
         (keuze_speler == 1 and computer_move == 0) or \
         (keuze_speler == 2 and computer_move == 1):
        print("Player WINS")
    else:
        print("Computer WINS")
rock_paper_scissors()