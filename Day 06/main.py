
with open("input.txt") as fileToRead:
    content = fileToRead.read()
    four_letters_dict = {}
    modality = False 
    for i in range(0,len(content)):
        if content[i] not in four_letters_dict.keys():
            four_letters_dict[content[i]] = i
            if not modality and len(four_letters_dict) == 4:
                print("First Part:   ",i + 1)
                modality = True
            elif modality and len(four_letters_dict) == 14:
                print("Second Part:   ",i + 1)
                break
        else:
            for k in list(four_letters_dict.keys()):
                if four_letters_dict[k] < four_letters_dict[content[i]]:
                    del four_letters_dict[k]
            four_letters_dict[content[i]] = i
