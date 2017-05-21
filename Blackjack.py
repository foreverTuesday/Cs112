#use function to define a deck of cards
    #randomly chosen number 1-4 to denote suit (use dictionary or list)
    #randomly chosen number to denote number (use dictionary or list)
#function to check total value of cards(aces are 1 or 11), say if it's over 21
#function to allow player to hit or stay
#function to start by dealing out two cards to a player
#make sure cards get removed from the deck

import random
#cardNum is numbers 0-12
cardNum = ['Ace','two','three','four','five','six',\
           'seven','eight','nine','ten','jack','queen','king']
Suit = ['hearts','spades','diamonds','clubs']
cValue =  {'Ace':1,'two':2,'three':3,'four':4,\
           'five':5,'six':6,'seven':7,'eight':8,\
           'nine':9,'ten':10,'jack':10,'queen':10,'king':10}
def main():
    used = ['joker']
    instruct()
    print("it is player one's turn")
    p1=game(used)
    print("it is player two's turn")
    p2=game(used)
    win(p1,p2,used)


def win(p1,p2,used):
    if p1>21 and p2>21:
        print("Both players went over 21.  There is no winner.")
    elif p1==p2:
        print("Both players tied.")
    aceCheck=Ace(used)
    if aceCheck>0:
        pass
    elif p1>p2:
        print("Player one wins.")
    else:
        print("Player two wins.")
    f = open("winners.txt",'w')
    f.write("glue")
    f.close()
    

def instruct():
    print("This is a two player game of Blackjack.")
    print("The goal of the game is to get your hand value \
as close to 21 as possible without going over")
    print("You will start with a hand of two cards.")
    print("You will then have the option to draw more cards one at a time.")
    input("Press enter when you are ready to begin.")


def maxBet():
    again = input("Would you like to play again?\n")
    return(again)

def game(used):
    v=0
    again="yes"
 #   again=maxBet()
    while again=="yes":
        again="no"
        startVal=startTurn(used)
        runVal=totalVal(used,startVal, v)
        game=turn(used,startVal,v)
        Ace(used)
    return(game)
 #       again=maxBet()
    

def turn(used,runVal,v):
    go=1
    while runVal<21 and go==1:
        go=hit_check()
        if go==1:
            v=hit(used)
            runVal=totalVal(used,runVal, v)
    if runVal<12:
        aceCheck=Ace(used)
        if aceCheck>0:
            runVal=runVal+110
    return(runVal)


def hit_check():
    more=input("Would you like to draw another card?\n")
    if more=="yes":
        hitme=1
        return(hitme)


def totalVal(used,startVal, v):
    runVal=startVal+v
    aceSeek=Ace(used)
    if aceSeek>0 and runVal<12:
        print("The current value of your hand is " +str(runVal)+" or "+str(runVal+10))
    else:
        print("The current value of your hand is " +str(runVal))
    return(runVal)


def Ace(used):
    aC=0
    for x in used:
        if "Ace" in x:
            aC=used.index(x)
    return aC


def hit(used):
    (s,n)=draw(used)
    print("You have drawn the "+n+" of "+s)
    v=addval(n)
    return(v)
    

def addval(card):
    v = cValue[card]
    return(v)
    
    
def startTurn(used):
    (s1,n1)=draw(used)
    c1_val=addval(n1)
    (s2,n2)=draw(used)
    c2_val=addval(n2)
    startVal=c1_val+c2_val
    print("You have drawn the "+n1+" of "+s1+" and the "+n2+" of "+s2)
    return(startVal)
    
    

def draw(used):
    isnew = 'n'
    while isnew == 'n':
        (suit, num) = cards()
        (isnew) = remove(suit,num,used)
    return(suit,num)
    

def cards():
    rawSuit = random.randint(0,3)
    suit = Suit[rawSuit]
    rawNum = random.randint(0,12)
    num = cardNum[rawNum]
    return(suit,num)


def remove(suit,num,used):
    cCode = suit+num
    isnew = 'null'
    if len(used)==53:
        print("You have used the entire deck :(")
        print("Reshuffling")
        used=["joker"]
    if cCode in used:
        isnew='n'
    else:
        used.append(cCode)
        isnew='y'
    return(isnew)
