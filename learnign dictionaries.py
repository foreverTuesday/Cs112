def main():
    npDict = {"jordan":"dog",'nate':'fish','shana':'plant'}
    print(npDict['jordan'])

    keys = npDict.keys()
    for key in keys:
        print(key + " has a pet " +npDict[key])

    values = npDict.values()
    print("pets:", end=" ")
    for value in values:
        print(value, end = ",")

