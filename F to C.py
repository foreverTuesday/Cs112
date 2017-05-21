while True:
    print("Operation 1 converts from fahrenheit to celcius.")
    print("Operation 2 converts from celcius to ferenheit.")
    print("Which would you like to do?")
    pick = input("I would like to do Operation ")

    if pick == "1":
            f = float(input("Temperature in fahrenheit? "))
            c = (5/9)*(f-32)
            degree_sign = "\u00b0"
            print(str(f) + "°f equals " + str(c) + degree_sign + "C")

    if pick == "2":
            c = float(input("Temperature in celcius? "))
            f = 32+(9/5)*c
            degree_sign = "\u00b0"
            print(str(c) + "°c equals " + str(f) + degree_sign + "F")

    endgame = input("Convert another number? ")
    print("    ")
    if endgame == "no":
        break
