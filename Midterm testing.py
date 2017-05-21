#have computer pick a random integer between 1 and 10
import random
number = random.randint(1,10)


#tell the user(s) how to play the game
print("This is a number guessing game.")
print("I am thinking of a number between 1 and 10")
print("You will have six tries to guess my number.")
print("Good luck.")


#define all variables that are used for loop continuation
count = 0

########### for C ########
#start loop here
while (count < 6):
#ask the user to guess a number
    guess = int(input("Guess a number between 1 and 10: "))
#add to a count
    count = count + 1
#tell user if number is too high, too low, or correct
    if guess == number:
        print("You win!!!!!!")
        break
    elif guess > number:
        print("Your guess is too high.")
        print("You have " + str(6 - count) + " guesses left")
    elif guess < number:
        print("Your guess is too low.")
        print("You have " + str(6 - count) + " guesses left")
    if count != 6:
        go = input("Would you like to guess again? ")
    if go == "no":
        print("Goodbye")
        break
if guess != number and go != "no" :
    print("You lose")


######### for B ###########
#ask both players for their names (P1 and P2)
#start loop here
#let P1 guess
#add to count1
#tell P1 if their guess was high, low, or correct
    #if correct, congradulate them and break
    #if incorrect
        #tell them how many guesses they have left (3 - count1)
        #ask them if they want to guess again
        #tell P1 to give the computer to P2
#Let P2 guess
#add to count2 and count3
#tell P2 if their guess was high, low, or correct
    #if correct, congradulate them and break
    #if incorrect
        #tell them how many guesses they have left (3 - count2)
        #ask them if they want to guess again
        #tell P2 to give the computer to P1
#count3 = count1 + count2
#if count3 = 6 or someone has guessed correctly, break the loop

#if neither player guessed correct, print names and that they are losers



#############  for A  ###########
#I'm going to code C and B first.....
#I need to do some code before I can write it all out


