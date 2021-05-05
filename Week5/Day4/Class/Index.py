import json 
import random

dic = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

jason_file = 'file.json'

with open(jason_file, 'w') as file_obj:
    json.dump(dic, file_obj)


with open(jason_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family["children"][0])

for child in my_family["children"]:
    # my_family["children"]({"Favorite colour": "green"})
    print(child)

print(my_family)