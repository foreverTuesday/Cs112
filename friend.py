class Friend:
    def __init__(self,n,a,m):
        self.name=n
        self.phone=a
        self.age=m
    def __str__(self):
        return(self.name+", age: "+str(self.age)+", phone #"+self.phone)

def oldmain():
    List=[]
    morefriends="yes"
    while morefriends=="yes":
        f=makeAFriend()
        print(f)
        cobra.append(f)
        morefriends=input("Make more friends????? [yes/no]\n")
    print("These are all of your friends:")
    for x in cobra:
        print(x)
    pickF(cobra)

def main():
    List=[]
    cobra=[]
    readFriend(List)
    defFriend(List,cobra)
    dateF(cobra)

def defFriend(List,cobra):
    x=0
    while x<3:
        name=List[3*x]
        phone=List[3*x+1]
        age=List[3*x+2]
        f=Friend(name,phone,age)
        cobra.append(f)
        x=x+1


def readFriend(List):
    f = open('friends.txt')
    for line in f:
        for word in line.split():
            List.append(word)
    f.close()


def dateF(cobra):
    nam=int(input("How old are you?\n"))
    uplim=Up(nam)
    lowlim=Low(nam)
    goodDate(cobra,lowlim,uplim)
    


def goodDate(cobra,lowlim,uplim):
    if uplim <= lowlim:
        print("You are too young to date.")
    else:
        print("Out of all of your friends, you can date...")
        for x in cobra:
            if int(x.age)<uplim and int(x.age)>lowlim:
                print(x.name)
        print("That's everyone!")
        
              

def Up(test):
    uplim = (test - 7)*2
    return(uplim)

def Low(test):
    lowlim = 7 + test/2
    return lowlim



#friend1.age>friend2.age
#cobra[1].name
