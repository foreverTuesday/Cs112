def main():
    print("Rendering text file.  Please stand by.")
    text = []
    f = open('my immortal full.txt')

    for line in f:

        for word in line.split():
            word = strip_punctuation(word)
            word = str.casefold(word)
            word = fWords(word)
        for k in line:
            if k != '':
                text.append(word)
    print(word)
    f.close()
    num = 0

    
    input("Text file rendered.  Press enter to continue.")
    check = str.casefold(input("What word would you like to check? "))
    for x in text:
        if x==check:
            num=num+1
    print(check + " shows up " + str(num) + " times.")       


def fWords(word):
    w = open('function words.txt')
    for line in w:
        line = line.rstrip()
    line = strip_ew(line)
    w.close
    for item in w:
        if word == item:
            word = ''
    return(word)

def strip_ew(line):
    for why in line:
        line = ""
    return(line)


def strip_punctuation(word):
        newWord = ""
        punc = [".",",","?","!",";",":","}"]

        for letter in word:
            if letter not in punc:
                newWord = newWord + letter

        return (newWord)
