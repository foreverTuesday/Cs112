while True:

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

    again = input("Again? ")
    if again == "no":
        break
