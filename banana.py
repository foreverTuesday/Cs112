def main():
    love = {"Knock":"♪","Who's":"♥","there":"♣","Banana":"☆","who":"♡","Orange":"❂","you":"✌","glad":"☺","I":"☃","didn't":"☮","say":"❄","again":"♙",",":",",".":".","?":"?"}
    joke = []
    f = open('banana.txt')
    for line in f:
        for word in line.split():
            joke.append(word)
    f.close()
    print(joke)
    for x in joke:
        print(love[x], end="")
