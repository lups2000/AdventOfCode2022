
def crateFunction(crates,modality):
    if(modality ==  False):
        for i in range(0,int(line[1])):
            crates[int(line[5])].insert(0,crates[int(line[3])][0])
            crates[int(line[3])].pop(0)
    else:
        for i in range(0,int(line[1])):
            crates[int(line[5])].insert(0,crates[int(line[3])][int(line[1]) - i - 1])
            crates[int(line[3])].pop(int(line[1]) - i - 1)

with open("input.txt") as fileToRead:
    crates = {}
    modality = True #False for the part1, True for the second one
    for line in fileToRead.readlines():
        line = line.replace("\n","").split(" ")
        cnt = 1
        temp = 0
        if(line[0] != "move"):
            for el in line:
                if el != "" and "[" in el:
                    temp = 0
                    if cnt not in crates.keys():
                        crates[cnt] = [el]
                    else:
                        crates[cnt].append(el)
                    cnt += 1
                else:
                    temp += 1
                    if(temp == 4):
                        cnt += 1
                        temp = 0
            cnt = 1
        else:
            crateFunction(crates,modality)
    
    string = ""
    sorted_crates = dict(sorted(crates.items())) 
    for key in sorted_crates.keys():
        element = sorted_crates[key][0].strip("[]")
        string += element

    print("Result:  ",string)