nums = (98, 29, 67, 23, 20, 51, 32, 15, 37, 40)
# print(nums)

# n1, n2, n3 = 1, 2, 3 # (n1 = 1, n2 = 2, n3 = 3)
# print(n1, n2, n3)

# n1 = 1, 2, 3    # packing - default type -> tuple
# print(n1)

# print("unpack-1: ", end='')
# n1, n2, *n3 = nums  # * will return packed data in list form
# n1, *n2, n3 = nums
# *n1, n2, n3 = nums
# print(n1, n2, n3)

print("unpack-2: ", end='')
n, *n2, n3 = 23, nums, 45

print(n, n2, n3)