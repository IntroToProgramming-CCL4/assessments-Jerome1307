#Exercise 3
Information = {"Name":"", "Hometown":"", "Age":""}

#This allows the user to input the data in the dictionary
name = input("Enter your name: ")
hometown = input("Enter your howntown: ")
age = int(input("Enter your age: "))

#The data inputed is then placed in the dictionary in their corresponding keys
Information["Name"] = name
Information["Hometown"] = hometown
Information["Age"] = age

for Info in Information.values():
    print(Info, type(Info))