#define list of names
#get user to input the name
#check list for name
#tell user where on the list it is

def main():
    STNMBL=-1
    tourist_trapped()
    journal_3 = ['Stan','Ford','Mabel','Dipper','Soos','Wendy','Robbie','Grenda','Candy','Pacifica','Waddles','Tad Strange','Gideon','Bill']
    Tyrone = input("What name would you like to check? ")
    if(Tyrone in journal_3):
        STNMBL=journal_3.index(Tyrone)
        print("Was it on the list?")
        print("Yes")
        print("Definitely!")
        print("ABSOLUTELY!!!!!")
        print("That name was in position #" + str(STNMBL) + " on the list")
    else:
        print("Why you ackin' so cray-cray?")
        print("That name isn't on the list.")
    Cheekums = journal_3[0]
    for index in range(0, len(journal_3)):
        if journal_3[index]:
            Cheekums = journal_3[index]
    print('Alphabetically, the first name on the list is ' + Cheekums)

    

def tourist_trapped():
    print("This program will check if a name is on a list.")
