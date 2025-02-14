import random as rand

words = []
word_display = []

with open("word_list.txt", "r") as wordlist:
  for word in wordlist:
    words.append(word.strip())
    
def pick_random_word():
    random_word = rand.choice(words)
    for i in range(len(random_word)):
        word_display.append("_")
    return random_word,word_display    
    
def do_turn(random_word,word_display):
    right_letter = False
    previous_guesses = []
  
    letter_choice = input("Pick a letter: ")
  
    if letter_choice in random_word:
        right_letter = True
    for i in range(len(random_word)):
        if random_word[i] == letter_choice:
            word_display[i]= letter_choice
            right_letter = True
    if not right_letter:
        previous_guesses.append(letter_choice)        
    return word_display,previous_guesses

random_word,word_display = pick_random_word()
word_display,previous_guesses = do_turn(random_word,word_display)
print(word_display)
print(previous_guesses)



