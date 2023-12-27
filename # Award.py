# Award.py 

# This is a program that determines the awawrd a person competing in a triathlon will receive. 
# Requirement:
#   Times shoud be in minutes for all three events.
#   Named variables - Swimming, cycling and running 
#   Calculate and display total time taken 
#   Print award according to qualifying criteria. 

#Declare variables

print("\nTriathlon Awards Result!\n\nPlease input minutes using numbers only.\n")

Swimming = float(input("What is your swim time (mins)? "))
Cycling = float(input("What is your cycle time (mins)? "))
Running = float(input("What is your run time (mins)? "))

Triathlon = Swimming + Cycling + Running

print(f"\nYour triathlon time is: {Triathlon} mins\n")

if Triathlon <= 100:
    print ("You have been award : Provincial Colours\n")
elif Triathlon ==101 or Triathlon <=105:
    print ("You have been award : Provincial Half Colours\n")
elif Triathlon ==106 or Triathlon <=110:
    print ("You have been award : Provincial Scroll\n")
else :
    print ("No Award\n")