SPECIAL_CHARS = '!@#$%^&*?/=-_~`\{}[]()<>'
# or use if not .isalnum()?
input = open("day3/test.txt", "rt")

def getLineNumList():
    nums = ''
    # if width of number +1 or -1 = special char then add
    for line in input:
        i = 0
        for i in range(0, len(line)):
            if line[i].isdigit() or line[i] in SPECIAL_CHARS:
                nums += line[i]
            if line[i] == '.' and line[i-1].isdigit():
                nums += ' '
        checkIfBeside(nums)

def checkIfBeside(list):
    i = 0
    for i in range(0, len(list)):
        if (list[i].isdigit() and list[i-1] in SPECIAL_CHARS) or (list[i].isdigit() and list[i+1] in SPECIAL_CHARS):
            pass



getLineNumList()
checkIfBeside()

input.close()