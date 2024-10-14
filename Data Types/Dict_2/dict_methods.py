# silly_animals = {
#     "duck" : "Quack",
#     "cat" : "Meow",
#     "dog" : "Woof",
#     "cow" : "Moo",
#     "pig" : "oink",
# }

# print(silly_animals)

# new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
# print(new_dict)

# weird_food_pairs = {
#     "Peanut Butter" : "Pickles",
#     "Pizza" : "Pineapple",
#     "Ice Cream" : "Ketchup",
#     "Fries" : "Chocolate Sauce",
#     "Butter Milk" : "Hershey's Chocolate Syrup",
#     "Marie Gold Biscuit" : "Lemon Juice",
# }

# print(weird_food_pairs.get("Marie Gold Biscoot", "Chai Latte"))

# print(weird_food_pairs.items())

# k = list(weird_food_pairs.keys())
# v = list(weird_food_pairs.values())
# print(k, v, sep='\n')

strange_inventions = {
    "Cat Translator" : "translates meows to human language",
    "Self-tying Shoes" : "Shoes that tie themselves",
    "Invisible Umbrella" : "Protect rain without blocking view",
    "Teleportation Toaster" : "Toasts bread and teleports is to your plate",
}

# print(strange_inventions.pop("Invisible Umbrella 2.0", "No such key present!"))

# for k, v in strange_inventions.items():
#     print(f"{k} : {v}", end='\n')

# k, v = strange_inventions.popitem();
# print(k, v, sep=", ")

# print(strange_inventions.setdefault("abcd", "xyz"))

# print(strange_inventions.update({"abcdxyz" : None}))

print(strange_inventions)



######################################################################
# 1. Check if a Given Key Already Exists in Dictionary
# -> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

# D1 = {'first_name' : 'Dhairya', 'age' : 20, 'height' : 5.5 , 'job' : 'Developer', 'company': 'Amazon'}