def part1(): 
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    currntCal = 0
    max = 0
    for line in lines:
            if line == "":
                if currntCal > max:
                    max = currntCal
                currntCal = 0
            else:
                currntCal += int(line)
    print(max)
                

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    currntCal = 0
    values = []
    for line in lines:
            if line == "":
                values.append(currntCal)
                currntCal = 0
            else:
                currntCal += int(line)
    values.sort(reverse=True)

    print(sum(values[0:3]))

part1()
part2()

