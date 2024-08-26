# Match Case (Switch Case)

print("1. Tea")
print("2. Coffee")
print("3. Milk")
choice = int(input("Enter your choice: "))
quantity = 0;
price = 0;

match(choice):
    case 1:
        print("-> Regular Tea - ₹10")
        print("-> Masala Tea - ₹15")
        print("-> Rajwadi Tea - ₹20")
        print("-> Milk Tea - ₹15")
        print("-> Green Tea - ₹20")
        choice = input("Enter your choice: ").casefold()
        
        match (choice):
            case "regular tea":
                quantity = int(input(f"How many {choice.title()} you want? -> "))
                print(f"Here is your Order -> {quantity} {choice.title()}.")
                price += quantity * 10
                
            case "masala tea":
                quantity = int(input(f"How many {choice.title()} you want? -> "))
                print(f"Here is your Order -> {quantity} {choice.title()}.")
                price += quantity * 15
                
            case "rajwadi tea":
                quantity = int(input(f"How many {choice.title()} you want? -> "))
                print(f"Here is your Order -> {quantity} {choice.title()}.")
                price += quantity * 20
                
            case "milk tea":
                quantity = int(input(f"How many {choice.title()} you want? -> "))
                print(f"Here is your Order -> {quantity} {choice.title()}.")
                price += quantity * 15
                
            case "green tea":
                quantity = int(input(f"How many {choice.title()} you want? -> "))
                print(f"Here is your Order -> {quantity} {choice.title()}.")
                price += quantity * 20

            case _:
                print("-> Invalid Coffee Tea!")
    
    case 2:
        print("1. Regular Coffee - ₹20")
        print("2. Black Coffee - ₹30")
        print("3. Cold Coffee - ₹25")
        print("4. Hot Coffee - ₹20")
        print("5. Nescafe Coffee - ₹15")
        choice = int(input("Enter your choice: "))
        
        match (choice):
            case 1:
                print("-> Here is your Regular Coffee!")
                
            case 2:
                print("-> Here is your Black Coffee!")
                
            case 3:
                print("-> Here is your Cold Coffee!")
                
            case 4:
                print("-> Here is your Hot Coffee!")
                
            case 5:
                print("-> Here is your Nescafe Coffee!")

            case _:
                print("-> Invalid Coffee Choice!")
    
    case 3:
        print("1. Regular Milk - ₹10")
        print("2. Skimmed Milk - ₹15")
        print("3. Bourvita Milk - ₹25")
        print("4. Goat Milk - ₹20")
        print("5. Cow Milk - ₹25")
        choice = int(input("Enter your choice: "))
        
        match (choice):
            case 1:
                print("-> Here is your Regular Milk!")
                
            case 2:
                print("-> Here is your Skimmed Milk!")
                
            case 3:
                print("-> Here is your Bourvita Milk!")
                
            case 4:
                print("-> Here is your Goat Milk!")
                
            case 5:
                print("-> Here is your Cow Milk!")

            case _:
                print("-> Invalid Milk Choice!")

    case _: # default
        print("-> Invalid Choice!")

print(f"Bill -> ₹{price}")

"""
Problem Statement:

You are building a ticket booking system for a cinema. Users can book tickets for different types of 
movies and seating categories. Implement a `match` case system to handle the following:

1. Movie Types:
   - Action
   - Comedy
   - Drama
   - Horror
   - Science Fiction

2. Seating Categories:
   - Standard
   - Premium
   - VIP

The user should first select the type of movie, then choose the seating category. Based on their 
choices, the system will display the corresponding message and calculate the price based on 
predefined rates:

- Action: $12 (Standard), $18 (Premium), $25 (VIP)
- Comedy: $10 (Standard), $15 (Premium), $20 (VIP)
- Drama: $8 (Standard), $12 (Premium), $18 (VIP)
- Horror: $14 (Standard), $20 (Premium), $27 (VIP)
- Science Fiction: $15 (Standard), $22 (Premium), $30 (VIP)

"""