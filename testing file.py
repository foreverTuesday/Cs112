import random
cardNum = ['Ace','two','three','four','five','six',\
           'seven','eight','nine','ten','jack','queen','king']
Suit = ['hearts','spades','diamonds','clubs']
cValue =  {'Ace':1,'two':2,'three':3,'four':4,\
           'five':5,'six':6,'seven':7,'eight':8,\
           'nine':9,'ten':10,'jack':10,'queen':10,'king':10}

pSuit= {'hearts':"♥",'spades':"♠",'diamonds':"♦",'clubs':"♣"}
pNum =  {'Ace':"A",'two':"2",'three':"3",'four':"4",\
           'five':"5",'six':"6",'seven':"7",'eight':"8",\
           'nine':"9",'ten':"T",'jack':"J",'queen':"Q",'king':"K"}


TEST="n"
x="♥"
y="K"

'{:^30}'.format('centered')
'{:<30}'.format('left aligned') 
'{:>30}'.format('right aligned')

handsize=3

if TEST=="n":
#for a in Suit:
    if TEST=="n":
    #for b in cardNum:
        #x=pSuit[a]
        #y=pNum[b]
        
        print('{:^3}'.format("|▔▔▔|"))
        print('{:^5}'.format("|  "+x+"  |"))
        print('{:^5}'.format("|  "+y+"  |"))
        print('{:^5}'.format("|_____|"))
        print("\n")



w=0
while w<=handsize:
    print('{:2}'.format("|▔▔▔|"),end=" ")
    w=w+1
print("\n",end="")

w=0
while w<=handsize:
    print('{:>2}'.format("|  "+x+"  |"),end=" ")
    w=w+1

print("\n",end="")
w=0
while w<=handsize:
    print('{:<2}'.format("|  "+y+"  |"),end=" ")
    w=w+1

print("\n",end="")
w=0
while w<=handsize:
    print('{:^2}'.format("|_____|"),end=" ")
    w=w+1




#print("\n")
#print('{:^30}'.format('test'))

#for x in range(1, 11):
    #print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#       card=("|▔▔▔|\n|  "+x+"  |\n|  "+y+"  |\n|_____|"+"\n")
