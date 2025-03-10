import random as rand
from hangman_visual import hangman

def pick_random_word(words):
    random_word = rand.choice(words)
    word_display = ["_" for _ in range(len(random_word))]
    return random_word,word_display    
    
def display_hangman(mistakes):
    print(hangman[mistakes])
    
def do_turn(random_word,word_display,previous_guesses,mistakes):
    right_letter = False
    letter_choice = input("Pick a letter: ")
    if letter_choice in previous_guesses:
        letter_choice = input("Already guessed,pick another letter. ")
    if letter_choice in random_word.lower():
        right_letter = True
    for i in range(len(random_word)):
        if random_word.lower()[i] == letter_choice:
            word_display[i]= letter_choice
            right_letter = True
    if not right_letter:
        previous_guesses.append(letter_choice)
        mistakes += 1
    display_hangman(mistakes)
    print(f"*|  {' '.join(word_display)}  |*")
    print(f"Wrong Guesses: {' - '.join(previous_guesses)} \n")    
    return word_display,previous_guesses,mistakes

def play_hangman():
    previous_guesses = []
    mistakes = 0
    with open("word_list.txt", "r") as wordlist:
        words = [word.strip() for word in wordlist]
    word_display = pick_random_word(words)

    random_word,word_display = pick_random_word(words)
    while random_word.lower() != "".join(word_display):
        if mistakes >5:
            print(f"YOU'RE DEAD\n The word was {random_word}\n")
            break
        word_display,previous_guesses,mistakes = do_turn(random_word,word_display,previous_guesses,mistakes)
    else:
        print(f"You won! '{random_word}' was the word!")
    
play_hangman()
