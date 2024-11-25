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
filteredList = list(filter(lambda elem: elem[0] > 5, pairs))
print(filteredList)