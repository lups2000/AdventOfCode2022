fileToRead = open("input.txt","r")

cnt1 = 0
cnt2 = 0
for line in fileToRead.readlines():
    couple = line.replace("\n","").split(",")
    firstInterval = couple[0].split("-")
    secondInterval = couple[1].split("-")
    if (int(firstInterval[0]) <= int(secondInterval[0]) and int(firstInterval[1]) >= int(secondInterval[1])) or (int(secondInterval[0]) <= int(firstInterval[0]) and int(secondInterval[1]) >= int(firstInterval[1])):
        cnt1 += 1
    if (int(firstInterval[0]) <= int(secondInterval[0]) <= int(firstInterval[1]) or (int(secondInterval[0]) <= int(firstInterval[0]) <= int(secondInterval[1]))):
        cnt2 += 1

print(f"First Part:  {cnt1}")
print(f"First Part:  {cnt2}")
fileToRead.close()