def checkCycle(cycle,x):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
       return cycle*x
    return 0

def drawCRT(CRT,cycle,value,x):
    if cycle <= 40:
        pos = 0
    elif cycle > 40 and cycle <= 80:
        pos = 1
    elif cycle > 80 and cycle <= 120:
        pos = 2
    elif cycle > 120 and cycle <= 160:
        pos = 3
    elif cycle > 160 and cycle <= 200:
        pos = 4
    else:
        pos = 5
    value -= 1
    if value >= x-1 and value <= x+1:
        CRT[pos] += "#"
    else:
        CRT[pos] += "."
    print(f"Cycle: {cycle},Value: {value},X: {x},CRT: {CRT[pos]}")
    return CRT

with open("input.txt","r") as fileToRead:
    x = 1
    cycle = 1
    val = 1
    result = 0
    CRT = []
    for i in range(0,6):
        CRT.append("")

    for line in fileToRead.readlines():
        line = line.replace("\n","").split(" ")
        instruction = line[0]
        if len(line) > 1:
            value = line[1]
        if instruction == "noop":
            for i in range(0,1):
                CRT = drawCRT(CRT,cycle,val,x)
                if cycle % 40 == 0:
                    val = 0
                cycle += 1
                val += 1
                result += checkCycle(cycle,x)
        elif instruction == "addx":
            for i in range(0,2):
                CRT = drawCRT(CRT,cycle,val,x)
                if cycle % 40 == 0:
                    val = 0
                if i==1:
                    x += int(value)
                cycle += 1
                val += 1
                result += checkCycle(cycle,x)
    print(f"First Part:   {result}")
    print("Second Part:   ")
    for i in range(0,6):
        print(CRT[i])