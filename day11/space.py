input = open('day11/test.txt', 'rt')
numRows = 0
numColumns = 0
for i, row in enumerate(input):
    numRows += 1
    row = row.rstrip()
    for column in row:
        if i == 1:
            numColumns += 1



print(numRows)
print(numColumns)