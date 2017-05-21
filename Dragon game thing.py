#team1
#introduction

#introduction

import time
import random

print ('Today could be the last day of your life.')
time.sleep(2)
print ('You are about to enter one of the four caves in a land full of dragons.')
time.sleep(2)
print ('One of them is a friendly dragon who will let you live and share their treasure with you.')
time.sleep(2)
print ('One of them is an evil one who will eat you alive.')
time.sleep(2)
print ('One is an airless cave, which you will need to pay the dragon before you die of hypoxia.')
time.sleep(2)
print ('The last one is a waterless cave, which you will also need to pay the dragon before you die of dehydration.')
time.sleep(2)
print ('You will be given 150 gold coins to begin with.')
time.sleep(2)
print ('Choose wisely.')

#give the person 150 gold coins

startingmoney= 150
print ('You will have 150 gold coins to start with.')





#team2
friendlyCave = 1
dangerCave = 2
airlessCave = 3
waterlessCave = 4

randomCave = random.randint (1,4)

#team3
def friendlyCave1(coin):
    import time
    print("You step into the cave...")
    time.sleep(2)
    print("...you hear nothing.")
    print("No breathing of dragons..")
    print("..no stillness of air..")
    print("just silence.")
    time.sleep(3)
    print("You look further into the cave ")
    print("and see...")
    time.sleep(2)
    print("A pile of gold coins! ")
    print("Congratulations! You've completed the quest!")
    return(int(coin)+200)


#team4

def dangerCave(coin):
    answer=0
    coinslost=random.randint(1,100)
    print("As you approach the cave...")
    time.sleep(3)
    print("You encounter a great, red dragon who steals your wallet.")
    time.sleep(3)
    print("The dragon asks you to guess which hand the wallet is held in.")
    time.sleep(2)
    print("If you guess correctly, you will only lose 80 coins.")
    print("If you guess wrong...")
    time.sleep(3)
    print("...you will be killed.")
    time.sleep(2)
    answer=input("Is the wallet in the left hand or the right hand?")
    if answer =="left":
        print("You are lucky enough to only lose coins.")
        return(coin-coinslost)
    else:
        print("You have guessed wrong! You are eaten alive by the dragon!")
        return(coin<0)



#team5
def airlessCave(coin):
    
    import time
    print("You entered the cave...")
    time.sleep(2)
    print("You hear silence at first...")
    time.sleep(2)
    print("You find yourself running out of air!")
    time.sleep(2)
    print("Suddenly, a dragon shows up, and tells you that unless you have 120 coins for air, you'll die from lack of oxygen...")
    time.sleep(2)
    if coin >= 120:
        print("You pay the dragon 120 coins! Oxygen hooray!")
        return(int(coin)-120)
        print("You have" + str(coin) + " gold coins left!")
    else:
        print("You don't have enough gold coins to pay the dragon for air, and therefore you die from lack of oxygen! BYE!")
        return(int(coin))


#team6
def waterlessCave(coin):
    days = random.randint(1,10)
    print("You are trapped!")
    print("The cave you are in has no water in it")
    print("You will need to buy water to survive.")

    for x in range(0, days):
        if coin > 0:
            print("This is day number " + str(days) + " of being trapped in this cave.")
            print("A wizard appears.  He is selling water bottles.")
            pay = input("Pay 20 gold coins for a water bottle? ")
            if pay == "no":
                coin = int(-1)
            else:
                coin = coin - 20
    if coin > 0:
        print("You have " + str(coin) + " gold coins left.")
    return coin 


#team7

#define main function
def main():
    count=0
    kg = "yes"
    dead = False
    startingMoney = 150
    displayintro()

#loop for choosing caves
    while (count<3) and !dead and kg = "yes":
        choiceQuestion = ()
        caveNumber = chooseCave()
        reportDead = checkCave(caveNumber) or money<0
        endMoney = 150 + money
        kg=input("keep going, yes or no?")
        count+=1
        
#report end money and print end of game
    print("The final ammount of money you have is " + str(endMoney) + " dollars.")
    print("Thanks for playing!")


