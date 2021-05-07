from anagram_checker import Anagram_checker

print(f'''

********************************
*                              *
*       ANAGRAM CHECKER        *
*       ****************       *
*       Enter a word or        *
*        type Q to quit        *
*                              *      
********************************
'''
)
ui = input()

flag = True
while flag:
    if ui == "Q":
        exit()

    else:
        for l in ui:
            if l.isnumeric() ==True:
                print("Please try again:")
                ui = input()
            elif len(ui.split())>1:
                print(len(ui.split()))
                print("Please try again:")
                ui = input()
            else:
                ui = ui.strip()
                flag = False




user_input = Anagram_checker(ui)
valid = user_input.is_valid_word()
anagrams = user_input.get_anagrams()

uiu= ui.upper()

print(type(valid))
if valid == True:
    print(f'Your word: "{uiu}"\nis a valid english word')
    if len(anagrams)>0:
        print(f'Anagrams for your word: {", ".join(anagrams)}.')
    else:
        print(f'{uiu} has no anagrams.')
else:
    print(f'The word "{uiu}" is invalid')
