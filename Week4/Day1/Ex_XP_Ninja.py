# # Ex 4 
# # 1. Use python to find out how many characters are in the following text, use a single line of 
# # code (beyond the establishment of your my_text variable)


# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# print(len(my_text))

# # Ex 5
# 1. Keep asking the user to input the longest sentence they can without the character “A”.
# 2. Each time a user successfully sets a new longest sentence, print a congratulations message.


word=input("Enter a word: ")
while word != "quit":
    new_word=input("Try aging. Enter a word: ")
    if len(new_word)>len(word) and "a" in new_word ==False:
        word = new_word
        print("Congratulations")
  