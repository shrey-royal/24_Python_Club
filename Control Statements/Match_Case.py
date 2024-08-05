# Match Case (Switch Case)

print("1. Tea")
print("2. Coffee")
print("3. Milk")
choice = int(input("Enter your choice: "))

match(choice):
    case 1:
        print("1. Regular Tea")
        print("2. Masala Tea")
        print("3. Rajwadi Tea")
        print("4. Milk Tea")
        print("5. Green Tea")
        choice = int(input("Enter your choice: "))
        
        match (choice):
            case 1:
                print("-> Here is your Regular Tea!")
                
            case 2:
                print("-> Here is your Masala Tea!")
                
            case 3:
                print("-> Here is your Rajwadi Tea!")
                
            case 4:
                print("-> Here is your Milk Tea!")
                
            case 5:
                print("-> Here is your Green Tea!")

            case _:
                print("-> Invalid Tea Choice!")
    
    case 2:
        print("1. Regular Coffee")
        print("2. Black Coffee")
        print("3. Cold Coffee")
        print("4. Hot Coffee")
        print("5. Nescafe Coffee")
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
        print("1. Regular Milk")
        print("2. Skimmed Milk")
        print("3. Bourvita Milk")
        print("4. Goat Milk")
        print("5. Cow Milk")
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