def part1(filePath):
    fileToRead = open(filePath,"r")
    sum = 0
    for line in fileToRead.readlines():
        newLine = line.replace("\n","")
        firstHalf, secondHalf = newLine[:len(newLine)//2],newLine[len(newLine)//2:]
        for i in range(0, len(firstHalf)):
            if firstHalf[i] in secondHalf:
                commonLetter = firstHalf[i]
                if('A' <= commonLetter <= "Z"):
                    sum += ord(commonLetter) - 38
                else:
                    sum += ord(commonLetter) - 96
                break
    fileToRead.close()
    return sum

def functionOccurence(linesTriples):
    value = 0
    commonLetter = ""
    for i in range(0,len(linesTriples[0])):
        for j in range(0,len(linesTriples[1])):
            for z in range(0,len(linesTriples[2])):
                if(linesTriples[0][i] == linesTriples[1][j] and linesTriples[0][i] == linesTriples[2][z]):
                    commonLetter = linesTriples[0][i]
                    if('A' <= commonLetter <= "Z"):
                        value = ord(commonLetter) - 38
                    else:
                        value = ord(commonLetter) - 96
                    return value

def part2(filePath):
    fileToRead = open(filePath,"r")
    cnt = 0
    sum = 0
    linesTriplet = []
    for line in fileToRead.readlines():
        newLine = line.replace("\n","")
        cnt += 1
        if(cnt < 3):
            linesTriplet.append(newLine)
        else:
            linesTriplet.append(newLine)
            sum += functionOccurence(linesTriplet)
            linesTriplet.clear()
            cnt = 0
    fileToRead.close()
    return sum

print("First Part:   ",part1("input.txt"))
print("Second Part:   ",part2("input.txt"))