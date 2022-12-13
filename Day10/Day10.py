def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    cycle = 0
    xValue = 1
    totalSignalStrength = 0
    for line in lines:
        if len(line.split()) == 1:
            operationCycles = 1
        else:
            operationCycles = 2

        for i in range(operationCycles):
            cycle += 1
            if cycle % 40 == 20:
                totalSignalStrength += (cycle * xValue)
        
        if len(line.split()) == 2:
            xValue += (int(line.split()[1])) 
                
    print(totalSignalStrength)

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    cycle = 0
    xValue = 1
    spriteMiddlePixle = 1
    currentRow = ''
    for line in lines:
        if len(line.split()) == 1:
            operationCycles = 1
        else:
            operationCycles = 2

        for i in range(operationCycles):
            if cycle % 40 == spriteMiddlePixle or cycle % 40 == spriteMiddlePixle - 1 or cycle % 40 == spriteMiddlePixle + 1:
                currentRow += '█'
            else:
                currentRow += ' '

            cycle += 1

            if cycle != 0 and cycle % 40 == 0:
                print(currentRow, cycle)
                currentRow = ''
            
        if len(line.split()) == 2:
            spriteMiddlePixle += (int(line.split()[1])) 

    while cycle != 241:
        currentRow += ' '

    print(currentRow, cycle)

part1()
part2()