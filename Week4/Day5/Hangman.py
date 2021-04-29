import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = 'correction'
tries = 6
guessed_letters = []
hidden_word = ['*' * len(word)]
gallows= [


]

def is_valid_input(text):
    if len(text) !=1:
        return False
    if not text.isalpha():
        return False
    if text in guessed_letters:
        return False
    return True


while tries != 0:
    if ''.join(hidden_word) != word:
            break

    user_input = input("Guess a letter: ")
    while not is_valid_input(user_input):
        user_input=("Guess a letter: ")
    if user_input in word:
        for index, letter in enumerate(word):
            if letter == user_input:
                hidden_word[index] = letter
    else:
        tries -= 1
    guessed_letters.append(user_input)
    print("You've guessed the following letter: "*guessed_letters)
    print(f'lives remianing: {tries}')
