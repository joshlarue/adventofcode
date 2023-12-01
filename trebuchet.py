input = open("trebuchetinput.txt", "rt")
arrLine = []

for line in input:
    line = line.rstrip()
    arrLine.append(line)

print(arrLine)
input.close()