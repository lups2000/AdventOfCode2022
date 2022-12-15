
def function1(matrix,direction,steps) -> int:
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if "H" in matrix[i][j]:
                head_x = i
                head_y = j
            if "T" in matrix[i][j]:
                tail_x = i
                tail_y = j
    cnt = 0
    for z in range(0,steps):
        if direction == "U":
            matrix[head_x][head_y] = matrix[head_x][head_y].replace("H","")
            matrix[head_x - 1][head_y] += "H"
            if abs(head_x - tail_x) > 0 or abs(head_y - tail_y) > 0:
                matrix[tail_x][tail_y] = matrix[tail_x][tail_y].replace("T","")
                tail_x = head_x
                tail_y = head_y
                matrix[tail_x][tail_y] += "T"
                if "#" not in matrix[tail_x][tail_y]:
                    matrix[tail_x][tail_y] += "#"
                    cnt += 1
            head_x -= 1
        elif direction == "D":
            matrix[head_x][head_y] = matrix[head_x][head_y].replace("H","")
            matrix[head_x + 1][head_y] += "H"
            if abs(head_x - tail_x) > 0 or abs(head_y - tail_y) > 0:
                matrix[tail_x][tail_y] = matrix[tail_x][tail_y].replace("T","")
                tail_x = head_x
                tail_y = head_y
                matrix[tail_x][tail_y] += "T"
                if "#" not in matrix[tail_x][tail_y]:
                    matrix[tail_x][tail_y] += "#"
                    cnt += 1
            head_x += 1
        elif direction == "L":
            matrix[head_x][head_y] = matrix[head_x][head_y].replace("H","")
            matrix[head_x][head_y - 1] += "H"
            if abs(head_x - tail_x) > 0 or abs(head_y - tail_y) > 0:
                matrix[tail_x][tail_y] = matrix[tail_x][tail_y].replace("T","")
                tail_x = head_x
                tail_y = head_y
                matrix[tail_x][tail_y] += "T"
                if "#" not in matrix[tail_x][tail_y]:
                    matrix[tail_x][tail_y] += "#"
                    cnt += 1
            head_y -= 1
        else:
            matrix[head_x][head_y] = matrix[head_x][head_y].replace("H","")
            matrix[head_x][head_y + 1] += "H"
            if abs(head_x - tail_x) > 0 or abs(head_y - tail_y) > 0:
                matrix[tail_x][tail_y] = matrix[tail_x][tail_y].replace("T","")
                tail_x = head_x
                tail_y = head_y
                matrix[tail_x][tail_y] += "T"
                if "#" not in matrix[tail_x][tail_y]:
                    matrix[tail_x][tail_y] += "#"
                    cnt += 1
            head_y += 1
        print(matrix)
    return cnt

with open("input.txt") as fileToRead:
    matrix = [
        ["","","","","",""],
        ["","","","","",""],
        ["","","","","",""],
        ["","","","","",""],
        ["","","","","",""],
        ["sTH","","","","",""],
    ]
    cnt = 0
    for line in fileToRead.readlines():
        line = line.replace("\n","").split(" ")
        cnt += function1(matrix,line[0],int(line[1]))
    print(cnt)