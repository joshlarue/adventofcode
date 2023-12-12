def getSize():
    input = open('day11/test.txt', 'rt')
    numRows = 0
    numColumns = 0
    for line in input:
        numRows += 1
        for numColumns in range(0, len(line)):
            numColumns += 1
    return numRows, numColumns

def getGalaxiesAndOpenColumns(rows, coordinates, openColumns):
    for i, item in enumerate(rows):
        prevSpace = True

        for j, char in enumerate(item):
            if char in '#':
                coordinates.append((i, j))

        if item[i] == '.':
            for n, blank in enumerate(rows):
                if rows[n][i] == '.' and prevSpace == True:
                    prevSpace = True
                else:
                    prevSpace = False
        if prevSpace == True:
            openColumns.append(i)

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


def main():
    input = open('day11/test.txt', 'rt')
    coordinates = []
    openRows = []
    openColumns = []
    rows = []
    numRows, numColumns = getSize()
    
    input = open('day11/test.txt', 'rt')
    for row in input:
        row = row.rstrip()
        rows.append(row)

    getGalaxiesAndOpenColumns(rows, coordinates, openColumns)
    getOpenRows(rows, openRows)
    insertRows(rows, openRows, numColumns)
    insertColumns(rows, openColumns)
    rows = setGalaxyNums(rows)
    input.close()

    print(coordinates)
    print(openColumns)
    print(openRows)
    for row in rows:
        print(row)





if __name__ == '__main__':
    main()