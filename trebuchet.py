input = open("trebuchetinput.txt", "rt")
arrLine = []

for line in input:
    line = line.rstrip()
    arrLine.append(line)

print(arrLine)
input.close()

for item in arrLine:
    firstNum = 0
    secondNum = 0
    localResult = []
    for char in item:
        if char.isnumeric():
            firstNum = char
    for char in reversed(item):
        if char.isnumeric():
            secondNum = char
    localResult.append(secondNum)
    localResult.append(firstNum)
    print(localResult)