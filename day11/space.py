input = open('day11/test.txt', 'rt')
numRows = 0
numColumns = 0
coordinates = []

for i, row in enumerate(input):
    numRows += 1
    row = row.rstrip()
    for j, column in enumerate(row):
        if i == 1:
            numColumns += 1
        if column in '#':
            coordinates.append((i, j))


print(coordinates)
print(numRows)
print(numColumns)