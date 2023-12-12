def getSize():
    input = open('day11/test.txt', 'rt')
    numRows = 0
    numColumns = 0
    for line in input:
        numRows += 1
        for numColumns in range(0, len(line)):
            numColumns += 1
    return numRows, numColumns




def main():
    input = open('day11/test.txt', 'rt')
    coordinates = []
    lineYN = []
    rows = []
    numRows, numColumns = getSize()
    
    input = open('day11/test.txt', 'rt')
    for row in input:
        row = row.rstrip()
        rows.append(row)

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
            lineYN.append(i)
                    
    input.close()

    print(coordinates)
    print(lineYN)





if __name__ == '__main__':
    main()