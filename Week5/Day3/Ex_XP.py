# # # Ex 1 Instructions

# # Python has many built-in functions.
# # If you feel that you don’t know how to properly implement them take a look at the python documentation online.


# x = abs(1.90)
# # print("abs = "+abs.__doc__)
# # print("int = "+int.__doc__)
# # print("input = "+input.__doc__)e

# # 1. Write a program which prints some of python’s built-in functions such as abs(), int(), raw_input().


    


# a = abs(-7)
# b= int(4.5)
# c = input("Input something:")

# print(a)
# print(b)
# print(c)

# # 2. Create your own documentation explaining what your classes functionality is, you can do this by using 
# # the __doc__ dunder method take a look on google for help.

# class function:
#     def __init__(self, object):
#         self.object = object
    
#     def do_stuff(self):
#         '''prints the absolute and interger value of a number'''
#         print(abs(object))
#         print(int(object))
    

# print(function.do_stuff.__doc__)

# Ex 2

class Currency:
    def __init__(self, currency, amount):
        self.currency=currency
        self.amount=amount
    
    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        num = int(self.amount)
        return(num)
    
    def __repr__(self):
        return f'{self.amount} {self.currency}'
    
    def __add__(self, other):
        try:
            other.amount
            if other.currency != self.currency:
                return TypeError(f'Cannot add between currency {other.currency} and {self.currency}' )
            else:
                return self.amount + other.amount
        except:
            return self.amount + other
    def __iadd__(self,other):
        try:
            self.amount + other.amount
            return Currency(self.currency,self.amount)
        except:
            self.amount = self.amount+other
            return Currency(self.currency,self.amount)
     
            
        







c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)

print (type(c1.amount))
print(c1.amount)
print(str(c2))
print(int(c4))
print(repr(c4))
print(c1+c2)
print(c1+c4)
c1+=5
print(c1)
c1 += c2
print(c1)


