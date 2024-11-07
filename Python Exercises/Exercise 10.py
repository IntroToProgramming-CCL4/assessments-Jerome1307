#Exercise 10

#This is the main function that has the input and prints the message from the next function
def Even_Odd():
    Checker = int(input("Enter a number: "))
    message = Check(Checker)
    print(message)

#This checks if the number is Even or Odd and returns with a message
def Check(Checker):
    if Checker % 2 == 0:
        return(f"The number {Checker} is Even.")
    else:
        return(f"The number {Checker} is Odd.")

Even_Odd()