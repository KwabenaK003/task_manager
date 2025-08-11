# MATCH STATEMENT
day = 5
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")



# Using the pipe characteras an or operator in the CASE Evaluation
day = int(input("Enter the number of the day of the week.\n"))
match day:
    case 1:
        print("It is a weekend, so rest!")
    case 2 | 3 | 4 | 5 | 6:
        print("It is a work day!")
    case 7:
        print("It is a Sabbath day!")
    


# If Statements are Guards
month = int(input("Enter the number of the month of the year.\n"))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("It has 31 days.")
    case 4 | 6 | 9 | 11:
        print("It has 30 days.")
    case 2:
        print("It has 28 days but 29 days in each leap year.")

