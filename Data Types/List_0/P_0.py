# Write a Python program to sum all the items in a list.

# numbers = [1, 2, -8]
numbers = []
sum = 0

size = int(input("Enter the size of the list: "))

for i in range(size):
    numbers.append(int(input(F"Enter element {i}: ")))

for i in numbers:
    sum += i

print(f"Sum all the items in the list is {sum}.")

# Homework
# In all the following tasks take input from user
# 1. Write a Python program to sum all Positive the numbers in a list.
# 2. Write a Python program to sum all Negative numbers in a list.
# 3. Write a Python program to sum all Even numbers in a list.
# 4. Write a Python program to sum all Odd numbers in a list.