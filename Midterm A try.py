#tell the user(s) how to play the game
P1 = input("Player 1, what is your name? ")
P2 = input("Player 2, what is your name? ")

print(P1 + " & " + P2 + ", this is a two player number guessing game.")
print("You will compete against each other in 3 games to guess my number first")
print("I am thinking of a number between 1 and 10")
print("You will have six tries total to guess my number each game.")
print("Good luck, " + P1 + " & " + P2)

winner = 0

for x in range (0, 3):
    import random
    number = random.randint(1,10)
#for testing purposes, remove the # from before the next line
    #print(number)

    count1 = 0
    count2 = 0
    count3 = 0
    cue1 = "yes"
    cue2 = "yes"
    guess = 100
    remind1 = " "
    remind2 = " "
    
    while (count3 < 6 and guess != number):
        print("There are " + str(6 - count3) + " guesses remaining.")
        if count3 != 0 and cue1 != "no":
            print("The numbers you have already guessed are:" + remind1)
        if cue1 == "no" and cue2 == "no":
            break
        if (cue1 != "no" and guess != number):
            guess = int(input(P1 + ", guess a number between 1 and 10: "))
            remind1 = remind1 + " " + str(guess)
            if guess == number:
                print(P1 + ", you win!!!!!!!!")
                winner = winner + 1
            else:
                count1 = count1 + 1
                if guess > number:
                    print("Your guess is too high.")
                if guess < number:
                    print("Your guess is too low.")
                if count3 != 5 and count2 != 2:
                    cue1 = input("Are you going to want to guess again? ")
                if cue2 != "no":
                    print("It is now " + P2 + "'s turn.")
                    input(P2 + ", please press enter when you are ready to play.")

        if count3 != 0 and cue2 != "no":
            print("The numbers you have already guessed are:" + remind2)
        if (cue2 != "no" and guess != number):           
            guess = int(input(P2 + ", guess a number between 1 and 10: "))
            remind2 = remind2 + " " + str(guess)
            if guess == number:
                print(P2 + ", you win!!!!!!!!")
                winner = winner - 1
            else:
                count2 = count2 + 1
                if guess > number:
                    print("Your guess is too high.")
                if guess < number:
                    print("Your guess is too low.")
                if count3 != 5 and count1 != 3:
                    cue2 = input("Are you going to want to guess again? ")
                if cue1 != "no" and count1 < 3:
                    print("It is now " +P1 + "'s turn.")
                    input(P1 + ", please press enter when you are ready to play.")
        count3 = count1 + count2

    print("You have completed game #" + str(int(x + 1)))
    if guess != number:
        print(P1 + " & " + P2 + ", you both LOSE :(")

if winner > 0:
    print(P1 + ", you are the ultimate winner because you have won the most games.")
if winner < 0:
    print(P2 + ", you are the ultimate winner because you have won the most games.")
if winner == 0:
    print(P1 + " & " + P2 + ", you have tied.  There is no ultimate winner.")


#I started by coding the C code, then B, then A, making sure each worked without errors before continuing
#My pseudo code was very vague, so I had to refine my code a lot from it
#I tested my code each time I made a change to make sure it functioned properly
#There are a lot of "counting" variables in my code, so I had to test each of them under different conditions to make sure they all functioned properly
#One of the challenges I had to figure out was the ways the two players impacted each other, for example:
    #The number of guesses left if one player quit
    #seprately storing numbers each player had already guessed
    #not letting players guess once the number had been figured out
#I originally set the code to display the random number to make it easier to test
#I tested the code by running it with various combinations of correct and incorrect guesses
    #neither player ever guessing the number
    #one player quitting right away
    #one player guessing correctly more than the other
    #players tieing both games
