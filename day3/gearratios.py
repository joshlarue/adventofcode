SPECIAL_CHARS = '!@#$%^&*?/=-_~`\{}[]()<>'
# or use if not .isalnum()?
input = open("day3/test.txt", "rt")

twoD = []

for line in input:
    line = line.rstrip()
    twoD.append(line)
print(twoD)

i = 0
j = 0
for i in range(0, len(twoD[0])):
    for j in range(0, len(twoD)):
        # this could probably be done better
        # keep getting index out of range error when i=9
        if i > 0 or j > 0 or i < 9 or j < 9:
            if (twoD[i][j].isdigit() and twoD[i+1][j] in SPECIAL_CHARS) or (twoD[i][j].isdigit() and twoD[i][j+1] in SPECIAL_CHARS) or (twoD[i][j].isdigit() and twoD[i+1][j+1] in SPECIAL_CHARS):
                print("add!")
        elif i == 0 or j == 0 or i == 9 or j == 9:
            pass
            #if (twoD[i][j].isdigit() and twoD[])

input.close()