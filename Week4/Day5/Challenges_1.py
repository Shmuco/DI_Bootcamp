# # Ex 1
# # Write a script that inserts an item at a defined index in a list.

# l1=[1, 2, 3, 4, 5, 6]
# print(l1)
# l1.insert(2, 6)
# print(l1)

# # Ex 2 
# # Write a script that counts the number of spaces in a string.

# string = input("Enter a string: ")
# print(string.count(" "))


# # Ex 3 

# string = input("Enter a string: ")

# upper_counter = 0
# for i in string:
#     if i.isupper():
#         upper_counter+=1
# print(upper_counter)

# string = input("Enter a string: ")

# lower_counter = 0
# for i in string:
#     if i.islower():
#         lower_counter+=1
# print(lower_counter)


# # Ex 4 
# # Write a function to find the sum of an array without using the built in function:
# def my_sum(number):
#     total = 0
#     for i in number:
#         total+= i
#     return total


# print(my_sum([1,5,4,2]))

# # Ex 5
# # Write a function to find the max number in a list

# def find_max(numbers):
#     max = numbers[0]
#     for i in numbers:
#         if i > max:
#             max = i
#     return max

# print(find_max([0,1,3,50]))


# # Ex 6
# # Write a function that returns factorial of a number
# def factorial(number):
#     start = 0
#     number_list = []
#     while start != number:
#         start+=1
#         number_list.append(start)
#         print(start)
#         print(number_list)
    
#     factorial = 1
#     for i in number_list:
#         factorial= factorial*i
#     return factorial

        

# print(factorial(4))


# # Ex 7

# def list_count(list,item):
#     counter = 0
#     for i in list:
#         if i == item:
#             counter+=1
#     return counter

# print(list_count(['a','a','t','o'],'a'))

# Ex 8 

# # # Ex 9

# def is_mono(list):
#     is_mono = False
#     if list == sorted(list):
#         is_mono = True
#     elif list == sorted(list,key=None,reverse=True):
#         is_mono = True
#     return is_mono

# print(is_mono([7,6,5,5,2,0]))

# print(is_mono([2,3,3,3]))
# print(is_mono([1,2,0,4]))