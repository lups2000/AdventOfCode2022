#28691
maxX = 1000
maxY = 1000

def drawRocks(fromX,toX,fromY,toY,mappa,modality):
    if modality:
        for i in range(0,maxX):
            mappa[i][174] = 1
    if fromX == toX:
        for i in range(fromY,toY + 1):
            mappa[fromX - 400][i] = 1
    else:
        for i in range(fromX,toX + 1):
            mappa[i - 400][fromY] = 1

def drawMap(mappa):
    for i in range(0,maxX):
        for j in range(0, maxY):
            if mappa[j][i] == 0:
                print(".",end="")
            elif mappa[j][i] == -1:
                print("+",end="")
            elif mappa[j][i] == -2:
                print("o",end="")
            else:
                print("#",end="")
        print()

def function1(fileToRead):
    mappa = [[0 for x in range(maxX)] for y in range(maxY)] 
    mappa[100][0] = -1
    for line in fileToRead.readlines():
        scan = line.replace("\n","").replace(" ","").split("->")
        for i in range(0,len(scan) - 1):
            fromX = min(int(scan[i].split(",")[0]),int(scan[i+1].split(",")[0]))
            toX = max(int(scan[i+1].split(",")[0]),int(scan[i].split(",")[0]))
            fromY = min(int(scan[i].split(",")[1]),int(scan[i+1].split(",")[1]))
            toY = max(int(scan[i+1].split(",")[1]),int(scan[i].split(",")[1]))
            drawRocks(fromX,toX,fromY,toY,mappa,False)
    cnt = 0
    while(True):
        sorgX = 100
        sorgY = 0
        rest = False
        while(not rest and sorgY >= 0 and sorgY < 172 and sorgX >= 0 and sorgX < 173):
            if mappa[sorgX][sorgY + 1] == 0:
                sorgY += 1
            elif mappa[sorgX - 1][sorgY + 1] == 0:
                sorgX -= 1
                sorgY += 1
            elif mappa[sorgX + 1][sorgY + 1] == 0:
                sorgX += 1
                sorgY += 1
            else:
                rest = True
        if sorgY >= 0 and sorgY < 172 and sorgX >= 0 and sorgX < 173 :
            cnt += 1
            mappa[sorgX][sorgY] = -2
        else:
            break
    print(f"First Part:   {cnt}")

def function2(fileToRead):
    mappa = [[0 for x in range(maxX)] for y in range(maxY)] 
    mappa[100][0] = -1
    for line in fileToRead.readlines():
        scan = line.replace("\n","").replace(" ","").split("->")
        for i in range(0,len(scan) - 1):
            fromX = min(int(scan[i].split(",")[0]),int(scan[i+1].split(",")[0]))
            toX = max(int(scan[i+1].split(",")[0]),int(scan[i].split(",")[0]))
            fromY = min(int(scan[i].split(",")[1]),int(scan[i+1].split(",")[1]))
            toY = max(int(scan[i+1].split(",")[1]),int(scan[i].split(",")[1]))
            drawRocks(fromX,toX,fromY,toY,mappa,True)
    #drawMap(mappa)
    cnt = 0
    while(True):
        sorgX = 100
        sorgY = 0
        rest = False
        temp = 0
        while(not rest):
            if mappa[sorgX][sorgY + 1] == 0:
                sorgY += 1
                temp += 1
            elif mappa[sorgX - 1][sorgY + 1] == 0:
                sorgX -= 1
                sorgY += 1
                temp += 1
            elif mappa[sorgX + 1][sorgY + 1] == 0:
                sorgX += 1
                sorgY += 1
                temp += 1
            else:
                rest = True
        cnt += 1
        mappa[sorgX][sorgY] = -2
        if temp == 0:
            break
    drawMap(mappa)
    print(f"Second Part:   {cnt}")


with open("input.txt") as fileToRead:
    function1(fileToRead)

with open("input.txt") as fileToRead:
    function2(fileToRead)   
