
def part1(fileContent):
    couplesWin = [['A','Y'],['B','Z'],['C','X']]
    couplesLose = [['B','X'],['A','Z'],['C','Y']]
    couplesDraw = [['A','X'],['B','Y'],['C','Z']]
    sum = 0
    for line in fileContent.readlines():
        newLine = line.replace("\n","").split(" ")
        if newLine in couplesWin:
            sum += 6
        elif newLine in couplesDraw:
            sum += 3
        if newLine[1] == "X":
            sum += 1
        elif newLine[1] == "Y":
            sum += 2
        elif newLine[1] == "Z":
            sum += 3
    print(sum)

def part2(fileContent):
    sum = 0
    for line in fileContent.readlines():
        newLine = line.replace("\n","").split(" ")
        if newLine[1] == "Z": # win
            sum += 6
            if newLine[0] == "A":
                sum += 2
            elif newLine[0] == "B":
                sum += 3
            else:
                sum += 1
        elif newLine[1] == "Y": #draw
            sum += 3
            if newLine[0] == "A":
                sum += 1
            elif newLine[0] == "B":
                sum += 2
            else:
                sum += 3
        else: #lose
            if newLine[0] == "A":
                sum += 3
            elif newLine[0] == "B":
                sum += 1
            else:
                sum += 2    
    print(sum)


fileContent = open("input.txt","r")
#part1(fileContent)
part2(fileContent)

