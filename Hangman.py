import random
from words import words
import time
def get_valid_word(words):
    word = random.choice(words) # Randomly chooses sth from words list.
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

player_name = input ("Welcome! what's your name? ")
print (f"Hello {player_name}. I hope enjoy the game! if you won less than 45 second, you are a hero without a cape {chr(171)} {chr(164)} {chr(187)}")
time.sleep (3)
def Hangman():
    word = get_valid_word (words)
    user_guess_letter = ""
    word_letters = list (word)
    right_letters = list ()
    wrong_letters = list ()
    current_word = ""
    turns = len (word)  # Number of times allowed for wrong answer.
    while turns > 0:
        current_word = [char if char in right_letters else '_' for char in word_letters]
        print ("Current_word: ", ' '.join (current_word))
        print ("Letters that not involve:", ' '.join(wrong_letters), f"your lives left: {turns}")
        user_guess_letter = input ("Guess a letter: ").upper()
        if user_guess_letter in word_letters:
            right_letters.append (user_guess_letter)
        else:    
            wrong_letters.append (user_guess_letter)
            turns -= 1
    if '_' in current_word: print (f"YOU LOSE{chr (161)}")
    else: print ("YOU WIN!")
    print (f"The word is: {word}")
    
Hangman ()