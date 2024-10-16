# frozen set - immutable and constant
# once it is declared then it can't be changed

# set1 = frozenset({1, 23, 56, 78, 34, 89, 234})
# print(set1)
# print(type(set1))

# name = frozenset({'P', 'r', 'e', 'm'})
# print(name)

# s1 = {'P', 'r', 'e', 'm'}

# print(s1)

fs = frozenset([1, 2, 3, 4, 5])
fs_union = fs.union([4, 5, 6, 7])
fs_intersection = fs.intersection([2, 3, 4, 5])

print(fs_union)
print(fs_intersection)