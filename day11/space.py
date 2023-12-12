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

def getOpenRows(rows, openRows):
    for i, row in enumerate(rows):
        if not '#' in row:
            openRows.append(i)

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
    input.close()

    print(coordinates)
    print(openColumns)
    print(openRows)





if __name__ == '__main__':
    main()