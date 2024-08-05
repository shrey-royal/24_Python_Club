# if else
'''
if (condition):
    //body of if
else:
    //body of else
'''

# age = int(input("Enter age: "))

# if age > 18:
#     print("You are an Adult")
# else:
#     print("You are a kid")

####################################################

# ladder if else

# marks = int(input("Enter your marks: "))
# grade = ""

# if marks > 90 and marks <= 100:
#     grade = "A+"
# elif marks > 60 and marks <= 90:
#     grade = "B"
# elif marks > 40 and marks <= 60:
#     grade = "C"
# elif marks > 33 and marks <= 40:
#     grade = "D"
# else:
#     grade = "F"

# print(f"you got {grade}")

####################################################

age = int(input("Enter your age: "))

if age >= 13:
    print("You can watch the movie!")
else:
    has_permission = input("Do the Kid have permission to watch the movie? (y/n): ")
    if has_permission.lower() == "y":
        print("You can watch the movie with permission!")
    else:
        print("Sorry, you can't watch the movie.")

"""
If Else Tasks:

1. Temperature Activity:
   - Given the current temperature in degrees Celsius, decide if it's a good day for a picnic or if it’s too cold. If it's above 25°C, suggest going for a picnic. If it's between 15°C and 25°C, suggest a walk. If it's below 15°C, suggest staying indoors.

2. Student Grade:
   - Given a student’s score, determine their grade. If the score is 90 or above, they get an 'A'. If it's between 80 and 89, determine if the score is closer to 80 or 89 to decide if they get a 'B+' or 'B'. If it's below 80, give a 'C'.

3. Theater Ticket Pricing:
   - Given the age of a movie-goer and whether they have a membership card, determine the ticket price. If they are under 12, it's a children's ticket price. If they are 12 to 65, determine if they have a membership card to decide between a standard or a discounted ticket. If they are above 65, they get a senior discount.

4. Grocery Store Discount:
   - Given the total amount of a purchase and whether the customer has a loyalty card, decide if a discount is applied. If the amount is $100 or more, check if the customer has a loyalty card to decide between a 10% or a 5% discount. If less than $100, no discount is applied.

5. Club Membership Eligibility:
   - Given a person’s age and their income, determine if they are eligible for a premium club membership. If they are 30 or older and their income is above $50,000, they qualify for premium membership. If they are younger but have an income above $50,000, determine if they have special recommendations to decide on eligibility.

6. Job Application Status:
   - Given the applicant’s years of experience and education level, determine if they qualify for an interview. If they have 5 or more years of experience, check if their education level is a bachelor’s degree or higher. If less than 5 years of experience, determine if they have any relevant certifications.

7. Travel Visa Eligibility:
   - Given the applicant’s country of origin and the purpose of their visit, determine if they need a visa. If they are from a country that requires a visa and the visit is for business, they need to apply for a business visa. If the visit is for tourism, check if they need a visa based on the duration of their stay.

8. Online Course Access:
   - Given the student’s age and their prior knowledge level, determine their access to an online course. If the student is above 18 and has prior knowledge, they get full access. If they are younger or have no prior knowledge, check if they have a recommendation to provide access.

9. Bank Account Types:
   - Given a person’s savings balance and their age, determine the type of bank account they should open. If their balance is above $10,000 and they are over 18, suggest a high-interest savings account. If their balance is below $10,000 but they are over 18, suggest a regular savings account. If under 18, suggest a youth savings account.

10. Restaurant Seating:
    - Given the number of people in a party and if it’s a special occasion, decide on the type of seating arrangement. If the party has 8 or more people and it’s a special occasion, suggest a private dining area. If the party has fewer people or it’s not a special occasion, suggest a regular table.
    
    
"""