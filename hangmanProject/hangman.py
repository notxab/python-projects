

import random
import string


wordList=''
rWord=''
hidden_word=''




def initialize():
    with open('words.txt', 'r') as wordList:
        wordList=wordList.read().splitlines()
        rWord = random.choice(wordList).lower()
        hidden_word = ["_"] * len(rWord)
        lives = 5
        alphabet = string.ascii_lowercase

    while "_" in hidden_word and lives>0:
        guess = input(f'\n{" ".join(hidden_word)}\n choose a letter - ').strip().lower()
        if guess in rWord and alphabet:
            onCorrectGuess(guess, hidden_word, rWord)
        else:
            lives = onWrongGuess(lives)

    if "_" not in hidden_word:
        print(f"good job! you got the word {rWord} right, you beat hangman.")
        exit()
    else:
        print(f'dumbass, the word was {rWord}')





def onCorrectGuess(guess, hidden_word, rWord):
    for i, letter in enumerate(rWord):
        if letter == guess:
            hidden_word[i] = guess
    print(f'\nCorrect!\n{" ".join(hidden_word)}\n')





def onWrongGuess(lives):
    lives -= 1
    print(f'incorrect! you got {lives} lives!')
    return lives





playHangman = str(input('would you fathom a game of...\n      HANGMAN?!\ny/n - '))
if playHangman == 'y':
    initialize()
elif playHangman == 'n':
    print('exiting!')
    exit()
else:
    print('enter either y/n!')
    exit()



