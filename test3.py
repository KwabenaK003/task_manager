my_dict = {
    "name" : "Kwabena Kumi",
    "nationality" : "Ghanaian",
    "language" : ["Twi", "English", "French"],
    "occupation" : "Web developer",
    "education" : "degree holder",
    "age" : 80
}
for x in my_dict:
    print(x)

i = 1
while i <= 5:
    i += 1
    print(i)

mylist = ["banana", "mango", "orange", "pear"]
for values in mylist:
    print(values)
    if values == "orange":
        break


for x in range(1, 5):
    print(x)
else:
    print("Well done!")


a = float(input("Enter the first number\n"))
b = float(input("Enter the second number\n")) 
print(f"The average is {(a + b)/2}")

name = input("What is your name?\n")
age = float(input("How old are you?\n"))
if age < 18 and int((a + b)/2) == 20:
    print(f"{name}, you are not allowed to vote")
elif age >= 18 and int((a + b)/2) >= 20:
    print(f"{name}, you are allowed to vote")
elif age >= 18 or int((a + b)/2) == 10:
    print(f"{name}, you are allowed to vote")
