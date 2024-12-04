# Anoymous Functions in Python

# lambda parameters: expression => syntax

# variable = lambda parameter: expression         => function definition
# variable(parameter) => function calling

# Normal function
# def square(x):
#     return x**2
# ans = square(4)

# lambda function
# square = lambda x: x**2
# ans = square(4)

# print(ans)

# lambda function with multiple parameters
# add = lambda a=23, b=34: a+b
# print(add(2, 3))
# print(add())

# lambda function without any parameters
# greet = lambda : "Hello!"
# print(greet())

########################################################################

import random

pairs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]
print(pairs)

# map(function, iterable) -> used to process data (work with any function who returns some data)

# Normal
# def map_fun(elem):
#     return elem[0] * elem[1]

# mappedList = list(map(map_fun, pairs))
# print(mappedList)

# //lambda
# mappedList = list(map(lambda elem: elem[0] * elem[1], pairs))
# print(mappedList)
##########################################################################

# filter(function, iterable) -> used with boolean function

# //Normal
# def filter_func(elem):
#     return elem[0] > 5

# filteredList = list(filter(filter_func, pairs))
# print(filteredList)

# //Lambda
# filteredList = list(filter(lambda elem: elem[0] > 5, pairs))
# print(filteredList)

# -----------------------------------------------------------------------------

# // sorted()
# myList = [67, 56, 43, 23, 435, 456, 67, 3, 23, 23, 2]
# sortedList = list(filter(lambda x: x%2 == 0, sorted(myList)))
# sortedList = sorted(myList, key=lambda x: -x)

# sortedList = sorted(pairs, key=lambda x: x[0])
# print(sortedList)

# fruits = [(1, '🍉'), (2, '🍒'), (3, '🍎'), (4, '🍅')]
# sortedFruits = sorted(fruits, key=lambda x: x[0])
# print(sortedFruits)


# num_list = [23, 345, 234, 56, 23, 45, 567]
# s1 = sorted(num_list, key=lambda x: x)
# s2 = sorted(num_list, key=lambda x: x%10)
# print(s1)
# print(s2)

# -----------------------------------------------------------------------------

# //reduce(function, sequence, initializer(optional)): apply function on all elems of sequence
from functools import reduce

def max(a, b):
    return a if a>b else b

# myList = [211, 4, 6, 8, 10, 11]
# print(reduce(max, myList))
# pairs = [random.randint(0, 10) for _ in range(5)]
# print(pairs)
# print(reduce(lambda x, y: x*y, pairs))

# any (returns true if any data is True), all (all the data must be True)
# print (any([False, False, False, False]))

# Here the method will short-circuit at the second item (True) and will return True.
# print (any([False, True, False, False]))

# Here the method will short-circuit at the first (True) and will return True.
# print (any([True, False, False, False]))

print(all([False, False, False, False]))
print(all([False, False, False, True]))
print(all([True, True, True, True]))
print(all([True, False, True, True]))