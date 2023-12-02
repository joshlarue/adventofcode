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
    gameArr.pop(0)
    for item in gameArr:
        setArr = item.split(",")
        print(setArr)
        for color in setArr:
            localRed = ''
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
    if not (int(localRed) > numRed) or (int(localGreen) > numGreen) or (int(localBlue) > numBlue):
        sumID += gameID
print(sumID)