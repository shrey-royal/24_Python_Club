"""
Tuple -> Immutable Sequence

syntax:
    tuple() -> represented by ()

Changeable? -> False
Duplicates Allowed? -> True

"""

myTuple = (3, 5, 2, 56, 8, 4, 3, 12, 5, 78, "2", ["2", 34, 2, 2])
# print(myTuple, type(myTuple), id(myTuple))

# print("Index: ", myTuple.index('2', 6, 12))
# print("Len: ", len(myTuple))
# print("Count: ", myTuple.count(2))

# myTuple[11][0] = 23

# print(myTuple)
print(myTuple[3])

'''
# smol practice
WAP to get 4th element from the right and from the left.
Sample Input:
    myTuple = (3, 5, 2, 56, 8, 4, 3, 12, 5, 78, "2", ["2", 34, 2, 2])
Sample Output:
    56, 5

'''



"""
2. Store Inventory System
Create a tuple to store inventory items, where each item is a tuple with (item_id, name, quantity, price). Write a program to update the quantity of a given item and print the updated inventory as a tuple.

Sample Input:

inventory = (
    (101, 'Apples', 50, 0.5),
    (102, 'Bananas', 30, 0.2),
    (103, 'Cherries', 20, 1.5)
)
item_id_to_update = 102
new_quantity = 45


Sample Output:
(
    (101, 'Apples', 50, 0.5), 
    (102, 'Bananas', 45, 0.2), 
    (103, 'Cherries', 20, 1.5)
)
"""