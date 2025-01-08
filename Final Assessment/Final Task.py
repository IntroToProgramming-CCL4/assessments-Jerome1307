#Assessment #2

#This holds all items with the corresponding Code, Price and Stock Available
import random
Soup_Based_Food = {"A1": {"Code":"A1", "Food":"Pork Sinigang", "Price":20, "Stock":random.randint(1, 9)},
    "A2": {"Code":"A2", "Food":"Beef Sinigang", "Price":15, "Stock":random.randint(1, 9)},
    "A3": {"Code":"A3", "Food":"Tinolang Manok", "Price":10, "Stock":random.randint(1, 9)},
    "A4": {"Code":"A4", "Food":"Pork Nilaga", "Price":20, "Stock":random.randint(1, 9)},
    "A5": {"Code":"A5", "Food":"Beef Nilaga", "Price":25, "Stock":random.randint(1, 9)}}

Sauce_Based_Food = {"B1": {"Code":"B1", "Food":"Beef Kare-Kare", "Price":25, "Stock":random.randint(1, 9)},
    "B2": {"Code":"B2", "Food":"Beef Caldereta", "Price":25, "Stock":random.randint(1, 9)},
    "B3": {"Code":"B3", "Food":"Pork Caldereta", "Price":20, "Stock":random.randint(1, 9)}}

Fried_Food = {"C1": {"Code":"C1", "Food":"Fried Chicken", "Price":15, "Stock":random.randint(1, 9)},
    "C2": {"Code":"C2", "Food":"Lechon Kawali", "Price":30, "Stock":random.randint(1, 9)},
    "C3": {"Code":"C3", "Food":"Crispy Pata", "Price":30, "Stock":random.randint(1, 9)}}

Condiments = {"D1": {"Code":"D1", "Condiment":"Bagoong", "Price":2, "Stock":random.randint(5, 15)},
    "D2": {"Code":"D2", "Condiment":"Ketchup", "Price":3, "Stock":random.randint(5, 15)},
    "D3": {"Code":"D3", "Condiment":"Mang Tomas", "Price":3, "Stock":random.randint(5, 15)},
    "D4": {"Code":"D4", "Condiment":"Soy Sauce", "Price":2, "Stock":random.randint(5, 15)},
    "D5": {"Code":"D5", "Condiment":"Calamansi", "Price":1, "Stock":random.randint(5, 15)},
    "D6": {"Code":"D6", "Condiment":"Patis  ", "Price":2, "Stock":random.randint(5, 15)}}

Drinks = {"E1": {"Code":"E1", "Drink":"Bottle Water", "Price":1, "Stock":random.randint(10, 25)},
    "E2": {"Code":"E2", "Drink":"Coca Cola", "Price":3, "Stock":random.randint(10, 25)},
    "E3": {"Code":"E3", "Drink":"Rc Cola", "Price":3, "Stock":random.randint(10, 25)},
    "E4": {"Code":"E4", "Drink":"Mountain Dew", "Price":3, "Stock":random.randint(10, 25)},
    "E5": {"Code":"E5", "Drink":"Root Beer", "Price":3, "Stock":random.randint(10, 25)}}

#Saves the Menu in a function to reprint the Menu if needed
def Menu():
    print("")
    print("Soup Based Foods")
    for key, value in Soup_Based_Food.items():
        print(f"Code:{value['Code']} \t{value['Food']} \tPrice:{value['Price']}AED \tStock:{value['Stock']}")

    print("")
    print("Sauce Based Foods")
    for key, value in Sauce_Based_Food.items():
        print(f"Code:{value['Code']} \t{value['Food']} \tPrice:{value['Price']}AED \tStock:{value['Stock']}")

    print("")
    print("Fried Foods")
    for key, value in Fried_Food.items():
        print(f"Code:{value['Code']} \t{value['Food']} \tPrice:{value['Price']}AED \tStock:{value['Stock']}")

    print("")
    print("Condiments")
    for key, value in Condiments.items():
        print(f"Code:{value['Code']} \t{value['Condiment']} \tPrice:{value['Price']}AED \tStock:{value['Stock']}")

    print("")
    print("Drinks")
    for key, value in Drinks.items():
        print(f"Code:{value['Code']} \t{value['Drink']} \tPrice:{value['Price']}AED \tStock:{value['Stock']}")

#Function to show suggestions based on what the user has chosen
def Suggestions():
    Suggestion_Soy_Sauce_Calamansi = ["A1", "A2"]
    Suggestion_Patis = ["A3", "A4", "A5"]
    Suggestion_Bagoong = ["B1"]
    Suggestion_Ketchup_Mang_Thomas = ["C1", "C2", "C3"]

    if Asker.capitalize() in Suggestion_Soy_Sauce_Calamansi:
        print(f"We would like to recommend to add {Condiments['D4']['Condiment']} and {Condiments['D5']['Condiment']}")
    elif Asker.capitalize() in Suggestion_Patis:
        print(f"We would like to recommend to add {Condiments['D6']['Condiment']}")
    elif Asker.capitalize() in Suggestion_Bagoong:
        print(f"We would like to recommend to add {Condiments['D1']['Condiment']}")
    elif Asker.capitalize() in Suggestion_Ketchup_Mang_Thomas:
        print(f"We would like to recommend to add {Condiments['D2']['Condiment']} or {Condiments['D3']['Condiment']}")

#This is the start of the vending machine and asks how much they placed in the machine
print("Hello and Welcome to the Cafeteria-inspired Vending Machine\n")
print("Select from the selection of different kinds of foods and Drinks")
Menu()
print("\nBut first input how much money you are working with\n")
while True:
    try:
        Money_Asker = float(input("Enter the amount of Money you have: "))
        if Money_Asker > 0:
            break  
        else:
            print(f"\nYou need to input at least one AED")
    except:
        print("\nPlease input a valid amount.")


#Asks the User to input the Code to dispense and informs user the inputs needed to finish or print the menu again
Counter = 0.0
Repeater = "Done"
print(f"\nYou have {Money_Asker}AED now pick what you want: ")
print("\nYou can add more items if needed and then enter Done when Finish")
print("\nYou can also input Menu if you want to see the menu again")
Asker = input("\nEnter the Item Code you want to dispense: ")

#Checks if the Code is Valid and shows the Item, Price and available Stock
while Asker.capitalize() != Repeater:
    if Asker.capitalize() == "Menu":
        Menu()
        Asker = input("\nEnter the Item Code you want to dispense: ")

    elif Asker.capitalize() in Soup_Based_Food:
        Check_Soup = Soup_Based_Food[Asker.capitalize()]
        if Check_Soup['Stock'] >= 0:
            Check_Soup['Stock'] -= 1
            print(f"{Check_Soup['Food']}")
            print(f"{Check_Soup['Price']}AED")
            print(f"Stock Left:{Check_Soup['Stock']}")
            Counter += Check_Soup['Price']
            Suggestions()
            Asker = input("\nEnter the Item Code you want to dispense: ")
        else:
            print(f"\nThe {Check_Soup['Food']} is now out of stock.")
            print("\nPlease try a different item")
            Asker = input("\nEnter the Item Code you want to dispense: ")

    elif Asker.capitalize() in Sauce_Based_Food:
        Check_Sauce = Sauce_Based_Food[Asker.capitalize()]
        if Check_Sauce['Stock'] > 0:
            Check_Sauce['Stock'] -= 1
            print(f"{Check_Sauce['Food']}")
            print(f"{Check_Sauce['Price']}AED")
            print(f"Stock left:{Check_Sauce['Stock']}")
            Counter += Check_Sauce['Price']
            Suggestions()
            Asker = input("\nEnter the Item Code you want to dispense: ")
        else:
            print(f"\nThe {Check_Sauce['Food']} is now out of stock.")
            print("\nPlease try a different item")
            Asker = input("\nEnter the Item Code you want to dispense: ")
            
    elif Asker.capitalize() in Fried_Food:
        Check_Fried = Fried_Food[Asker.capitalize()]
        if Check_Fried['Stock'] > 0:
            Check_Fried['Stock'] -= 1
            print(f"{Check_Fried['Food']}")
            print(f"{Check_Fried['Price']}AED")
            print(f"Stock left:{Check_Fried['Stock']}")
            Counter += Check_Fried['Price']
            Suggestions()
            Asker = input("\nEnter the Item Code you want to dispense: ")
        else:
            print(f"\nThe {Check_Fried['Food']} is now out of stock.")
            print("\nPlease try a different item")
            Asker = input("\nEnter the Item Code you want to dispense: ")

    elif Asker.capitalize() in Condiments:
        Check_Condiment = Condiments[Asker.capitalize()]
        if Check_Condiment['Stock'] > 0:
            Check_Condiment['Stock'] -= 1
            print(f"{Check_Condiment['Condiment']}")
            print(f"{Check_Condiment['Price']}AED")
            print(f"Stock left:{Check_Condiment['Stock']}")
            Counter += Check_Condiment['Price']
            Asker = input("\nEnter the Item Code you want to dispense: ")
        else:
            print(f"\nThe {Check_Condiment['Condiment']} is now out of stock.")
            print("\nPlease try a different item")
            Asker = input("\nEnter the Item Code you want to dispense: ")

    elif Asker.capitalize() in Drinks:
        Check_Drink = Drinks[Asker.capitalize()]
        if Check_Drink['Stock'] > 0:
            Check_Drink['Stock'] -= 1
            print(f"{Check_Drink['Drink']}")
            print(f"{Check_Drink['Price']}AED")
            print(f"Stock left:{Check_Drink['Stock']}")
            Counter += Check_Drink['Price']
            Asker = input("\nEnter the Item Code you want to dispense: ")
        else:
            print(f"\nThe {Check_Drink['Drink']} is now out of stock.")
            print("\nPlease try a different item")
            Asker = input("\nEnter the Item Code you want to dispense: ")

    else:
        print(f"\nPls Try Again, As the Item Code you inputted is not in the Menu")
        Asker = input("\nEnter the Item Code you want to dispense: ")
else:
    print(f"\nThe total amount to pay is {Counter}AED")

#This checks if you have enough money to pay and dispenses the item if not you can add more
if Money_Asker >= Counter:
    Deductor = Money_Asker - Counter
    print("\nItems has been dispensed")
    print(f"\nYour change is {Deductor}AED")
elif Money_Asker < Counter:
    Money_Need = Counter - Money_Asker
    print(f"\nYou still need {Money_Need}AED")
    Money_Add = input("\nEnter Yes if you want to add more money: ")
    if Money_Add.capitalize() == "Yes":
        while Money_Asker < Counter:
            try:
                Adder = float(input("\nEnter the money you need to add: "))
                Money_Asker = Money_Asker + Adder
                Money_Need = Counter - Money_Asker
                if Money_Need <= 0:
                    continue
                elif Money_Need > 0:
                    print(f"\nYou still need {Money_Need}AED")
            except:
                print("\nPlease input a valid amount.")
        else:
            Deductor = Money_Asker - Counter
            print("\nItems has been dispensed")
            print(f"\nYour change is {Deductor}AED")
    else:
        print(f"\nYou have been refunded of {Money_Asker}AED")