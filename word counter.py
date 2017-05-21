def main():
    text = []
    f = open('My immortal full.txt')

    for line in f:

        for word in line.split():
            word = strip_punctuation(word)
            word = str.casefold(word)
            text.append(word)
    f.close()
    num = 0
    input("Press enter to check how many times a word showed up")
    check = str.casefold(input("What word would you like to check? "))
    for x in text:
        if x==check:
            num=num+1
    print(check + " shows up " + str(num) + " times.")


def strip_punctuation(word):
        newWord = ""
        punc = [".",",","?","!",";",":"]

        for letter in word:
            if letter not in punc:
                newWord = newWord + letter

        return (newWord)

