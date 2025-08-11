# If statement
user = float(input("Input your age.\n"))
if user >= 18:
    print("You're an adult!")
else:
    print("You're underaged!")

a = float(input("Please, type any number\n"))
b = float(input("Please, type another number\n"))


# if, elif and else statement
if a == b:
    print("They are equal.")
elif a > b:
    print("A is bigger than B.")
elif a < b:
    print("A is smaller is than B.")
else:
    print("I don't know what is going on.")



gender = male, female
user = input(f"What is your {gender}")
if gender == male:
    print("Please, sit on the right.")
    
elif gender == female:
    print("PLease, sit on the left")
else:
    print("Sorry, you are not allowed.")


# Ask user to input an integer
# Find the integer modulo 2
# If the remainder is equal to 0 print even
# Else print odd
user = int(input("Please type a number.\n"))
if user % 2 == 0:
    print("The value is an even number.")
else:
    print("The value is an odd number.")