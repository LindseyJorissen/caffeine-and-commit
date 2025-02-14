import random as rand

def pick_random_word(words,word_display):
    random_word = rand.choice(words)
    for i in range(len(random_word)):
        word_display.append("_")
    return random_word,word_display    
    
def do_turn(random_word,word_display,previous_guesses):
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
    print("##hangman##")
    print(" ".join(word_display))
    print(f"Wrong Guesses: {' - '.join(previous_guesses)} \n")    
    return word_display,previous_guesses

def play_hangman():
    words = []
    word_display = []
    previous_guesses = []
    
    with open("word_list.txt", "r") as wordlist:
        for word in wordlist:
            words.append(word.strip())
            
    random_word,word_display = pick_random_word(words,word_display)
    while random_word.lower() != "".join(word_display):
        word_display,previous_guesses = do_turn(random_word,word_display,previous_guesses)
    print(f"You won! '{random_word}' was the word!")
    
play_hangman()    
