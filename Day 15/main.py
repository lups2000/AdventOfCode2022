import math
from fractions import Fraction
minX = -2#-532461
maxX = 25#3999024
mapLine = 10#2000000

with open("input.txt","r") as FileToRead:
    positions = []
    sensors = []
    beacons = []
    manDistances = []
    for line in FileToRead.readlines():
        line = line.replace("\n","").split(": ")
        sensorCoords = line[0].replace("Sensor at ","").replace("x=","").replace("y=","").split(", ")
        beaconCoords = line[1].replace("closest beacon is at ","").replace("x=","").replace("y=","").split(", ")
        for i in range(0,len(sensorCoords)):
            sensorCoords[i] = int(sensorCoords[i])
            beaconCoords[i] = int(beaconCoords[i])
        manhattanDistance = abs(sensorCoords[0] - beaconCoords[0]) + abs(sensorCoords[1] - beaconCoords[1])
        sensors.append(sensorCoords)
        beacons.append(beaconCoords)
        manDistances.append(manhattanDistance)
    
    cnt = 0
    j = 0
    k = 0
    for j in range(minX - manDistances[k], maxX + manDistances[k]):
        for i in range(0,len(sensors)):
            if j == beacons[i][0] and beacons[i][1] == mapLine:
                continue
            if abs(j - sensors[i][0]) + abs(mapLine - sensors[i][1]) <= manDistances[i]:
                cnt += 1
                break
        k += 1
    print(f"First Part:   {cnt}")


    """
    correct but too inefficient!!!
    found = False
    for i in range(0,4000000):
        for j in range(0,4000000):
            found = False
            for k in range(0,len(sensors)):
                if abs(i - sensors[k][0]) + abs(j - sensors[k][1]) <= manDistances[k]:
                    found = True
                    break
            if not found:
                print(f"Second Part:   {Fraction(i) * Fraction(4000000) + j}")
                exit(0)"""