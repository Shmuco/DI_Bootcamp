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

# # Ex 8 
# import math
# def norm(list):
#     sum = 0 

#     for i in list:
#         sq = i*i
#         sum += sq
#     return math.sqrt(sum)
# print(norm([1,2,2]))

# # Ex 9

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


# # Ex 10

# def longets_word(list):
#     longest = ""
#     for i in list:
#         if len(i)>len(longest):
#             longest = i
#     return longest


# print(longets_word(['hello', 'world', 'hellllllllooooo']))


# # Ex 11

# def sort(list):
#     integers = []
#     strings = []

#     for i in list:
#         try:
#             i.isalpha()
#             strings.append(i)
#         except:
#             integers.append(i)
        
#     return integers, strings

# print(sort([0,2,4,"hello","world"]))



# # Ex 12

# def is_palindrome(x):
#   y = x[::-1]
#   if y == x:
#     return True
#   else:
#     return False


# print(is_palindrome('radar'))
# print(is_palindrome('John'))


# # Ex 13

# def sum_over_k(sentance,k):
#     total = 0
#     sen_li = sentance.split()
#     print(sen_li)
#     for i in sen_li:
#         if len(i)>k:
#             total+=1
        
#     return total

# print(sum_over_k('Do or do not there is no try',2))

# # Ex 14

# def dict_avg(dict):
#     sum =0
#     for i in dict:
#         sum += dict[i]
#     return sum/len(dict)

# print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))


# # Ex 15

# def common_div(num1,num2):
#     all_devisors =[]
#     commons=[]
#     for i in range(1,num1+1):
#         if num1%i ==0:
#             all_devisors.append(i)
#     for i in range(1,num2+1):
#         if num2%i ==0:
#             all_devisors.append(i)
#     for i in all_devisors:
#         if all_devisors.count(i)>1:
#             commons.append(i)
#     return set(commons)


# print(common_div(10,20))


# # Ex 16

# def is_prime(num):
#     divisables = []

#     for i in range(1,num+1):
#         if num%i ==0:
#             divisables.append(i)
#     if len(divisables) ==2:
#         return True
#     else: return False

# print(is_prime(25))


# # Ex 17

# def weird_print(list):
#     div_2 = []
#     for i in list:
#         if i%2 == 0:
#             if i not in div_2:
#                 div_2.append(i)
#     return div_2

# print(weird_print([1,2,2,3,4,5]))


# # Ex 18
# def type_count(**args):
#     int_count = 0
#     str_count = 0
#     float_count = 0
#     bool_count = 0

#     for keyword,i in args.items():
#         if type(i) ==int:
#             int_count += 1
#         elif type(i) == float:
#             float_count += 1
#         elif type(i) == bool:
#             bool_count += 1
#         elif type(i) == str:
#             str_count += 1

#     return f'int: {int_count}, str: {str_count}, folat: {float_count}, bool: {bool_count}'

# print(type_count(a=1,b='string',c=1.0,d=True,e=False))

# # Ex 19

# def my_split(string, splitter):
#     words = []
#     current_indx = 0

#     for i in string:
#         print(i)
#         if i == splitter:

#             words.append(string[current_indx:string.index(splitter,current_indx)])
#             current_indx= string.index(splitter,current_indx)+1
#         elif string.index(i,current_indx)==len(string)-1:
#             words.append(string[current_indx:])

#     return words

# print(my_split('hello world how are you?'," "))

# # Ex 20

# def hide_text(text):
#     return '*'*len(text)

# print(hide_text(input('Enter text: ')))

