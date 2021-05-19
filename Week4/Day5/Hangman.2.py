import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)


body_parts = ['0','|','/','\\', '/','\\']
copy_of_part = ['','','','','','']




flag = True
blank_word = "_"*len(word)
blank_word = list(blank_word)
counter = 0
guess_list = []
word_li = list(word)

while flag is True:
    if counter == 6:
        flag = False
        print(blank_word)
    elif "".join(blank_word)== word:
        print("Congratulations")
        flag = False
    else:
        fgallows = f'''
        |--------
        |   {copy_of_part[0]}
        |  {copy_of_part[2]}{copy_of_part[1]}{copy_of_part[3]}
        |  {copy_of_part[4]} {copy_of_part[5]}
        '''
        print(fgallows)
        print("".join(blank_word))

        print(f'Guess: {", ".join(guess_list)}')
        print(f'Lives used: {counter}/6')
        guess = input("Choose a letter: ")
        if guess in guess_list:
            continue
        elif guess in word:
            for index, letter in enumerate(word):
                if guess == letter:
                    blank_word[index] = guess
                
        else:
            copy_of_part[counter]=body_parts[counter]
            counter += 1
            guess_list.append(guess)
       
    