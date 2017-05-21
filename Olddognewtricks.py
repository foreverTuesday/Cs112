

#this is where you put in the dog's name
dogname = input("What is your dog's name? ")

#this is where you put in the dog's age
dogage = float(input("How old is " + dogname + "? "))

#now we'll say if the dog can learn new tricks or not
if dogage>=8:
    print(dogname + " is an old dog. " + dogname + " cannot learn new tricks.")
else:
    print(dogname + " is not an old dog. " + dogname + " can learn new tricks!")

if dogage>=16:
    print("Your dog is very old and cannot even remember old tricks.")



print(" ")



#now we're going to look at ages

#first your age
yourage=float(input("How old are you? "))

#this is how old the dog is in dog years
dogyears=dogage*7

print("Your dog is " + str(dogyears) + " dog years old.")

#now we'll see if the dog is older than you
if dogyears>=yourage:
    print(dogname + " is effectively older than you.")
