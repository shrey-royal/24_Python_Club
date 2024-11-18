"""
Functions --> Assistants

=> A Function is a named code block that performs a job or return a value

syntax:
def function_name(argument/s):
    //body of the function

"""
# import datetime as dt

# def greet():
#     now = dt.datetime.now()
#     current_hour = now.hour

#     if 5 <= current_hour < 12:
#         greeting = "Good morning!"
#     elif 12 <= current_hour < 17:
#         greeting = "Good afternoon!"
#     elif 17 <= current_hour < 21:
#         greeting = "Good evening!"
#     else:
#         greeting = "Good night!"

#     return greeting

# print(greet())
######################################################################

# Doc Strings (Documentation String)

# def custom_print(message: str=""):    # default parameter is used
#     """This is Doc String"""
#     print(message)

# custom_print()
######################################################################

# def greet(name):
#     print(f'Hi, {name}')

# naam = input("Enter your name: ")
# greet(naam)
######################################################################

# def addition(a, b):
#     return a+b

# print(addition(2, 3))

# Default Parameters

# def addition(a, b=0):       # Default parameter is used
#     print(f"{a} + {b} = {a+b}")

# addition(34, 2)
# addition(3)
######################################################################

# smol praktis
# Problem Statement: Create a function 'greet_user' that takes two parameters: 'name' (a string) and 'greeting' (a string). The greeting parameter should have a default value of "Hello". The function should print a message in the format: "greeting, name!". If no greeting is provided, it should use the default value.

def addition(a: int | None = 0, b = 0):
    print(f"{a} + {b} = {a+b}")

addition(b=23)