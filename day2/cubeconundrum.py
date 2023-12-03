input = open("day2/test.txt", "rt")
lineNum = 1
sumID = 0

for line in input:
    gameID = lineNum
    line = line.replace(":", ";")
    gameArr = line.split(";")
    numRed = []
    numGreen = []
    numBlue = []
    print(line)
    gameArr.pop(0) # gets rid of the game label so that gameArr is just an array of each game's colors
    for item in gameArr:
        setArr = item.split(",") # splits the game up into each set of blocks
        localRed = '' # using strings so that I can easily push multiple consecutive digits
        localGreen = ''
        localBlue = ''
        for color in setArr:
            if 'red' in color:
                for char in color:
                    if char.isdigit(): localRed += char
            if 'green' in color:
                for char in color:
                    if char.isdigit(): localGreen += char
            if 'blue' in color:
                for char in color:
                    if char.isdigit(): localBlue += char
        if localRed == '': localRed = 0 # if there was no color of the specified type, set to 0, otherwise this causes typeerrors
        if localGreen == '': localGreen = 0
        if localBlue == '': localBlue = 0
        # create array of number of colors for each set and loop through to find lowest number
        # will have to be array of just that color
        #dictIter = {}
        #dictIter[localRed, localGreen, localBlue] = gameArr, gameArr, gameArr
        #print(dictIter)

        numRed.append(int(localRed))
        numGreen.append(int(localGreen))
        numBlue.append(int(localBlue))
    print(numRed, numGreen, numBlue)
    numRed.sort()
    numGreen.sort()
    numBlue.sort() # NEED TO ACCOUNT FOR 0s
    print(numRed, numGreen, numBlue)
    powerOfSet = numRed[0] * numGreen[0] * numBlue[0]
    print(powerOfSet)
    lineNum += 1