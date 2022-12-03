def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sumOfPriority = 0
    for line in lines:
        front = line[:int(len(line)/2)]
        back = line[int(len(line)/2):]

        for chr in front:
            if chr in back:
                if chr.islower():
                    sumOfPriority += ord(chr) - 96
                else:
                    sumOfPriority += ord(chr) - 38
                break

    print(sumOfPriority)

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sumOfPriority = 0
    for firstElf in range(0,len(lines),3):
        for chr in lines[firstElf]:
            if chr in lines[firstElf+1] and chr in lines[firstElf+2]:
                if chr.islower():
                    sumOfPriority += ord(chr) - 96
                else:
                    sumOfPriority += ord(chr) - 38
                break
            
    print(sumOfPriority)

part1()
part2()