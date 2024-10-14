from pprint import pprint

# Dictionary - Ordered, Mutable and Unique (no duplicates) collection of pairs containing key and values
# (Keys must be unique and value may contain duplicates)

# myDict = {
#     "key":"value",
# }
# myDict = dict()

# myDict = {
#     "name" : "Royal",
#     "address" : "gandhinagar",
#     "students" : {
#         "prem" : (7, "Full Stack Developer", "1.5 Cr"),
#         "ramesh" : (24, "Manager", "3 Cr"),
#     },
# }

# pprint(myDict)
#####################################################################

# Dhiraj Sir arranges Royal Jamanvaar for 1 day

# employee_choice = {
#     "Dhiraj Sir" : {"Breakfast" : "Dosa", "Lunch" : "Punjabi", "Dinner" : "khichdi-kadhi"},
#     "Zafar Sir" : {"Breakfast" : ['Fafda', 'Jalebi'], "Lunch" : "Kathiyawadi", "Dinner" : "Gujarati"},
#     "Shrey Sir" : {"Breakfast" : "Fruits", "Lunch" : "South Indian", "Dinner" : "Maggie"},
#     "Madhusudan Sir" : {"Breakfast" : "Solid Masti", "Lunch" : "Pizza", "Dinner" : "Solid Masti"},
#     "Mohak Sir" : {"Breakfast" : ["Saurashtra Ganthiya", "Jalebi"], "Lunch" : "Italian", "Dinner" : "Mexican"},
# }

# Accessing the data
# pprint(employee_choice)

# using square bracket notation (dict[key])
# print(employee_choice["Madhusudan Sir"])
# print(employee_choice["Zafar Sir"])
# print(employee_choice["Krutarth Sir"])  # KeyError

# get() method  # returns None if key not found
# print(employee_choice.get("Dhiraj Sir"))
# print(employee_choice.get("Krutarth Sir"))

# choice = input("Enter the name: ")
# print(employee_choice.get(choice, employee_choice["Dhiraj Sir"]))

#########################################################################

# add new pairs of data

person = {
    'fname' : 'Cynthia',
    'lname' : 'Wright',
    'age' : 24,
    'favorite_colors' : ['blue', 'green'],
    'ssn' : "123-44-7678",
    'active' : True,
}

# person['active'] = False

# deleting a pair
# del person['age']
# pprint(person)

for k, v in person.items():
    print(f"{k} : {v}")