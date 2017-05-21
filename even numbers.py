def main():
    f = open('numbers.txt')
    lines = f.readlines()
    lines = stripNewLinesMakeNumbers(lines)
    f.close()
    print(lines)
    list2 = even(lines)
    print(list2)
    list2 = even2(lines)
    print(list2)
    list2 = even3(lines)
    print(list2)


def stripNewLinesMakeNumbers(lines):
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())
    return(lines)



def even(lines):
    list2 = []
    for x in lines:
        if x%2 == 0:
            list2.append(x)
    return list2

        
def even2(lines):
    list2 = []
    x=0
    while(x<len(lines)):
        test = lines[x]
        if test%2 == 0:
            list2.append(test)
        x=x+1
    return list2

def even3(lines):
    list2 = []
    for x in range(len(lines)):
        test = lines[x]
        if test%2 == 0:
            list2.append(test)
    return list2
