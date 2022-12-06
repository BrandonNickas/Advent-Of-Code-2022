def setup():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    bottomOfStartState = 0
    for index, line in enumerate(lines):
        if line.split()[0] == '1':
            bottomOfStartState = index
            lastStackNumber = int(line.split()[-1])
            break

    stacks = []
    for i in range(lastStackNumber):
        stacks.append([])

    for level in range(bottomOfStartState - 1,-1,-1):
        for index, boxes in enumerate(lines[level].split()):
            if boxes[1] != '1':
                stacks[index].append(boxes[1])

    return stacks, bottomOfStartState

def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    stacks, beginingOfInstructions= setup()

    for line in range(beginingOfInstructions + 2, len(lines)):
        instruciton = lines[line].split()

        for i in range(int(instruciton[1])):
            if stacks[int(instruciton[3]) - 1] != []:
                stacks[int(instruciton[5]) - 1].append(stacks[int(instruciton[3]) - 1].pop())

    solution = ''
    for stack in stacks:
        if stack != []:
            solution += stack.pop()

    print(solution)

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    stacks, beginingOfInstructions= setup()

    for line in range(beginingOfInstructions + 2, len(lines)):
        instruciton = lines[line].split()

        inMotion = []
        for i in range(int(instruciton[1])):
            if stacks[int(instruciton[3]) - 1] != []:
                inMotion.insert(0,stacks[int(instruciton[3]) - 1].pop())
        
        stacks[int(instruciton[5]) - 1].extend(inMotion)


    solution = ''
    for stack in stacks:
        if stack != []:
            solution += stack.pop()

    print(solution)

part1()
part2()