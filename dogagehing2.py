dog1name = input("What's the name of your dog ")
calendarAge = int(input("What's " + dog1name + "\'s age (calendar years)? "))
dog1age = calendarAge*7

dog2name = input("What's the name of your dog? ")
calendarAge = int(input("What's " + dog2name + "\'s age (calendar years)? "))
dog2age = calendarAge*7

print(dog1name + " is " + str(dog1age) + " years old (dog years) and ")
print(dog2name + " is " + str(dog2age) + " years old (dog years).")
