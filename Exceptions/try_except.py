"""
try:
    # code that may occur exception
except:
    # code that handle exception
else:
    # code that executes when no exception occured
finally:
    # code that clean up
    # code here will be executed everytime doesn't matter whether the exception occurs or not
"""
"""
print("Before Exception")

try:
    # print(12/0) # Exception
    a = int(input("Enter int: "))   # ValueError 
except (ValueError, ZeroDivisionError) as error:
    print(f"Exception Occured: {error}")
else:
    print(f"a = {a}")
finally:
    print("YAY!")

print("After Exception")

"""

"""
try:
    a, b = int(input("Enter a: ")), int(input("Enter b: "))
    print(a/b)
except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")
# except ValueError:
#     print("Please enter a number!")
# except ZeroDivisionError:
#     print("Infinite")
"""

"""
def get_integer_value(prompt):
    try:
        return int(input(prompt))
    except ValueError as e:
        print("Error: Invalid input, input a valid integer.")

print(get_integer_value("Scan int: "))
"""

# Throwing exception

a, b = int(input("Enter a: ")), int(input("Enter b: "))

if b == 0:
    raise ValueError("Denominator can't be zero!")
else:
    print(a/b)