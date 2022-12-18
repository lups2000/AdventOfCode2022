def parseInput(fileToRead):
    monkeys = {}
    currentKey = 0
    for line in fileToRead.readlines():
        line = line.replace("\n","").replace(":","").replace(",","").strip(" ").split(" ")
        if line[0] == "Monkey":
            currentKey = line[1]
            if currentKey not in monkeys.keys():
                monkeys[currentKey] = {}
        elif line[0] == "Starting":
            monkeys[currentKey]["items"] = []
            for el in line[2:]:
                monkeys[currentKey]["items"].append(int(el))
        elif line[0] == "Operation":
            monkeys[currentKey]["operation"] = ""
            for el in line[4:]:
                monkeys[currentKey]["operation"] += el
        elif line[0] == "Test":
            monkeys[currentKey]["test"] = line[3]
        elif line[0] == "If" and line[1] == "true":
            monkeys[currentKey]["true"] = line[5]
        elif line[0] == "If" and line[1] == "false":
            monkeys[currentKey]["false"] = line[5]
        else:
            monkeys[currentKey]["inspections"] = 0
    monkeys[currentKey]["inspections"] = 0

    return monkeys

def performOperation(worryLevel,operationString) -> int:
    if operationString[1:] == "old":
        if operationString[0] == "+":
            return worryLevel + worryLevel
        elif operationString[0] == "-":
            return worryLevel - worryLevel
        elif operationString[0] == "*":
            return worryLevel * worryLevel
        else:
            return worryLevel / worryLevel
    else:
        if operationString[0] == "+":
            return worryLevel + int(operationString[1:])
        elif operationString[0] == "-":
            return worryLevel - int(operationString[1:])
        elif operationString[0] == "*":
            return worryLevel * int(operationString[1:])
        else:
            return worryLevel / int(operationString[1:])

def function1(fileToRead):
    monkeys = parseInput(fileToRead)
    for i in range(0,20):
        for key in monkeys.keys():
            monkey = monkeys[key]
            for item in monkey["items"]:
                worryLevel = performOperation(item,monkey["operation"])
                worryLevel = int(worryLevel/3)
                if worryLevel % int(monkey["test"]) == 0:
                    nextMonkey = monkey["true"]
                else:
                    nextMonkey = monkey["false"]
                monkeys[nextMonkey]["items"].append(worryLevel)
                monkey["inspections"] += 1
            monkey["items"].clear()
    result = []
    for key in monkeys.keys():
        monkey = monkeys[key]
        result.append(monkey["inspections"])
    result.sort(reverse=True)
    return result[0] * result[1]

def function2(fileToRead):
    monkeys = parseInput(fileToRead)
    divisor = 1
    for key in monkeys.keys():
        divisor *= int(monkeys[key]["test"])

    for i in range(0,10000):
        for key in monkeys.keys():
            monkey = monkeys[key]
            for item in monkey["items"]:
                worryLevel = performOperation(item,monkey["operation"])
                worryLevel = worryLevel % divisor
                if worryLevel % int(monkey["test"]) == 0:
                    nextMonkey = monkey["true"]
                else:
                    nextMonkey = monkey["false"]
                monkeys[nextMonkey]["items"].append(worryLevel)
                monkey["inspections"] += 1
            monkey["items"].clear()
    result = []
    for key in monkeys.keys():
        monkey = monkeys[key]
        result.append(monkey["inspections"])
    result.sort(reverse=True)
    return result[0] * result[1]

with open("input.txt") as fileToRead:
    print("First Part:    ",function1(fileToRead))
with open("input.txt") as fileToRead:
    print("Second Part:    ",function2(fileToRead))