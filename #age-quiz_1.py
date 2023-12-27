#age-quiz.py
# This is a code for creating a age quiz making the use of if,elif and control structures.

# Requirements of the quiz : 
#    40 >= return message "You're over the hill"
#    > 100 return message " Sorry, you're dead."
#    65 >= return message " Enjoy your retirement!"
#    13 < return message " You qualifiy for the kiddie discount"
#    21 == return message "Congrats on your 21st"
#    Any other age return message " Age is but a number"

Age = int(input("What is your age? "))
print (f"\nYour age is {Age}")

if Age < 13:
    print ("You qualify for the kiddie discount")
elif Age == 21:
    print ("Congrats on your 21st!")
elif Age >= 40:
    print ("You're over the hill")
elif Age >= 65:
    print ("Enjoy your retirement!")
elif Age >100:
    print("Sorry you're dead.")
else:
    print("Age is but a number.")