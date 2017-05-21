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
    v=0
    startVal=startTurn(used)
    runVal=totalVal(used,startVal, v)
    turn(used,startVal,v)
    print(used)

def turn(used,runVal,v):
    go=1
    while runVal<21 and go==1:
        go=hit_check()
        if go==1:
            v=hit(used)
            runVal=totalVal(used,runVal, v)


def hit_check():
    more=input("Would you like to draw another card?\n")
    if more=="yes":
        hitme=1
        return(hitme)


def totalVal(used,startVal, v):
    runVal=startVal+v
    aceSeek=Ace(used)
    if aceSeek==1:
        print("The current value of your hand is " +str(runVal)+" or "+str(runVal+10))
    else:
        print("The current value of your hand is " +str(runVal))
    return(runVal)


def Ace(used):
    aC=2
    for x in used:
        if "Acd" in x:
            aC=1
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
    if len(used)==57:
        input("You have used the entire deck :(")
        exit(main)
    if cCode in used:
        isnew='n'
    else:
        used.append(cCode)
        isnew='y'
    return(isnew)
