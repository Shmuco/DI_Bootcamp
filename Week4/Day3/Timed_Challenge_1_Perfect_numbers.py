user_num = int(input("Enter a number to see if it perfect: "))
divisable = []

for i in range(1,user_num):
    if (user_num % i == 0):
        divisable.append(i)
if sum(divisable) == user_num:
    print("True")
else: print("False") 
