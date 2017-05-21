#store variables for types of cancer and gender
breast_male = "0.13%"
lung_male = "7.43%"
stomach_male = "1.08%"
breast_female = "12.33%"
lung_female = "6.17%"
stomach_female = "0.67%"

#ask the person for their name
name = input("What is your name? ")

#ask if the person is male of female
sex = input(name + ", are you male or female? ")


#ask the person what type of cancer they are concerned about (out of the three)
print("Are you concerned about breast, lung, or stomach cancer?")
kind = input("Please pick only one: ")

while True:
    #tell the person their risk of cancer
    if sex == "male":
        if kind == "breast":
            print(name + ", your risk of developing " + kind + " cancer is " + breast_male)
        if kind == "lung":
            print(name + ", your risk of developing " + kind + " cancer is " + lung_male)
        if kind == "stomach":
            print(name + ", your risk of developing " + kind + " cancer is " + stomach_male)
    if sex == "female":
        if kind == "breast":
            print(name + ", your risk of developing " + kind + " cancer is " + breast_female)
        if kind == "lung":
            print(name + ", your risk of developing " + kind + " cancer is " + lung_female)
        if kind == "stomach":
            print(name + ", your risk of developing " + kind + " cancer is " + stomach_female)

    print("  ")
    more = input("Are you concerned about another type of cancer? ")
    if more == "no":
        break
    else:
        print("Are you concerned about breast, lung, or stomach cancer?")
        kind = input()
