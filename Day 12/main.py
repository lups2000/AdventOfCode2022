from collections import deque

def BFS(source):
    queue = deque()
    queue.append(source)
    visited = set()
    while len(queue) > 0:
        source = queue.popleft()
        if (source[0],source[1]) in visited:
            continue

        visited.add((source[0],source[1]))

        if matrix[source[0]][source[1]] == 26:
            return source[2]

        #moving up
        if isValid(source[0] - 1, source[1], source ,matrix):
            queue.append([source[0] - 1, source[1], source[2] + 1])
        #moving down
        if isValid(source[0] + 1, source[1], source ,matrix):
            queue.append([source[0] + 1, source[1], source[2] + 1])
        #moving left
        if isValid(source[0], source[1] - 1, source ,matrix):
            queue.append([source[0], source[1] - 1, source[2] + 1])
        #moving right
        if isValid(source[0], source[1] + 1, source ,matrix):
            queue.append([source[0], source[1] + 1, source[2] + 1])
    return -1
    
def isValid(x,y,source,matrix):
    if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]) and matrix[x][y] <= matrix[source[0]][source[1]] + 1:
        return True
    return False

with open("input.txt","r") as fileToRead:
    matrix = []
    row = 0
    column = 0
    source = [0, 0, 0]
    lowerPositions = []
    for line in fileToRead.readlines():
        line = line.replace("\n","")
        list = []
        column = 0
        for letter in line:
            if letter == "S":
                source = [row,column, 0]
                letter = 0
            elif letter == "E":
                letter = 26
            else:
                letter = ord(letter) - 97
                if letter == 0:
                    lowerPositions.append([row,column,0])
            list.append(letter)
            column += 1
        matrix.append(list)
        row += 1
    lowerPositions.append(source)
    print("First Part:   ",BFS(lowerPositions[len(lowerPositions) - 1]))
    posValues = [BFS(lowerPositions[len(lowerPositions) - 1])]
    for i in range(0,len(lowerPositions) - 1):
        value = BFS(lowerPositions[i])
        if value != -1 :
            posValues.append(value)
    print("Second Part:   ",min(posValues))