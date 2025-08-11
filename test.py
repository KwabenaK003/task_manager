# Ask user to input their score as a number
# If score is between 90 to 100(inclusive) print grade A
# If score is between 80 to 89(inclusive) print grade B
# If score is between 70 to 79(inclusive) print grade C
# If score is between 60 to 69(inclusive) print grade D
# If score is between 0 to 159(inclusive) print grade F
user = float(input("Please type your total score.\n"))
if user >= 90 and user <= 100:
    print("You had grade A.")
elif user >= 80 and user < 90:
    print("You had grade B.")
elif user >= 70 and user < 80:
    print("You had grade C.")
elif user >= 60 and user < 70:
    print("You had grade D.")
elif user >= 0 and user < 60:
    print("You had grade F.")



# Ask user to input their purchase amount as float
# Amount is more than 100 cedis apply 20% discount and print amount to pay
# Amount is 50 cedis or more apply 10% discount and print amount to pay
# If amount is less than 50 cedis apply no discount and print amount to pay
user = float(input("Enter your purchase amount in cedis.\n"))
discount1 = 0.2 * user
discount2 = 0.1 * user
if user >= 100:
    print(f"Your purchase amount is {user - discount1}")
elif user >= 50:
    print(f"Your purchase amount is {user - discount2}")
elif user < 50:
    print(f"No discount applied. Your purchase amount is {user}")



day = int(input("Enter the number of the day of the week.\n"))
if day == 1:
    print("Monday.")
elif day == 2:
    print("Tuesday.")
elif day == 3:
    print("Wednesday.")
elif day == 4:
    print("Thursday.")
elif day == 5:
    print("Friday.")
elif day == 6:
    print("Saturday.")
elif day == 7:
    print("Sunday.")




    

