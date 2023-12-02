numRed = 12
numGreen = 13
numBlue = 14
input = open("blockbag.txt", "rt")

lineNum = 1
sumID = 0
for line in input:
    gameID = lineNum
    lineNum += 1
    line = line.replace(":", ";")
    gameArr = line.split(";")
    gameArr.pop(0) # gets rid of the game label so that gameArr is just an array of each game's colors
    for item in gameArr:
        setArr = item.split(",") # splits the game up into each set of blocks
        print(setArr)
        for color in setArr:
            localRed = '' # using strings so that I can easily push multiple consecutive digits
            localGreen = ''
            localBlue = ''
            if 'red' in color:
                for char in color:
                    if char.isdigit(): localRed += char
                print(localRed)
            if 'green' in color:
                for char in color:
                    if char.isdigit(): localGreen += char
                print(localGreen)
            if 'blue' in color:
                for char in color:
                    if char.isdigit(): localBlue += char
                print(localBlue)
            if localRed == '': localRed = 0 # if there was no color of the specified type, set to 0, otherwise this causes typeerrors
            if localGreen == '': localGreen = 0
            if localBlue == '': localBlue = 0
            if (int(localRed) < numRed) and (int(localGreen) < numGreen) and (int(localBlue) < numBlue):
                sumID += gameID
print(sumID)