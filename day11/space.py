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
    numRows, numColumns = getSize()
    for i, row in enumerate(input):
        row = row.rstrip()
        prevSpace = True
        
        for j, column in enumerate(row):
            if column == '.':
                for c in range(0, 9):
                    if row[c] == '.' and prevSpace == True:
                        prevSpace = True
                    else:
                        prevSpace = False
            if column in '#':
                coordinates.append((i, j))
                
        if prevSpace == True:
            lineYN.append(i)
            










    print(coordinates)
    print(numRows)
    print(numColumns)
    print(lineYN)

if __name__ == '__main__':
    main()