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

n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i

print(f"Sum of {n} natural numbers is {sum}")

# Product of n numbers
# sum of all even numbers upto n
# print x numbers which are divisible by n

# Gujarat Hotel -> Hotel Menu using match case (run until user exits the program) -> atleast 10 dish with price calculation and quantity