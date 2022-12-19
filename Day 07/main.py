
with open("input.txt","r") as fileToRead:
    dict = {}
    current_dict = ""
    for line in fileToRead:
        line = line.replace("\n","")
        if line.startswith("$"):
            if "cd" in line:
                line = line.split(" ")
                if line[2] not in dict.keys():
                    dict[line[2]] = {}
                    current_dict = line[2]
        else:
            if line.startswith("dir"):
                line = line.split(" ")
                dict[current_dict]