#get dog name to make owner feel special
dog_name = input("What is your dog's name? ")

#get dog age
dog_age = float(input("How old is your dog? "))

#if dog is two years or less, disregard weight
#otherwise, get weight
if dog_age > 2:
    dogweight = float(input("How many pounds does your dog weigh? "))

#take age - 2 for multiplying by apropriate variable
#multiply by variable and add 21

if dog_age <= 1:
    dog_years = 15*(dog_age)
elif dog_age <= 2:
    dog_years = 15 + 6*(dog_age - 1)
elif dogweight < 20:
    dog_years = 21 + 4*(dog_age - 2)
elif dogweight >= 20 and dogweight <=50:
    dog_years = 21 + 5*(dog_age - 2)
elif dogweight > 50 and dogweight <= 90:
    dog_years = 21 + 6*(dog_age - 2)
elif dogweight > 90:
    dog_years = 21 + 7*(dog_age - 2)

#tell user how old their dog is
print(dog_name + " is " + str(dog_years) + " years old.")
