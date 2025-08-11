# Ask user to enter their first name
name1 = input("What is your first name?\n")
name1_upper = name1.upper()
# Ask user to enter their last name
name2 = input("What is your last name?\n")
name2_upper = name2.upper()
# Print iser's fullname in UPPERCASE
# e.g If user full name is Michael Hammond, it should rather print MICHAEL HAMMOND
print(f"Welcome, {name1_upper} {name2_upper}")

# Ask user to enter their first name
name1 = input("What is your first name?\n")
# Ask user to enter their last name
name2 = input("What is your last name?\n")
# Print iser's fullname in UPPERCASE
# e.g If user full name is Michael Hammond, it should rather print MICHAEL HAMMOND
print(f"Welcome, {name1.upper()} {name2.upper()}")


user1 = int(input("Please type a number.\n"))
user = user1 / 2
if type(user) is int:
    print("The value is an even number")
else:
    print("The value is an odd number")

