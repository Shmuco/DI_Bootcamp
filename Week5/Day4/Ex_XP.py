# import random
# # Ex 1


# # 1 .Download this word list
# # 2. Save it in your development directory.
# # 3. Create a function called get_words_from_file.
# #    This function should read the file’s content and return the words as a collection.
# #    What is the correct data type to store the words?
# word_list = []


# def get_words_from_file(filename):
#     for line in open(filename):
#         line = line.strip()
#         word_list.append(line)


# # 4. Create another function called get_random_sentence which takes a single parameter called length.
# #     The length parameter will be used to determine how many words the sentence should have.
# #     The function should:
# #     - use the words list to get your random words.
# #     - the amount of words should be the value of the length parameter.

# def get_random_sentence(length):
#     i = 0
#     random_sentance = []
#     get_words_from_file("sowpods.txt")
#     while length > i:
#         ran_num = random.randrange(0, len(word_list))
#         word = word_list[ran_num]
#         random_sentance.append(word)
#         # print(word)
#         i += 1
# # 5. Take the random words and create a sentence (using a python method), the sentence should be lower case.
#     final_sentence = " ".join(random_sentance).lower()
#     # print(random_sentance)
#     print(f'{final_sentence}.')

# # 6. Create a function called main which will:
#     # - Print a message explaining what the program does.
#     # - Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
#     #   Validate your data and test your validation
#     # - If the user inputs incorrect data, print an error message and end the program.
#     # - If the user inputs correct data, run your code.
# def main():
#     sen_len = input(
#         "Type in a number and i will generate a a random sentance with the many words.\nInput a number between 2-20: ")

#     sen_len_int = int(sen_len)
#     if 2 <= sen_len_int <= 20:
#         get_random_sentence(sen_len_int)
#     else:
#         print("I can only take integers between 2-20")


# main()


# # Ex 2

# import json
# sampleJson = {"company": {"employee": {"name": "emma","payable": {"salary": 7000,"bonus": 800}}}}

# # 1. Access the nested “salary” key from the JSON-string above.
# print(sampleJson["company"]["employee"]["payable"]["salary"])

# # 2. Add a key called “birth_date” to the JSON-string at the same level as the “name” key.

# sampleJson["company"]["employee"]["birth_date"] = None
# print(sampleJson["company"]["employee"])

# # 3. Save the dictionary as JSON to a file.

# json_file = "jsonfile.json"

# with open(json_file,'w') as file_obj:
#     json.dump(sampleJson, file_obj)