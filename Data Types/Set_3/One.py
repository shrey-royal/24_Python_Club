'''
set - A set is an unordered collections of items, every element should be unique(no duplicates) and mutable means we can change it.

set is mutable(changeable), unordered(no index), no duplicates allowed
syntax -: 
mySet = {1, 2, 3, ..., n}
'''

# mySet = {}  # dictionary  -> we can't define set like this
# mySet = set()
# mySet = {2345, 45, 123, 345456, 12123, 213}
# print(mySet)

# basics of set
# stores multiple data types
# mySet = {1, 2, 3, "Python", 2.3, 'j'}
# print(mySet)

# set can't have duplicates
# mySet = {11, 23, 11, 34, 11, 22}
# print(mySet)

# myList = ['veggies', 'fruits', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'fruits', 'chocolates', 'fruits']
# print(set(myList))


# Methods of set
# skills = {'Eating', 'Python Programming', 'Databases', 'Software design', 'Networking'}

# skills.add('Critical Thinking')
# print(skills)

# skills.clear()
# newSetofSkills = skills.copy()
# print(skills, newSetofSkills, sep='\n')

# skills.discard('Databases')
# print(skills)

mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}

# print(mySet.difference(dummy_set))
# print(mySet - dummy_set)
# mySet.difference_update(dummy_set)    # update the set values

# print(mySet.intersection(dummy_set))
# mySet.intersection_update(dummy_set)
# print(new_set.issubset(mySet))

# print({1, 2, 3}.isdisjoint({23, 22, 4}))
# print(mySet.isdisjoint(disjoint_set))
# print(mySet.pop())
# print(mySet.remove(45))
# print(mySet.symmetric_difference(dummy_set))
# mySet.symmetric_difference_update(dummy_set)
# mySet.update((34, 89))
# print({1, 2}.union({3, 4}))

# del mySet, dummy_set, disjoint_set, new_set

print(mySet)