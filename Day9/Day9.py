def moveTail(headCord, tailCord):
    #head is touching the tail diff beteen x and t is 0 or 1
    if abs(headCord[0] - tailCord[0]) < 2 and abs(headCord[1] - tailCord[1]) < 2:
        return tailCord

    #head is 2 away in only 1 direction
    elif (abs(headCord[0] - tailCord[0]) == 2 and abs(headCord[1] - tailCord[1]) == 0) or (abs(headCord[0] - tailCord[0]) == 0 and abs(headCord[1] - tailCord[1]) == 2):
        direction = 1
        if abs(headCord[0] - tailCord[0]) == 2:
            direction = 0

        if headCord[direction] - tailCord[direction] == 2:
            tailCord[direction] += 1
        else:
            tailCord[direction] -= 1

        return tailCord

    #head is 2 away in one direction and 1 away in another directions
    elif (abs(headCord[0] - tailCord[0]) == 2 and abs(headCord[1] - tailCord[1]) == 1) or (abs(headCord[0] - tailCord[0]) == 1 and abs(headCord[1] - tailCord[1]) == 2):
        twoDirection = 1
        oneDirection = 0
        if abs(headCord[0] - tailCord[0]) == 2:
            twoDirection = 0
            oneDirection = 1

        if headCord[twoDirection] - tailCord[twoDirection] == 2:
            tailCord[twoDirection] += 1
            if headCord[oneDirection] - tailCord[oneDirection] == 1:
                tailCord[oneDirection] += 1
            else:
                tailCord[oneDirection] -= 1
        else:
            tailCord[twoDirection] -= 1
            if headCord[oneDirection] - tailCord[oneDirection] == 1:
                tailCord[oneDirection] += 1
            else:
                tailCord[oneDirection] -= 1

        return tailCord

    #head is 2 away from the knot in two direction
    else:
        twoDirection = 1
        oneDirection = 0
        if abs(headCord[0] - tailCord[0]) == 2:
            twoDirection = 0
            oneDirection = 1
            
        if headCord[twoDirection] - tailCord[twoDirection] == 2:
            tailCord[twoDirection] += 1
            if headCord[oneDirection] - tailCord[oneDirection] == 2:
                tailCord[oneDirection] += 1
            else:
                tailCord[oneDirection] -= 1
        else:
            tailCord[twoDirection] -= 1
            if headCord[oneDirection] - tailCord[oneDirection] == 2:
                tailCord[oneDirection] += 1
            else:
                tailCord[oneDirection] -= 1 
        return tailCord

def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    currentHeadLocation = [0,0]
    currentTailLocation = [0,0]
    tailLocationsVisited = {'[0, 0]'}

    for line in lines:
        direction = line.split()[0]
        numberOfSteps = int(line.split()[1])
        for i in range(numberOfSteps):
            if direction == "L":
                currentHeadLocation[0] -=  1

            if direction == "R":
                currentHeadLocation[0] +=  1

            if direction == "D":
                currentHeadLocation[1] -=  1

            if direction == "U":
                currentHeadLocation[1] +=  1   
            
            currentTailLocation = moveTail(currentHeadLocation, currentTailLocation).copy()
            tailLocationsVisited.add(str(currentTailLocation))

    print(len(tailLocationsVisited))

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    currentHeadLocation = [0,0]
    currentKnotLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    tailLocationsVisited = {'[0, 0]'}

    for line in lines:
        direction = line.split()[0]
        numberOfSteps = int(line.split()[1])
        for i in range(numberOfSteps):
            if direction == "L":
                currentHeadLocation[0] -=  1

            if direction == "R":
                currentHeadLocation[0] +=  1

            if direction == "D":
                currentHeadLocation[1] -=  1

            if direction == "U":
                currentHeadLocation[1] +=  1   
            
            currentKnotLocations[0] = moveTail(currentHeadLocation, currentKnotLocations[0]).copy()

            for index, knotLocation in enumerate(currentKnotLocations):
                if index == 0:
                    currentKnotLocations[0] = moveTail(currentHeadLocation, currentKnotLocations[0]).copy()
                    continue

                currentKnotLocations[index] = moveTail(currentKnotLocations[index - 1], knotLocation).copy()
            
            tailLocationsVisited.add(str(currentKnotLocations[8]))

    print(len(tailLocationsVisited))

part1()
part2()