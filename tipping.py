class Dinner:
    def __init__(self,a,b,c):
        self.person=a
        self.food=b
        self.cost=c
    def __str__(self):
        return(self.person+" ordered "+self.food+" for a total cost of $"\
               +str(self.cost))


def main():
    cobra=[]
    intro()
    makeameal(cobra)
    


def intro():
    print("You went out to dinner with some friends")


def makeameal(cobra):
    name=input("What is the name of your first friend?\n")
    food=input("What did "+name+" order?\n")
    cost=input("How much did this cost?\n$")
    moreFood="yes"
    while moreFood="yes":
        moreFood="Did "+name+" order anythign else?")
        
    
    yum=Dinner(name,food,cost)
    print(yum)
    



def oldPro():
    print("How much does meal one cost?")
    meal_1 = float(input("     Meal one costs $"))
    print("How much does meal two cost?")
    meal_2 = float(input("     Meal two costs $"))
    print("How much does meal three cost?")
    meal_3 = float(input("     Meal three costs $"))

    meal_price = (meal_1 + meal_2 + meal_3)
    tax = (.0625)*(meal_price)
    tip = (.2)*(meal_price)
    to_pay = (tax + tip + meal_price)
    each_pay = (to_pay)/(3)
    each_minus = (meal_price)/(3)

    print("  ")
    print("Total meal cost is $" + str(meal_price))
    print("Tax is $" + str(format(tax, '.2f')))
    print("Tip is $" + str(format(tip, '.2f')))
    print("Your total bill is $" + str(format(to_pay, '.2f')))
    print("Without tax or tip, the price per person is $" + str(format(each_minus, '.2f')))
    print("The bill for each person is $" + str(format(each_pay, '.2f')))
    print("  ")

