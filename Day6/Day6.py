def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    window = []
    for index, chr in enumerate(lines[0]):
        window.insert(0,chr)
        if len(window) == 5:
            window.pop()
        
            sortedWindow = window.copy()
            sortedWindow.sort()
            uniqueCharacter = True
            for i in range(len(sortedWindow) - 1):
                if sortedWindow[i] == sortedWindow[i+1]:
                    uniqueCharacter = False
                    break

            if uniqueCharacter:
                print(index + 1)
                break

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    window = []
    for index, chr in enumerate(lines[0]):
        window.insert(0,chr)
        if len(window) == 15:
            window.pop()
        
            sortedWindow = window.copy()
            sortedWindow.sort()
            uniqueCharacter = True
            for i in range(len(sortedWindow) - 1):
                if sortedWindow[i] == sortedWindow[i+1]:
                    uniqueCharacter = False
                    break

            if uniqueCharacter:
                print(index + 1)
                break

part1()
part2()