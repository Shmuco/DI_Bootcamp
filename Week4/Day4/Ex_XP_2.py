# # Ex 7
# from datetime import date
# age=0


# def get_age(year, month, day):
#     cdate = date.today()
#     brithdate = date(year,month,day)
#     diff = cdate - brithdate
#     age = int(diff.days/365)
#     return age
 

# def can_retire(gender,date_of_birth):
#     dob = date_of_birth.split("/")
#     year=int(dob[0])
#     month=int(dob[1])
#     day=int(dob[2])
    

#     age=get_age(year, month, day)

#     if gender =="m":
#         if age >= 67:
#             print("You can Retire.")
#         else:
#              print("You cant Retire.")
#     elif gender == "f":
#         if age >= 62:
#              print("You can Retire.")
#         else:
#              print("You cant Retire.")


# # date_of_birth = 
# # gender= input("Whats your gender? (m or f) ")
# can_retire(input("Whats your gender? (m or f) "),input("Enter date of birth (yyyy/mm/dd): ")) 


# # Ex 8
# def sequence_calc(y):
#     X=int(y)
#     XX=int(y+y)
#     XXX=int(y+y+y)
#     XXXX=int(y+y+y+y)

#     result = X+XX+XXX+XXXX
#     print(f'{result}({X}+{XX}+{XXX}+{XXXX})')

# sequence_calc(input("Enter a number: "))
