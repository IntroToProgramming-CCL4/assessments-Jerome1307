#Exercise 6

#This defines the correct password and allows the user to input the password
Correct_Password = (12345)
Attempts = 5
Password_Guesser = int(input("Enter the correct password of 5 numbers: "))

#This loop shows the user the number of attempts they have and once it reaches 0 it shows the message that the owner is alerted
while Password_Guesser != Correct_Password:
        if Attempts < 1:
            print("The owner has been alerted /ᐠ - ˕ -マ︻デ═一")
            break
        else:
            print(f"You have {Attempts} tries remaining")
            Attempts = Attempts - 1
            Password_Guesser = int(input("Enter the correct password of 5 numbers: "))
else:
    print("Access Granted")