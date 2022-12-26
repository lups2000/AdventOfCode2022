from itertools import accumulate

def function1(dirs):
    res = 0
    for k,v in dirs.items():
        if v <= 100000:
            res += v
    return res

def function2(dirs):
    totalSpace = 70000000
    unusedSpaceRequired = 30000000

    unusedSpace = totalSpace - dirs["//"]
    list = []
    for k,v in dirs.items():
        if unusedSpace + v >= unusedSpaceRequired:
            if len(list) == 0:
                list.append(v)
            else:
                if v < list[0]:
                    list[0] = v
    return list[0]


with open("input.txt","r") as fileToRead:
    dirs = {"//" : 0}
    current_dir = []

    for line in fileToRead:
        line = line.replace("\n","")
        if line.startswith("$"):
            if "cd" in line:
                line = line.split(" ")
                if line[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(line[2] + "/")
        else:
            if line.startswith("dir"):
                line = line.split(" ")
                dirs["".join(current_dir) + line[1] + "/"] = 0
            else:
                line = line.split(" ")
                for i in accumulate(current_dir):
                    dirs[i] += int(line[0])

    #print(dirs)
    print(f"First Part:   {function1(dirs)}")
    print(f"Second Part:   {function2(dirs)}")