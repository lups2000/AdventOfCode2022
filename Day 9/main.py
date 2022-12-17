
def function1(fileToRead):
    head = [0, 0]
    tail = [0, 0]
    listPositions = [[0, 0]]
    for line in fileToRead.readlines():
        line = line.replace("\n", "").split(" ")
        direction, steps = line[0], int(line[1])
        for i in range(0, steps):
            if direction == "U":
                head[0] -= 1
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = [head[0] + 1, head[1]]
            elif direction == "D":
                head[0] += 1
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = [head[0] - 1, head[1]]
            elif direction == "L":
                head[1] -= 1
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = [head[0], head[1] + 1]
            else:
                head[1] += 1
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = [head[0], head[1] - 1]
            if tail not in listPositions:
                listPositions.append(tail)
    return len(listPositions)


def function2(fileToRead):
    head = [0, 0]
    positions = {
        "1": [0, 0],
        "2": [0, 0],
        "3": [0, 0],
        "4": [0, 0],
        "5": [0, 0],
        "6": [0, 0],
        "7": [0, 0],
        "8": [0, 0],
        "9": [0, 0],
    }
    listPositions = set(['[0, 0]'])

    for line in fileToRead.readlines():
        line = line.replace("\n", "").split(" ")
        direction, steps = line[0], int(line[1])
        for i in range(0, steps):
            if direction == "U":
                head[0] -= 1
            elif direction == "D":
                head[0] += 1
            elif direction == "L":
                head[1] -= 1
            else:
                head[1] += 1

            prev = head
            for k in positions.keys():
                x = positions[k][0]
                y = positions[k][1]
                if (x - prev[0]) * (x - prev[0]) + (y - prev[1]) * (y - prev[1]) > 2:
                    if abs(prev[0] - x) <= 1:
                        positions[k][0] = prev[0] 
                    else:
                        positions[k][0] = int((prev[0] + x) / 2)
                    if abs(prev[1] - y) <= 1:
                        positions[k][1] = prev[1]
                    else:
                        positions[k][1] = int((prev[1] + y) / 2)
                prev = positions[k]    
            listPositions.add(str(positions["9"]))

    return len(listPositions)


with open("input.txt") as fileToRead:
    print("First Part:   ", function1(fileToRead))
with open("input.txt") as fileToRead:
    print("Second Part:   ", function2(fileToRead))


