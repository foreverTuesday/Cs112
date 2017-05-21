import random
cardNum = ['Ace','two','three','four','five','six',\
           'seven','eight','nine','ten','jack','queen','king']
Suit = ['hearts','spades','diamonds','clubs']
cValue =  {'Ace':1,'two':2,'three':3,'four':4,\
           'five':5,'six':6,'seven':7,'eight':8,\
           'nine':9,'ten':10,'jack':10,'queen':10,'king':10}

#start objects here

class Cards:
    def __init__(self,n,a):
        self.suit=n
        self.num=a
    def __str__(self):
        return(self.num + " of " +self.suit)

class Player:
    def __init__(self,p,q,r,s):
        self.name=p
        self.hand=q
        self.val=r
        self.win=s
    def __str__(self):
        return(self.name+" has a hand containing the following cards:\n"\
               +str(self.hand)+"\nThis hand is worth "+str(self.val)+" points")

#start functions here    

def main():
    instruct()
    print("Player 1, ",end="")
    name1=player()
    print("Player 2, ",end="")
    name2=player()
    multiG(name1,name2)   
    

##### GAMES #####
def multiG(name1,name2):
    deck=[]
    deckbuild(deck)
    more="yes"
    g1=0
    g2=0
    while more=="yes":
        if len(deck)<13:
            print("Shuffling Deck")
            print()
            while len(deck)>0:
                deck.pop()
            deckbuild(deck)
        hand1=[]
        hand2=[]
        tTrack=1
        tSwap(name1,name2,tTrack)
        ACES = turn(tTrack,hand1,hand2,deck)
        v1=aVal(ACES,hand1,hand2,tTrack)
        tTrack=2
        tSwap(name1,name2,tTrack)
        ACES = turn(tTrack,hand1,hand2,deck)
        v2=aVal(ACES,hand1,hand2,tTrack)
        (p1,p2)=showALL(name1,name2,hand1,hand2,v1,v2,g1,g2)
        (g1,g2)=win(p1,p2,g1,g2)
        (p1,p2)=showALL(name1,name2,hand1,hand2,v1,v2,g1,g2)
        more=input("Would the two of you like to play again? [yes/no]\n")
        while more!="yes" and more!="no":
            print("That is not a valid answer.")
            more=input("Would the two of you like to play again? [yes/no]\n")
            
    print(p1.name+" won "+str(p1.win)+" games.  "+p2.name+" won "+str(p2.win)+" games.")
##### GAMES #####


def instruct():
    print("This is a two player game of Blackjack.")
    print("The goal of the game is to get your hand value \
as close to 21 as possible without going over")
    print("You will start with a hand of two cards.")
    print("You will then have the option to draw more cards one at a time.")
    input("Press enter when you are ready to begin.")


def tSwap(name1,name2,tTrack):
    if tTrack==1:
        print("It is now "+name1+"'s turn")
        input(name1+", please press enter to start playing")
    else:
        print("It is now "+name2+"'s turn")
        input(name2+", please press enter to start playing")


##### ACES ####
def aCheck(hand1,hand2,tTrack,hval):
    aces="false"
    if hval<12:
        if tTrack==1:
            for x in hand1:
                if "Ace" in str(x):
                    aces="true"
                    print("The current value of your hand is " +str(hval)+" or "+str(hval+10))
                    return(aces)
        else:
            for x in hand2:
                if "Ace" in str(x):
                    aces="true"
                    print("The current value of your hand is " +str(hval)+" or "+str(hval+10))
                    return(aces)
    return(aces)

def aShow(hand1,hand2,tTrack,hval):
    if tTrack==1:
        print("Your hand for the turn is worth "+str(hval+10))
        print("Your final hand is the following cards: ")
        for x in hand1:
            print(x)
        print()
    else:
        print("Your hand for the turn is worth "+str(hval+10))
        print("Your final hand is the following cards: ")
        for x in hand2:
            print(x)
        print()

def aVal(aces,hand1,hand2,tTrack):
    runV=totalVal(hand1,hand2,tTrack)
    if aces=="true":
        runV=runV+10
    return(runV)   
##### ACES ####

def turn(tTrack,hand1,hand2,deck):
    run="a"
    draw(deck,hand1,hand2,tTrack)
    draw(deck,hand1,hand2,tTrack)
    hval=totalVal(hand1,hand2,tTrack)

    AAA=aCheck(hand1,hand2,tTrack,hval)
    if AAA == "false":
        print("The value of your hand is currently "+str(hval))
    while hval<21 and run=="a":
        hitme=input("Would you like to draw another card? [yes/no]\n")
        if hitme=="no":
            run="b"
        if hitme=="yes":
            draw(deck,hand1,hand2,tTrack)
            hval=totalVal(hand1,hand2,tTrack)
            AAA=aCheck(hand1,hand2,tTrack,hval)
            if AAA == "false":
                print("The value of your hand is currently "+str(hval))
                        
    if AAA=="true":
        aShow(hand1,hand2,tTrack,hval)
    else:
        hShow(hand1,hand2,tTrack,hval)
    return(AAA)

def hShow(hand1,hand2,tTrack,hval):
    if tTrack==1:
        print("Your hand for the turn is worth "+str(hval))
        print("Your final hand is the following cards: ")
        for x in hand1:
            print(x)
        print()
    else:
        print("Your hand for the turn is worth "+str(hval))
        print("Your final hand is the following cards: ")
        for x in hand2:
            print(x)
        print()
    
    
    
def win(p1,p2,g1,g2):
    winner="no one"
    if p1.val>21 and p2.val>21:
        print("Both players went over 21.  There is no winner.")
    else:
        if p1.val==p2.val:
            print("Both players tied.")
        elif p1.val>p2.val and p1.val<22:
            print(p1.name+" wins")
            winner=p1.name
            g1=p1.win+1
        else:
            print(p2.name+" wins")
            winner=p2.name
            g2=p2.win+1
    f = open("winners.txt",'w')
    f.write("The winner is "+winner)
    f.close()
    return(g1,g2)
    



def draw(deck,hand1,hand2,tTrack):
    card=deck.pop()
    if tTrack==1:
        hand1.append(card)
        print("You have drawn the "+card.num+" of "+card.suit)
    else:
        hand2.append(card)
        print("You have drawn the "+card.num+" of "+card.suit)
        

def player():
    pn=input("what is your name?\n")
    return(pn)


def showALL(name1,name2,hand1,hand2,v1,v2,g1,g2):
    p1=Player(name1,hand1,v1,g1)
    p2=Player(name2,hand2,v2,g2)
    return(p1,p2)


def deckbuild(deck):
    for x in Suit:
        for y in cardNum:
            c=Cards(x,y)
            deck.append(c)
    random.shuffle(deck)

#############Value of hand section################
def totalVal(hand1,hand2,tTrack):
    runV=0
    if tTrack==1:
        for x in hand1:
            number=x.num
            v = cValue[number]
            runV=runV+v
        return(runV)
    else:
        for x in hand2:
            number=x.num
            v = cValue[number]
            runV=runV+v
        return(runV)
