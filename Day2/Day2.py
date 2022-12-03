def part1():
    scores = {'A':{'X':4,'Y':8,'Z':3},'B':{'X':1,'Y':5,'Z':9},'C':{'X':7,'Y':2,'Z':6}}

    with open('input.txt') as f:
        lines = f.read().splitlines()

    totalScore = 0
    for line in lines:  
        totalScore += scores[line[0]][line[2]]
    
    print(totalScore)

def part2():
    scores = {'A':{'X':3,'Y':4,'Z':8},'B':{'X':1,'Y':5,'Z':9},'C':{'X':2,'Y':6,'Z':7}}

    with open('input.txt') as f:
        lines = f.read().splitlines()

    totalScore = 0
    for line in lines:  
        totalScore += scores[line[0]][line[2]]
    
    print(totalScore)

part1()
part2()
