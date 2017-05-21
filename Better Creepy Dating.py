##main function
#get users age
#get potential date's age
def main():
    intro()
    test = float(input("How old are you? "))
    goodDate(test)


##Function to introduce to the program
#give instructions
def intro():
    print("Welcome to Date Pro, the better dating software")
    print("With just 2 numbers from you, we can tell if any hottie is right for you")

##Function to find the upper limit of people your client can date
def Up(test):
    uplim = (test - 7)*2
    return uplim

##Function to find the lower limit of people your client can date
def Low(test):
    lowlim = 7 + test/2
    return lowlim

##Function to report whether your client can date the particular prospect
def goodDate(test):
    if Up(test) <= Low(test):
        print("You are too young to date.")
    else:
        boyfriend = float(input("How old is the hottie? "))
        if boyfriend <= Up(test) and boyfriend >=Low(test):
            print("The two of you are a perfect match!")
        else:
            print("The two of you are not a good match.  Better luck next time.")

#testing data
            #test=20, boyfriend=12
            #test=20, boyfriend=21
            #test=12
