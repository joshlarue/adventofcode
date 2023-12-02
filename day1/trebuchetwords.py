input = open("trebuchetinput.txt", "rt")
arrLine = []
result = 0
numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

for line in input:
    line = line.rstrip()
    arrLine.append(line)
input.close()

# for item in arrline
#   loop through the array forwards in 3, 4, and 5 sized chunks
#       for number in numbers
#           if number in chunk3
#               firstNum = numbers[number].value()? idk

for item in arrLine:
    firstNum = 0
    secondNum = 0
    localResult = ''
    #for item in arrLine:
    i = 0
    for i in range(0, len(item)):
        if item[i].isdigit():
            firstNum = item[i]
            break
        threeChunk = item[i:3] # what happens if this goes beyond the end of the string?
        fourChunk = item[i:4]
        fiveChunk = item[i:5]
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
    

    #localResult += secondNum
    #localResult += firstNum
    #result += int(localResult)

#print(result)