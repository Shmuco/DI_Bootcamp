# #Ex 1
# import math
# nums = input('Enter numbers seperated by commas: ')

# nums_list = nums.split(",")
# print(nums_list)

# for number in nums_list:
#     x = math.sqrt((2*50*int(number))/30)
#     print(x)

# #Ex 2

# li = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
# li2 =[]
# li_50 =[]
# li_10 =[]
# li_sq =[]
# li_nodub =[]
# print(li)
# print(sorted(li))
# sum_li = sum(li)
# print(sum_li)

# li2.append(li[0])
# li2.append(li[-1])
# print(li2)

# for i in li:
#     if i > 50:
#         li_50.append(i)
# print(li_50)

# for i in li:
#     if i < 10:
#         li_10.append(i)
# print(li_10)

# for i in li:
#     li_sq.append(i*i)
# print(li_sq)

# li_set = set(li)
# for i in li_set:
#     li_nodub.append(i)
# print(li_nodub)
# print(len(li_nodub))

# average = sum_li/len(li)
# print(f'Average: {average}')

# print(max(li))
# print(min(li))


# # Ex 3
# import string

# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et mauris lacus. Proin interdum, diam suscipit congue pretium, velit velit tristique turpis, eu tristique augue nibh in nisl. Donec dui sapien, laoreet a risus vitae, bibendum sollicitudin eros. Duis quis justo et urna sollicitudin tempus pellentesque ac quam. Fusce tempus arcu ac augue mollis imperdiet. Curabitur quis tincidunt lorem. Donec quis eros vitae ex venenatis posuere ac id massa. Morbi non nibh vel lorem hendrerit mattis ac a nisi. Proin accumsan lacus at accumsan sollicitudin. Duis congue faucibus ante, molestie porta elit imperdiet id. Vestibulum commodo turpis nunc. Sed molestie tempor tincidunt. Donec eu scelerisque felis. Cras sit amet scelerisque mauris, at mattis leo. Donec cursus risus et iaculis ornare. Integer tempor porta sollicitudin. Nam mattis tincidunt mi, ac tincidunt diam porttitor eu. Pellentesque viverra, neque ac lobortis suscipit, ante magna malesuada nisl, vel maximus purus quam et dui. Morbi mattis felis eu sem volutpat, eu sodales justo semper. Donec a urna tortor. Donec sagittis turpis sem, vel faucibus nunc viverra id. Curabitur sit amet elit enim."
# text_nopunc =""
# print(f'There are {len(text)} in the text.')

# sen = text.split('. ')
# print(f'There are {len(sen)} sentances in the text.')

# words = text.split(" ")
# print(f'There are {len(words)} words in the text.')


# for i in text:
#     if i not in string.punctuation:
#         text_nopunc+=i.lower()

# text_nopunc_list = text_nopunc.split(" ")

# unique_counter = 0
# for i in text_nopunc_list:
#     if text_nopunc_list.count(i)==1:
#         print(i)
#         unique_counter+=1


# print(f'There are {unique_counter} unique words in the text')

# counter = 0
# for i in text:
#     if i != " ":
#         counter +=1

# print(f'There are {counter} non white-space charecters in the list')

# sen_len =[]
# for i in sen:
#     x = i.split(" ")
#     sen_len.append(len(x))

# average = sum(sen_len)/len(sen_len)
# print(f'There are average of {average} words in each sentance.')

# non_unique_counter = 0
# for i in text_nopunc_list:
#     if text_nopunc_list.count(i)>1:
#         non_unique_counter+=1


# print(f'There are {non_unique_counter} non unique words in the text')

# # Ex 3

# str = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'

# str_ls = str.split(' ')
# str_set = set(str_ls)

# for i in str_set:
#     print(f'{i}: {str_ls.count(i)}')

