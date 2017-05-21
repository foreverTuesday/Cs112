#Program Goals:
#1 tell user the age range of people they can date
#2 tell user they may not date anyone named David


#ask for user's age
your_age = float(input("What is your age? "))

#find the low end of their datable range
datable = 7 + your_age/2

#find the high end of the range
uplim = (your_age - 7)*2


#tell user who they can date
elif uplim <= datable:
    print("You are too young to date.")
else:
    print("The youngest person you can date is " + str(datable) + " years old.")
    print("The oldest person you can date is " + str(uplim) + " years old.")


