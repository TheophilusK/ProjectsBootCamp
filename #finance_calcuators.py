#finance_calcuators.py

#This calcuator will allow the use to choose which calcuation they will use investment or bond.
# Investment calcuator - calculate the amount of interest you'll earn on your investment
# Bond calcuator - calucate the amount you will have to pay on a home loan
import math

# Display menu
print("\n\tFinance Calculator\n")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond      - to calculate the amount you'll have to pay on a home loan\n")

# User inputbond 
User_Investment_Type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").capitalize()

# Investment Variables set up 
if User_Investment_Type == "Investment":
    investment_deposit = float(input("How much are you depositing: "))
    investment_interest_rate = float(input("\nWhat is the interest rate (%): "))
    investment_years = int(input("How many years will you be investing for: "))

    simple_interest = investment_deposit * (1 + (investment_interest_rate / 100) * investment_years)
    compound_interest = investment_deposit * math.pow((1 + investment_interest_rate / 100), investment_years)

    # Output for investment type
    investment_type = input("\nSimple or Compound: ").capitalize()

    if investment_type == "Simple":
        print("\nSimple Interest:", simple_interest)
    elif investment_type == "Compound":
        print("\nCompound Interest:", compound_interest)
    else:
        print("Invalid choice. Please enter 'Simple' or 'Compound'.")

    # Bond calculation
elif User_Investment_Type == "Bond".capitalize():
    present_value = float(input("Present value of the house: "))
    annual_interest_rate = float(input("Annual Intrest rate: "))
    Monthly_interest = annual_interest_rate / 12 / 100  # Convert annual rate to monthly rate
    Repayment_month = int(input("Number of months to repay bond: "))

    Repayment = (Monthly_interest* present_value)/(1 - (1+Monthly_interest)**(-Repayment_month))
        
    print(f"Bond repayment : {Repayment}.")
else:
    # If investment or bond not typed return a invaild investment type message.
    print("Invalid investment type. Please enter 'Bond' or 'Investment'.")
