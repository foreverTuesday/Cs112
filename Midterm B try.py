#have computer pick a random integer between 1 and 10
import random
number = random.randint(1,10)
print(number)

#tell the user(s) how to play the game
P1 = input("Player 1, what is your name? ")
P2 = input("Player 2, what is your name? ")

print(P1 + " & " + P2 + ", this is a two player number guessing game.")
print("I am thinking of a number between 1 and 10")
print("You will have six tries total to guess my number.")
print("Good luck, " + P1 + " & " + P2)

count1 = 0
count2 = 0
count3 = 0
cue1 = "yes"
cue2 = "yes"
guess = 100

while (count3 < 6 and guess != number):
    print("You have " + str(6 - count3) + " guesses remaining.")
    if cue1 == "no" and cue2 == "no":
        break
    if (cue1 != "no" and guess != number):
        guess = int(input(P1 + ", guess a number between 1 and 10: "))
        if guess == number:
            print(P1 + ", you win!!!!!!!!")
        else:
            count1 = count1 + 1
            if guess > number:
                print("Your guess is too high.")
            if guess < number:
                print("Your guess is too low.")
            if count3 != 5 and count1 != 3:
                cue1 = input("Are you going to want to guess again? ")
            if cue2 != "no":
                print("It is now " +P2 + "'s turn.")
                input(P2 + ", please press enter when you are ready to play.")
        
#player 2 guessing
    if (cue2 != "no" and guess != number):           
        guess = int(input(P2 + ", guess a number between 1 and 10: "))
        if guess == number:
            print(P2 + ", you win!!!!!!!!")
        else:
            count2 = count2 + 1
            if guess > number:
                print("Your guess is too high.")
            if guess < number:
                print("Your guess is too low.")
            if count3 != 5 and count2 != 3:
                cue2 = input("Are you going to want to guess again? ")
            if cue1 != "no" and count1 < 3:
                print("It is now " +P1 + "'s turn.")
                input(P1 + ", please press enter when you are ready to play.")
    count3 = count1 + count2

if guess != number:
    print(P1 + " & " + P2 + ", you both LOSE :(")
