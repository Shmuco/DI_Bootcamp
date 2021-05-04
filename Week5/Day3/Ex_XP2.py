# Ex1
# Create a function that displays the current date.
# Hint : Use the datetime module.
# import datetime
# today = datetime.date.today()
# def date_today():
#     print (today)

# date_today()

# # Ex 2
# from datetime import datetime
# def now_jan():
#     jan= datetime(2022,1,1,0,)
#     diff = jan-datetime.now()
#     print (f'The 1st of January is in {diff}')
# now_jan()



# # Ex 3
# from datetime import date
# date_of_birth=input("Enter your birth date: (dd/mm/yyyy)")

# dob = date_of_birth.split("/")
# year=int(dob[2])
# month=int(dob[1])
# day=int(dob[0])

# cdate = date.today()
# brithdate = date(year,month,day)
# diff = cdate - brithdate
# age = diff.days*24*24

# print(f'you have been alive {age} minutes')


# # Ex 4
# from datetime import datetime
# def next_holiday():
#     shavuot= datetime(2021,5,9,0,)
#     diff = shavuot-datetime.now()
#     print (f'Shavuot is in {diff}')
# next_holiday()


# # Ex 5
# age_seconds = int(input("Enter your age in seconds: "))
# planet = input("Enter Planet: ")

# def earth_years(age_seconds):
#     age_years= age_seconds/60/60/24/365.25
#     return age_years

# if planet == "Earth":
#     print(earth_years(age_seconds))
# elif planet == "Mercury":
#     age = earth_years(age_seconds)*0.2408467
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Venus":
#     age = earth_years(age_seconds)*0.61519726
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Mars":
#     age = earth_years(age_seconds)*1.8808158
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Jupiter":
#     age = earth_years(age_seconds)*11.862615
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Saturn":
#     age = earth_years(age_seconds)*29.447498 
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Uranus":
#     age = earth_years(age_seconds)*84.016846
#     print(f'On {planet} you are {age} {planet}-years old')
# elif planet == "Neptune":
#     age = earth_years(age_seconds)*164.79132
#     print(f'On {planet} you are {age} {planet}-years old')
    
# # Exercise 6
# from faker import Faker
# fake = Faker()

# users=[]


# def add_user():
#     users.append({
#         "name":fake.name(),
#         "address":fake.address(),
#         "langage_code":fake.language_code(),
#     })

