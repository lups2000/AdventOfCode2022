sumCalories = 0
calories = []
fileToRead = open("input.txt")

for line in fileToRead.readlines():
    if line != "\n":
        sumCalories += int(line.replace("\n",""))
    else:
        calories.append(sumCalories)
        sumCalories = 0

calories.append(sumCalories)    
calories.sort(reverse=True)
print(f"First Part: {calories[0]}")
print(f"Second Part: {calories[0] + calories[1] + calories[2]}")
fileToRead.close()