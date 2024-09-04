'''
List Comprehension: [expression for item in iterable if condition]

for else -> [expression_1 if condition else expression_2 for item in iterable]

'''

# nums = [num**2 for num in range(11)]
# print(nums)

# even_squares = [num**2 for num in range(11) if (num % 2) == 0]
# print(even_squares)

# basic = [i for i in range(11)]
# even_squares = [num**2 if (num % 2) == 0 else num**3 for num in range(11)]
# for i in range(11):
#     print(f"{basic[i]} -> {even_squares[i]}")

new_list = [int(i**0.5) for i in [num**2 for num in range(11) if (num % 2) == 0]]
print(new_list)