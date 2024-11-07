#Exercise 4


print("Hello and Welcome to the Knowledge Quiz\n")
print("There are 10 questions all about the capitals of European Countries\n")
print("If you get one wrong you move to the next question\n")
print("The questions get harder each time\n")
print("If the answer is two words add an underscore _\n")

#This holds the Correct Answers and the Score
Answers = ["Paris", "Rome", "Luxembourg_City", "Amsterdam", "Madrid", "Kiev", "Warsaw", "Riga", "Sarajevo", "Zagreb"]
Score = 0

#The same if-else statement is used and has different responses for each right or wrong answer
France = input("What is the Capital of France? ").capitalize()
if France == Answers[0]:
    print("Easy first question")
    Score = Score + 1
else:
    print("It is the first question how can you get that wrong?")


Italy = input("What is the Capital of Italy? ").capitalize()
if Italy == Answers[1]:
    print("Everyone knows this")
    Score = Score + 1
else:
    print("You don't know this?")


Luxembourg = input("What is the Capital of Luxembourg? ").capitalize()
if Luxembourg == Answers[2]:
    print("Trick Question but you got it")
    Score = Score + 1
else:
    print("Sorry about that trick question")


Netherlands = input("What is the Capital of Netherlands? ").capitalize()
if Netherlands == Answers[3]:
    print("The questions get harder from here")
    Score = Score + 1
else:
    print("I hope you got the other questions correct")


Spain = input("What is the Capital of Spain? ").capitalize()
if Spain == Answers[4]:
    print("Good job")
    Score = Score + 1
else:
    print("5th question yet kinda an easy one yet you got it wrong")


Ukraine = input("What is the Capital of Ukraine? ").capitalize()
if Ukraine == Answers[5]:
    print("Alright respectable")
    Score = Score + 1
else:
    print("I am not suprised you got that worng")


Poland = input("What is the Capital of Poland? ").capitalize()
if Poland == Answers[6]:
    print("You know your capitals")
    Score = Score + 1
else:
    print("At least you tried")


Latvia = input("What is the Capital of Latvia? ").capitalize()
if Latvia == Answers[7]:
    print("Excellent work")
    Score = Score + 1
else:
    print("Study next time")


Bosnia_Herzegovina = input("What is the Capital of Bosnia and Herzegovina? ").capitalize()
if Bosnia_Herzegovina == Answers[8]:
    print("I am shocked you got this")
    Score = Score + 1
else:
    print("Understandable this is an unpopular country")


Croatia = input("What is the Capital of Croatia? ").capitalize()
if Croatia == Answers[9]:
    print("You made it Congratulations")
    Score = Score + 1
else:
    print("Nice try")

#This prints the Score and the message for each one
print("\nYou made it and here is the score")
if Score == 10:
    print(Score)
    print("You know your capitals and studied for this Good job")
elif Score >= 7:
    print(Score)
    print("Alright you know the capitals and did well")
elif Score >= 4:
    print(Score)
    print("you passed and next time try to study")
elif Score >= 1:
    print(Score)
    print("Try to study harder next time")
elif Score == 0:
    print(Score)
    print("You failed /ᐠﹷ ‸ ﹷ ᐟ\ﾉ")