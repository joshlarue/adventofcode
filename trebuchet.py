input = open("trebuchetinput.txt", "rt")

# line = 1
# 
# line.rstrip
# 

for line in input:
    line = line.rstrip()
    firstChar = False
    while firstChar == False:
        for char in line:
            if char.isnumeric():
                print(char)
                firstChar = True


input.close()