from datetime import datetime, date

print("")
date_of_birth = datetime.strptime(input("Your date of birth (dd mm yyyy): "), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)
agestr=str(age)
num=agestr[-1]
num=int(num)


print(age)

print("         "+"i"*num)
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")
   