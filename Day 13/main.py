import json
from functools import cmp_to_key
#6369 e 25800

def function1(left,right):
    lenght = max(len(left),len(right))
    for i in range(lenght):
        if i >= len(left):
            return 1
        if i >= len(right):
            return -1

        l = left[i]
        r = right[i]
        ordered = 0

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                ordered = 1
            elif l > r:
                ordered = -1
            else: 
                ordered = 0
                continue
        elif isinstance(l, list) and isinstance(r, list):
            ordered = function1(l,r)
        else:
            if isinstance(l, int):
                l = [l]
            else:
                r = [r]
            ordered = function1(l,r)
        if ordered != 0:
            return ordered
    return 0

with open("input.txt") as fileToRead:
    total_packets = []
    packets = []
    index = 1
    result = 0
    for line in fileToRead.readlines():
        line = line.replace("\n","")
        if line == "":
            #call the function
            if function1(packets[0],packets[1]) == 1:
                result += index
            packets.clear()
            index += 1
        else:
            packet = json.loads(line)
            packets.append(packet)
            total_packets.append(packet)
    #call the function
    if function1(packets[0],packets[1]) == 1:
        result += index
    print(f"First Part:  {result}")
    two = [[2]]
    six = [[6]]
    total_packets.append(two)
    total_packets.append(six)
    sorted_packets = sorted(total_packets,key=cmp_to_key(function1),reverse=True)
    print(f"Second Part:  {(sorted_packets.index(two)+1) * (sorted_packets.index(six)+1)}")