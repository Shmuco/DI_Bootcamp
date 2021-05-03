# class door():
#     def __init__(self, is_opened):
#        self.is_opened = is_opened
#     def open_door(self):
#         print('The door is open')
#         self.is_opened = True
#     def close_door(self):
#         print('The door is closed')
#         self.is_opened = False


# class BlockedDoor (door):
#     def open_door(self):
#         print('The door is blocked and cannot be opend or closed')
    
    
#     def close_door(self):
#         self.open()


sum = 0
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
# for i in my_list:
#     if type(i) is int:
#         sum += i
# print(sum)

def sum_meliciouts(given_list):
    total = 0 
    for num in given_list:
        try:
            total += int(num)
        except:
            print(f'"{num}" is not a number')
    print(total)
sum_meliciouts(my_list)