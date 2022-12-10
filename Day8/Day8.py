def setup():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    rowRanges = []
    for line in lines:
        currentRow = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
        for index, tree in enumerate(line):
            height = int(tree)

            if currentRow[height][0] == -1:
                currentRow[height][0] = index
            else:
                currentRow[height][1] = index

        rowRanges.append(currentRow)

    colRanges = []
    for col in range(len(lines[0])):
        currentCol = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
        for row in range(len(lines)):
            height = int(lines[row][col])

            if currentCol[height][0] == -1:
                currentCol[height][0] = row
            else:
                currentCol[height][1] = row

        colRanges.append(currentCol)

    return rowRanges, colRanges

def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    rowRanges, colRanges = setup()

    visableTrees = 0
    for rowIndex, line in enumerate(lines):
        for colIndex, tree in enumerate(line):
            foundLeft, foundRight, foundUp, foundDown = False, False, False, False
            for height in range(9,int(tree) - 1,-1):
                if rowRanges[rowIndex][height][0] != -1 and rowRanges[rowIndex][height][0] < colIndex:
                    foundLeft = True
                if (rowRanges[rowIndex][height][1] != -1 and rowRanges[rowIndex][height][1] > colIndex) or (rowRanges[rowIndex][height][1] == -1 and rowRanges[rowIndex][height][0] != -1 and rowRanges[rowIndex][height][0] > colIndex):
                    foundRight = True
                if colRanges[colIndex][height][0] != -1 and colRanges[colIndex][height][0] < rowIndex:
                    foundUp = True
                if (colRanges[colIndex][height][1] != -1 and colRanges[colIndex][height][1] > rowIndex) or (colRanges[colIndex][height][1] == -1 and colRanges[colIndex][height][0] != -1 and colRanges[colIndex][height][0] > rowIndex):
                    foundDown = True
        
            if not(foundLeft and foundRight and foundUp and foundDown):
                visableTrees += 1
    
    print(visableTrees)


def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    bestTreeScore = 0
    for rowIndex, line in enumerate(lines):
        for colIndex, tree in enumerate(line):
            scoreLeft, scoreRight, scoreUp, scoreDown  = colIndex, len(line) - colIndex - 1, rowIndex, len(lines) - rowIndex - 1
            height = int(tree)

            for i in range(colIndex - 1, -1, -1):
                if int(line[i]) >= height:
                    scoreLeft = colIndex - i
                    break
            
            for i in range(colIndex + 1, len(line)):
                if int(line[i]) >= height:
                    scoreRight = i - colIndex
                    break

            for i in range(rowIndex - 1, -1, -1):
                if int(lines[i][colIndex]) >= height:
                    scoreUp = rowIndex - i
                    break

            for i in range(rowIndex + 1, len(lines)):
                if int(lines[i][colIndex]) >= height:
                    scoreDown = i - rowIndex
                    break

            if bestTreeScore < scoreLeft * scoreRight * scoreDown  * scoreUp:
                bestTreeScore = scoreLeft * scoreRight * scoreDown * scoreUp

    print(bestTreeScore)

part1()
part2()