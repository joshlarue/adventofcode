input = open("trebuchetinput.txt", "rt")
arrLine = []
result = 0

for line in input:
    line = line.rstrip()
    arrLine.append(line)
input.close()

for item in arrLine:
    firstNum = 0
    secondNum = 0
    localResult = ''
    for char in item:
        if char.isnumeric():
            firstNum = char
    for char in reversed(item):
        if char.isnumeric():
            secondNum = char
    localResult += secondNum
    localResult += firstNum
    result += int(localResult)

print(result)