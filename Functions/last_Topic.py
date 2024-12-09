# *args -> tuple

# def add(*args):
#     return sum(args)

# def sub(*args):
#     res = 0
#     for i in args:
#         res -= i
#     return res

# print(sub(2, 3, 5, 6, 78, 4, 3, 5, 7))
##################################################
# **kwargs -> keyword arguments

def numbers(**nums):
    # print(type(nums))
    print(nums)

# numbers(a=1, b=2, c=23, d=12)

myDict = {'a': "Apple", 'b': "Banana", 'c': "Carrot"}
numbers(**myDict)