# # Ex 1

# # Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# # For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

# sentance = input("Enter a sentance: ")
# sentance = sentance.split()
# longest= 0
# star="*"
# for word in sentance:
#     length = len(word)
#     if length > longest:
#         longest = length

# print(star*(longest+5))
# for word in sentance:
#     print(f'{star} {word} {" "*(longest-len(word))} {star}')
# print(star*(longest+5))

# # Ex 2
# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)