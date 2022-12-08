def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # entery in directories [0'nameOfDirectory',1'nameOfParent',2[contents, of, directory], 3totalStorage, 4booleanTotalFound]
    directories = []
    currentDirectory = ''
    contentsRead = False

    directoryInProgress = ['','','','','','']

    for line in lines:
        words = line.split()
        if len(words) == 3 and words[2] == '..':
            if contentsRead:
                directories.append(directoryInProgress)
            contentsRead = False
            
            for directory in directories:
                if directory[5] == directoryInProgress[5][:-len(directoryInProgress[0])]:
                    directoryInProgress = directory.copy()
                    currentDirectory = directoryInProgress[0]
                    break

        elif words[0] + words[1] == '$cd':
            if contentsRead:
                directories.append(directoryInProgress)
            contentsRead = False

            directoryInProgress = [words[2], currentDirectory, [], 0, False, directoryInProgress[5] + words[2]]
            currentDirectory = words[2]

        elif words[0] + words[1] == '$ls':
            contentsRead = True
            continue

        elif words[0] == 'dir':
            directoryInProgress[2].append(words[1])

        else:
            directoryInProgress[2].append(int(words[0]))

    directories.append(directoryInProgress)

    mathDone = False
    while not mathDone:
        for directory in directories:
            if directory[4]:
                continue
            if all(isinstance(item, int) for item in directory[2]):
                directory[3] = sum(directory[2])
                directory[4] = True
            else:
                sumOfDirectory = 0
                directory[3] = 0
                for item in directory[2]: 
                    if isinstance(item, int):
                        sumOfDirectory += item
                    else:
                        directory[4] = False
                        for solvedDirectory in directories:
                            if solvedDirectory[4] and solvedDirectory[5] == directory[5]+item: 
                                sumOfDirectory += solvedDirectory[3]
                                directory[4] = True
                                break
                            
                    directory[3] = sumOfDirectory

        for directory in directories:
            if not directory[4]:
                mathDone = False
                break
            mathDone = True

    totalDataToDelete = 0
    for directory in directories:
        if directory[3] <= 100000:
            totalDataToDelete += directory[3]   

    print(totalDataToDelete)          

def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # entery in directories [0'nameOfDirectory',1'nameOfParent',2[contents, of, directory], 3totalStorage, 4booleanTotalFound]
    directories = []
    currentDirectory = ''
    contentsRead = False

    directoryInProgress = ['','','','','','']

    for line in lines:
        words = line.split()
        if len(words) == 3 and words[2] == '..':
            if contentsRead:
                directories.append(directoryInProgress)
            contentsRead = False
            
            for directory in directories:
                if directory[5] == directoryInProgress[5][:-len(directoryInProgress[0])]:
                    directoryInProgress = directory.copy()
                    currentDirectory = directoryInProgress[0]
                    break

        elif words[0] + words[1] == '$cd':
            if contentsRead:
                directories.append(directoryInProgress)
            contentsRead = False

            directoryInProgress = [words[2], currentDirectory, [], 0, False, directoryInProgress[5] + words[2]]
            currentDirectory = words[2]

        elif words[0] + words[1] == '$ls':
            contentsRead = True
            continue

        elif words[0] == 'dir':
            directoryInProgress[2].append(words[1])

        else:
            directoryInProgress[2].append(int(words[0]))

    directories.append(directoryInProgress)

    mathDone = False
    while not mathDone:
        for directory in directories:
            if directory[4]:
                continue
            if all(isinstance(item, int) for item in directory[2]):
                directory[3] = sum(directory[2])
                directory[4] = True
            else:
                sumOfDirectory = 0
                directory[3] = 0
                for item in directory[2]: 
                    if isinstance(item, int):
                        sumOfDirectory += item
                    else:
                        directory[4] = False
                        for solvedDirectory in directories:
                            if solvedDirectory[4] and solvedDirectory[5] == directory[5]+item: 
                                sumOfDirectory += solvedDirectory[3]
                                directory[4] = True
                                break
                           
                    directory[3] = sumOfDirectory

                for part in directory[2]:
                    for doubleCheck in directories:
                        if doubleCheck[5] == directory[5]+str(part) and not doubleCheck[4]:
                            directory[4] = False

        for directory in directories:
            if not directory[4]:
                mathDone = False
                break
            mathDone = True

    bestDirectorySize = 99999999999
    spaceRemaining = 70000000 - directories[0][3]
    for directory in directories:
        if directory[3] + spaceRemaining >= 30000000 and bestDirectorySize > directory[3]:
              bestDirectorySize = directory[3]

    print(bestDirectorySize) 

part1()
part2()