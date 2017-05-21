dog_age = 0
dog_years = 0
dogweight = 0
dog_name = "unknown"
total_age = 0

#find out how many dogs the client has
dog_num = int(input("How many dogs do you have? "))


#run "better dog years" for each dog
for x in range (0,dog_num):
    #get dog name to make owner feel special
    dog_name = input("What is dog #" + str(x+1) + "'s name? ")

    #get dog age
    dog_age = float(input("How old is " + dog_name + "? "))

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

#add dog_age to some total
    total_age = total_age + dog_years

    #tell user how old their dog is in dog and calendar years
    print(dog_name + " is " + str(dog_age) + " calendar years old.")
    print(dog_name + " is " + str(dog_years) + " dog years old. \n")

#tell the user the average age of their dogs
print("The average age of your dogs is " + str(total_age/dog_num) + " dog years.")


#test variables:
    #2 dogs of different ages
    #3 dogs of different ages
    #test all values for "better dog years"
        #dog >= one year old
        #dog between one and two years old
        #small dog older than 2
        #medium dog older than 2
        #large dog older than 2
        #very large dog older than 2
