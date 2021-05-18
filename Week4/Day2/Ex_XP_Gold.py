# Ex 1

# li1 = [1,2,3,4,5]
# li2 = [6,7,8,9]

# for i in li2:
#     li1.append(i)

# print(li1)

# joint_ist = [*li1,*li2]

# print (joint_ist)


# Ex 2

# number = []
# number.append(input("Input the 1st number: "))
# number.append(input("Input the 2nd number: "))
# number.append(input("Input the 3rd number: "))

# print(f'The greatest number is: {max(number)}')

## Ex 3 
# string ='abcdefghijklmnopqrstuvwxyz'
# vowels = ['a','e','i','o','u']
# for i in string:
#     if i in vowels:
#         print('Vowel')
#     else:
#         print('Constanet')

# # Ex 4

# name = input("Whats your name? ")
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# if name in names:
#     print(names.index(name))
# else:
#     print('Name not in list.')


# # Ex 5
# word_list=[]
# count= 0 
# while count<7:
#     word_list.append(input('Enter a word: '))
#     count +=1
# letter = input("Enter a letter: ")
# for word in word_list:
#     if letter in word:
#         print(f'Index of "{letter}" in "{word}" is {word.index(letter)}')
#     else:
#         print(f'Sorry "{letter}" is not in "{word}"')


# # Ex 6
# import time 
# number_list=[]

# for number in range(0,10000001):
#     number_list.append(number)

# print(min(number_list))
# print(max(number_list))
# time_start = time.perf_counter()

# addition = sum(number_list)
# time_end = time.perf_counter()
# print(addition)
# print(time_end-time_start)


# # Ex 7
# string = input("Enter a list of numbers sperated by a comma: ")
# li = string.split(",")
# tup = tuple(li)

# print(li)
# print(tup)


# Ex 8
import random

flag = True
win = 0 
loss = 0 
while flag is True:
    user_num = input("Enter a number between 0-9 or q to quit:")
    comp_num = random.randint(0,9)
    if user_num =='q':
        flag = False
    elif int(user_num) == comp_num:
        win+=1
        print('Winner!!')
        print(comp_num)
    else:
        loss+=1
        print(comp_num)
        print('Looser')
    

print(f'Wins: {win}')
print(f'Losses: {loss}')


