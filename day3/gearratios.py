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
for i in range(0, len(twoD)):
    for j in range(0, len(twoD[0])):
        # this could probably be done better
        # keep getting index out of range error when i=9
        if twoD[i][j].isdigit() and any(twoD[x][y] in SPECIAL_CHARS
                                        for x in range(max(0, i-1), min(len(twoD), i+2))
                                        for y in range(max(0, j-1), min(len(twoD[0]), j+2))):
            print("add!")

input.close()