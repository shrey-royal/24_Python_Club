'''
Loop: Entry-Controlled Loop

1. for: fixed iteration
syntax:
    for iterator_var in iterable:
        # body

2. while: unfixed iteration
syntax:
    while condition:
        # body

'''

# range(start, stop-1, step) function

# for i in range(65, 91):
#     print(chr(i), end=' ')
###############################################

# for i in range(20):
#     print(i, end=' ')
###############################################

# user_input = int(input("Enter the number of iterations: "))

# for i in range(user_input):
#     print(i, end=' ')
###############################################

# while loop
# i=0
# while(i < 5):
#     print(i, end=' ')
#     i+=1

###############################################
# choice = 1
# while choice != 0:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 3: print("Good!")
#     elif choice == 0: break
#     else: print("Invalid Choice! Try Again")

###############################################
# while True:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 3: print("Good!")
#     elif choice == 0: break
#     else: print("Invalid Choice! Try Again")

###############################################

# Sum of n natural number

# n = int(input("Enter n: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i

# print(f"Sum of {n} natural numbers is {sum}")

# Product of n numbers
# sum of all even numbers upto n
# print x numbers which are divisible by n

# Gujarat Hotel -> Hotel Menu using match case (run until user exits the program) -> atleast 10 dish with price calculation and quantity
###############################################

# Write a program in Python to display n terms of natural numbers and their sum.
total = 0;
n = int(input("Enter n: "))

for i in range(1, n+1):
    print(f"{i}, ", end='')
    total += i

print(f"\nSum of {n} natural numbers is {total}")
"""
1. Write a program in Python to read 10 numbers from the keyboard and find their sum and average.
Test Data :
Input the 10 numbers :
Number-1 :2
...
Number-10 :2
Expected Output :
The sum of 10 no is : 55
The Average is : 5.500000

2. Write a program in Python to display the cube of the number up to an integer.
Test Data :
Input number of terms : 5
Expected Output :
Number is : 1 and cube of the 1 is :1
Number is : 2 and cube of the 2 is :8
Number is : 3 and cube of the 3 is :27
Number is : 4 and cube of the 4 is :64
Number is : 5 and cube of the 5 is :125

3. Write a program in Python to display the multiplication table for a given integer.
Test Data :
Input the number (Table to be calculated) : 15
Expected Output :
15 X 1 = 15
...
...
15 X 10 = 150

4. Write a Python program to display the n terms of odd natural numbers and their sum.
Test Data
Input number of terms : 10
Expected Output :
The odd numbers are :1 3 5 7 9 11 13 15 17 19
The Sum of odd Natural Number upto 10 terms : 100

5. Write a Python program to check whether a number is a palindrome or not.
Test Data :
Input a number: 121
Expected Output :
121 is a palindrome number.

"""