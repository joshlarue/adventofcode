input = open("day1/trebuchetinput.txt", "rt")
arrLine = []
result = 0
numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

for line in input:
    line = line.rstrip()
    arrLine.append(line)
input.close()

for item in arrLine:
    localResult = ''
    firstNum = 0
    secondNum = 0
    i = 0
    for i in range(0, len(item)):
        if item[i].isdigit():
            firstNum = item[i]
            break
        threeChunk = item[i:i+3] # what happens if this goes beyond the end of the string?
        fourChunk = item[i:i+4]
        fiveChunk = item[i:i+5]
        if threeChunk in numbers:
            firstNum = numbers[threeChunk]
            break
        if fourChunk in numbers:
            firstNum = numbers[fourChunk]
            break
        if fiveChunk in numbers:
            firstNum = numbers[fiveChunk]
            break
    print(firstNum)
    localResult += str(firstNum)
    
    for i in range(len(item), 0, -1):
        if item[i-1].isdigit():
            secondNum = item[i-1]
            break
        threeChunk = item[i-3:i]
        fourChunk = item[i-4:i]
        fiveChunk = item[i-5:i]
        if threeChunk in numbers:
            secondNum = numbers[threeChunk]
            break
        if fourChunk in numbers:
            secondNum = numbers[fourChunk]
            break
        if fiveChunk in numbers:
            secondNum = numbers[fiveChunk]
            break
    print(secondNum)
    localResult += str(secondNum)
    result += int(localResult)
print(result)