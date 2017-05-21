def main():
    listt = ['Nanette','Waldo','Bob','Arthur','Waldo']
    print("waldo is at index " + str(listt.index('Waldo')))
    index = 0
    count = 0
    target = 'Waldo'
    while index<len(listt):
        if listt[index]==target:
            count+=1
        index+=1

    if(count>0):
        print(target + "appears " + str(count) + " times")
    else:
        print("couldn't find ", target)
