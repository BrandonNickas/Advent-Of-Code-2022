from math import floor

def setup():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    monkeys = [] #[[starting items], operation, test, true, false, inspections]
    
    for line in lines:
        if line == '':
            currentMonkey.append(0)
            monkeys.append(currentMonkey)
        elif line.split()[0] == 'Monkey':
            currentMonkey = []
        elif line.split()[0] == 'Starting':
            currentListOfItems = []
            test = line.split()
            for item in line.split()[2:]:
                if item[-1] == ',':
                    currentListOfItems.append(int(item[:-1]))
                else:
                    currentListOfItems.append(int(item))

            currentMonkey.append(currentListOfItems)
        
        elif line.split()[0] == 'Operation:':
            currentMonkey.append([line.split()[4], line.split()[5]])
        elif line.split()[0] == 'Test:':
            currentMonkey.append(int(line.split()[-1]))
        elif line.split()[0] == 'If':
            currentMonkey.append(int(line.split()[-1]))

    currentMonkey.append(0)
    monkeys.append(currentMonkey)

    return monkeys

def part1():
    monkeys = setup()

    #[[starting items], [operator, modifier], test, true, false, inspections]

    for round in range(20):
        for monkey in monkeys:
            while(len(monkey[0]) != 0):
                currentItem = monkey[0].pop(0)
                monkey[5] += 1
                if monkey[1][0] == '+':
                    if monkey[1][1] == 'old':
                        currentItem = currentItem + currentItem
                    else:
                        currentItem = currentItem + int(monkey[1][1])
                else:
                    if monkey[1][1] == 'old':
                        currentItem = currentItem * currentItem
                    else:
                        currentItem = currentItem * int(monkey[1][1])

                currentItem = floor(currentItem / 3)

                if currentItem % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(currentItem)
                else:
                    monkeys[monkey[4]][0].append(currentItem)
    
    inspectionValues = []
    for monkey in monkeys:
        inspectionValues.append(monkey[5])

    inspectionValues.sort()

    print(inspectionValues[-1] * inspectionValues[-2])

def part2():
    monkeys = setup()

    #[[starting items], [operator, modifier], test, true, false, inspections]

    for round in range(100):
        for monkey in monkeys:
            while(len(monkey[0]) != 0):
                currentItem = monkey[0].pop(0)
                monkey[5] += 1
                if monkey[1][0] == '+':
                    if monkey[1][1] == 'old':
                        currentItem = currentItem + currentItem
                    else:
                        currentItem = currentItem + int(monkey[1][1])
                else:
                    if monkey[1][1] == 'old':
                        currentItem = currentItem * currentItem
                    else:
                        currentItem = currentItem * int(monkey[1][1])

                if currentItem % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(currentItem)
                else:
                    monkeys[monkey[4]][0].append(currentItem)
    
    inspectionValues = []
    for monkey in monkeys:
        inspectionValues.append(monkey[5])

    inspectionValues.sort()

    print(inspectionValues[-1] * inspectionValues[-2])

part1()
part2()