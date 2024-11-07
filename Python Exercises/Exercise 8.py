#Exercise 8


Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
Searcher = input("Enter the name you want to search: ")

#This checks if the name searched is in the list of names
if Searcher in Names:
    print(f"{Searcher} is in the list. ")
else:
    print(f"{Searcher} is not in the list")