# # Ex 1

# # Create a class called Family and implement the following attributes:

# # members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# # last_name : (string)

# class family():
#     def __init__(self, members, last_name):
#         self.members = members
#         self.last_name = last_name

# # is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not
#     def is_18(self, name):
#         for people in self.members:
#             if people.get("name") == name:
#                 if people.get("age")>= 18:
#                     print("True")
#                 else:
#                     print("False")


# # a method that prints all the members of the family.
#     def family_members(self):
#         for people in self.members:
#             print(people.get("name"))


# # born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print("Congratulations on the new addition!!")



# hickinbottom = family([
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ], "Hickinbottom")

# print(type(hickinbottom.members[0]))
# hickinbottom.is_18("Michael")
# hickinbottom.family_members()
# hickinbottom.born(name="james", age=0, gender="male")




# # Ex 2
# # 1. Create a class called TheIncredibles. This class should inherit from the Family class
# #     - This is no random family they are an incredible family, therefore we need to 
# #     add the following keys to our dictionaries: power and incredible_name.

# class the_incredibles(family):


# # - Add a method called use_power, this method should print the power of a member if they are over 18 years old. 
# #   If not raise an exception (look up exceptions) which stated they are not over 18 years old.

#     def use_power(self, name):
#         for people in self.members:
#             if people.get("name") == name:
#                 if people.get("age")>= 18:
#                     print(people.get("power"))
#                 else:
#                     print("Under 18")

# # Add a method called incredible_presentation which presents the family members with their incredible names and powers.
#     def incredible_presentation(self):
#         for people in self.members:
#             print(f'{people.get("incredible_name")} : {people.get("power")}')
   
   
#     def normal_presentation(self):
#         for people in self.members:
#             print(f'{people.get("name")} : {people.get("age")}')
          

# # 2. Look up the names of The Incredibles characters on Google and build the family \
# # (if you can’t find the correct information just improvise).
# TheIncredibles = the_incredibles([
#     {'name': 'Bob', 'age': 40, 'gender': 'Male', 'is_child': False, 'power': "Strength",'incredible_name':'Mr Incredible', },
#     {'name': 'Helen', 'age': 38, 'gender': 'female', 'is_child': False, 'power':'Elastic','incredible_name':'Elastgirl', },
#     {'name': 'Dashiell', 'age': 10, 'gender': 'Male', 'is_child': True, 'power':'Super Speed','incredible_name':'Dash', },
#     {'name': 'Violet', 'age': 14, 'gender': 'Female', 'is_child': True, 'power':'Invisibility' ,'incredible_name':'Violet', },
    
# ], "The Incredibles")

# # 3. Print their normal presentation and their incredible presentation.
# TheIncredibles.normal_presentation()
# TheIncredibles.incredible_presentation()

# # 4. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# TheIncredibles.born(name="Baby Jack", age="0", gender="Male", is_child=True, power="Unknown Power", incredible_name="TBC")

# # 5. Print both presentations again. Check that Baby Jack is born and that his power is showing when 
# # using the incredible representation.
# TheIncredibles.normal_presentation()
# TheIncredibles.incredible_presentation()


# TheIncredibles.use_power("Violet")
