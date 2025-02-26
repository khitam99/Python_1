amount=int(input("please enter the amount: "))
team_name="Abtal a-Digital"
team_member=10
is_a_membership_owner=True

if amount>10:
    print("Warning! Too much loan amount.")
elif amount==0 and (not is_a_membership_owner):
    print("You have nothing")
else:
    print("The customer is Not allowed to take a loan.")

print("Program Exiting!")
