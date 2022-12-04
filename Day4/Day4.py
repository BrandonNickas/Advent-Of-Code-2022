def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    completeOverlap = 0
    for line in lines:
        range1 = line.split(',')[0].split('-')
        range2 = line.split(',')[1].split('-')
        if (int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1])) or (int(range2[0]) >= int(range1[0]) and int(range2[1]) <= int(range1[1])):
            completeOverlap += 1

    print(completeOverlap)

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    completeOverlap = 0
    for line in lines:
        range1 = [int(number) for number in line.split(',')[0].split('-')]
        range2 = [int(number) for number in line.split(',')[1].split('-')]
        if range1[0]<= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1] or range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]:
            completeOverlap += 1

    print(completeOverlap)

part1()
part2()