def function1(matrix,row,column,direction) -> bool:
    if direction == "N":
        i = row
        while(i > 0):
            if matrix[row][column] <= matrix[i - 1][column]:
                return False
            i -= 1
    elif direction == "S":
        i = row
        while(i < len(matrix) - 1):
            if matrix[row][column] <= matrix[i + 1][column]:
                return False
            i += 1
    elif direction == "E":
        j = column
        while(j > 0):
            if matrix[row][column] <= matrix[row][j - 1]:
                return False
            j -= 1
    else:
        j = column
        while(j < len(matrix[0]) - 1):
            if matrix[row][column] <= matrix[row][j + 1]:
                return False
            j += 1
    return True

def function2(matrix,row,column,direction) -> int:
    cnt = 0
    if direction == "N":
        i = row
        while(i > 0):
            if matrix[row][column] > matrix[i - 1][column]:
                cnt += 1
            else:
                cnt += 1
                break
            i -= 1
    elif direction == "S":
        i = row
        while(i < len(matrix) - 1):
            if matrix[row][column] > matrix[i + 1][column]:
                cnt += 1
            else:
                cnt += 1
                break
            i += 1
    elif direction == "E":
        j = column
        while(j > 0):
            if matrix[row][column] > matrix[row][j - 1]:
                cnt += 1
            else:
                cnt += 1
                break
            j -= 1
    else:
        j = column
        while(j < len(matrix[0]) - 1):
            if matrix[row][column] > matrix[row][j + 1]:
                cnt += 1
            else:
                cnt += 1
                break
            j += 1
    return cnt

with open("input.txt") as fileToRead:
    matrix = []
    modality = False # false for the first part, true for the second one
    for line in fileToRead:
        list = []
        for num in line.replace("\n",""):
            list.append(num)
        matrix.append(list)
    cnt = 0
    maxProduct = 1
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[0])):
            if row == 0 or column == 0 or row == len(matrix)-1 or column == len(matrix[0])-1:
                cnt += 1
            else:
                directions = ["N","S","E","O"]
                product = 1
                if not modality:
                    for d in directions:
                        if function1(matrix,row,column,d) == True:
                            cnt += 1
                            break
                else:
                    for d in directions:
                        if function2(matrix,row,column,d) != 0:
                            product *= function2(matrix,row,column,d)
                    if product > maxProduct:
                        maxProduct = product

    if modality:
        print(f"Second part:   {maxProduct}")
    else:
        print(f"First part:   {cnt}")
