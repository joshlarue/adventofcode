def getSize():
    input = open('day11/input.txt', 'rt')
    numRows = 0
    numColumns = 0
    for line in input:
        numRows += 1
        for numColumns in range(0, len(line)):
            numColumns += 1
    input.close()
    return numRows, numColumns

def getOpenColumns(rows, openColumns):
    for i, item in enumerate(rows):
        prevSpace = True

        if item[i] == '.':
            for n, blank in enumerate(rows):
                if rows[n][i] == '.' and prevSpace == True:
                    prevSpace = True
                else:
                    prevSpace = False
        if prevSpace == True:
            openColumns.append(i)
    return openColumns

def getGalaxies(rows, coordinates):
    for i, items in enumerate(rows):
        for j, char in enumerate(items):
            if char in '#':
                coordinates.append((i, j))
    return coordinates

def insertColumns(rows, openColumns):
    colOffset = 0
    for i in range(0, len(openColumns)):
        for j, row in enumerate(rows):
            colToInsert = rows[j]
            newCol = colToInsert[:openColumns[i]+colOffset] + '.' + colToInsert[openColumns[i]+colOffset:]
            rows[j] = newCol
        colOffset += 1

def getOpenRows(rows, openRows):
    for i, row in enumerate(rows):
        if not '#' in row:
            openRows.append(i)
    
def insertRows(rows, openRows, numColumns):
    for i in range(0, len(openRows)):
        rows.insert(openRows[i]+1, '.'*numColumns)

def setGalaxyNums(rows):
    numberedGalaxies = []
    galaxyNum = 1
    for i, row in enumerate(rows):
        numberedLine = list(row)
        for j, char in enumerate(numberedLine):
            if char == '#':
                numberedLine[j] = f'{galaxyNum}'
                galaxyNum += 1
        numberedGalaxies.append(''.join(numberedLine))
    return numberedGalaxies

def findClosest(coordinates):
    shortestPaths = 0
    numPairs = 0
    usedCoords = []
    for i in range(len(coordinates)-1):
        currentX = coordinates[i][0]
        currentY = coordinates[i][1]
        for j in range(len(coordinates)-1):
            nextX = coordinates[j+1][0]
            nextY = coordinates[j+1][1]
            if numPairs < ((len(coordinates)-1)*(len(coordinates)))/2 and (currentX, currentY) != (nextX, nextY) and sorted([currentX, currentY, nextX, nextY]) not in usedCoords:
                print(currentX, currentY, nextX, nextY)
                pathX = abs(nextX - currentX)
                pathY = abs(nextY - currentY)
                pathLength = pathX + pathY
                print(pathLength)
                shortestPaths += pathLength
                numPairs += 1
                usedCoords.append(sorted([currentX, currentY, nextX, nextY]))
    print(numPairs)
    return shortestPaths
        

def main():
    coordinates = []
    openRows = []
    openColumns = []
    rows = []
    numRows, numColumns = getSize()
    
    input = open('day11/input.txt', 'rt')
    for row in input:
        row = row.rstrip()
        rows.append(row)
    input.close()

    getOpenColumns(rows, openColumns)
    getOpenRows(rows, openRows)
    insertRows(rows, openRows, numColumns)
    insertColumns(rows, openColumns)
    getGalaxies(rows, coordinates)
    setGalaxyNums(rows)
    shortestPaths = findClosest(coordinates)


    print(coordinates)
    print(openColumns)
    print(openRows)
    print(shortestPaths)
    for row in rows:
        print(row)





if __name__ == '__main__':
    main()