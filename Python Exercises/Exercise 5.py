#Exercise 5

Months = {"1":"31", "2":"28", "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31", "9":"30", "10":"31", "11":"30", "12":"31"}
Month = input("Enter the month number: ")

#If the month number is 2 it checks if it is a leap year or not then otherwise prints the corresponding days
if Month in Months:
    if Month == '2':
        print("Is it a leap year?")
        Chooser = int(input("Write 1 for leap year and 2 if not: "))
        if Chooser == 1:
            Months['2'] = 29
            print(f"There is {Months[Month]} days")
        else:
            print(f"There is {Months[Month]} days")
    else:
        print(f"There is {Months[Month]} days")