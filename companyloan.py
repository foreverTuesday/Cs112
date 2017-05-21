#ask how long the employee has been at the company for
years = float(input("How many years have you worked at the company for? "))


#ask how much the employee makes
salary = float(input("How many thousands of dollars do you make per year? "))


#say if they can get a loan or not and why
if years>=2 and salary>=24:
    print("You can get a company sponsored loan!")
elif years<=2 and salary<=24:
    print("You have not worked here long enough nor do you make enough money to qualify for a company sponsored loan.")
elif years<=2:
    print("You have not worked here long enough to qualify for a company sponsored loan.")
elif salary<=24:
    print("You do not make enough money to qualify for a company sponsored loan.")
    

