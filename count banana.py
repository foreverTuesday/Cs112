def main():
    input("press enter to hear a joke")
    print("Knock , Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Orange . Orange who ? Orange you glad I didn't say Banana again ?  ")
    joke = []
    f = open('banana.txt')
    for line in f:
        for word in line.split():
            joke.append(word)
    f.close()
    num = 0
    input("Press enter to check how many times a word showed up")
    check = input("What word in the joke would you like to check? ")
    for x in joke:
        if x==check:
            num=num+1
    print(check + " shows up " + str(num) + " times in the joke.")
