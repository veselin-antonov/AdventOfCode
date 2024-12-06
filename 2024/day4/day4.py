import re

# Day 4: Ceres Search

def getColumns(text):
    lines = text.split('\n')
    
    rows = len(lines)
    columnsCount = len(lines[0])
    
    columns = ['' for _ in range(columnsCount)]
    
    for row in range(rows):
        for col in range(columnsCount):
            columns[col] = columns[col] + lines[row][col]
            
    return columns

def getDiagonals(text):
    lines = text.split('\n')
    
    rows = len(lines)
    columns = len(lines[0])
    
    diagonals = ['' for _ in range((rows + columns) * 2)]
    
    for row in range(rows):
        for col in range(columns):
            diagonals[row + col] = diagonals[row + col] + lines[row][col]
        
    reverseStart = rows + columns - 1
            
    for row in range(rows):
        for col in range(columns - 1, -1, -1):
            diagonals[reverseStart + row + columns - col] = diagonals[reverseStart + row + columns - col] + lines[row][col]
            
    return diagonals

def turn90deg(lines):
    rows = len(lines)
    columns = len(lines[0])
    
    turned = ['' for _ in range(columns)]
    
    for col in range(columns):
        for row in range(rows - 1, -1, -1):
            turned[col] = turned[col] + lines[row][col]
            
    return turned
              
# Part 1
def findXMAS(inputFile):
    
    with open(inputFile, 'r') as file:
        data = file.read()
        
    pattern = r'(?=(XMAS|SAMX))'

    matchesHorisontal = re.finditer(pattern, data)
    countHorizontal = sum(1 for _ in matchesHorisontal)
    
    columns = getColumns(data).split('\n')
    matchesVertical = re.finditer(pattern, columns)
    countVertical = sum(1 for _ in matchesVertical)

    diagonals = getDiagonals(data).split('\n')
    matchesDiagonal = re.finditer(pattern, diagonals)
    countDiagonals = sum(1 for _ in matchesDiagonal)
        
        
    result = countHorizontal + countVertical + countDiagonals
        
    print(result)

# Part 2    
def doubleMAS(inputFile):
    
    with open(inputFile, 'r') as file:
        data = file.read()
        
    rows = data.split('\n');
    rows90deg = turn90deg(rows)
    rows180deg = turn90deg(rows90deg)
    rows270deg = turn90deg(rows180deg)
    
    pattern = 'MMASS'
    getCross = lambda data, row, col: data[row][col] + data[row][col + 2] + data[row + 1][col + 1] + data[row + 2][col] + data[row + 2][col + 2]
    hasDoubleMas = lambda data, row, col: getCross(data, row, col) == pattern

    result = 0;
    for i in range(0, len(rows) - 2):
        for j in range(0, len(rows[i]) - 2):
            if hasDoubleMas(rows, i, j):
                result += 1
            if hasDoubleMas(rows90deg, i, j):
                result += 1
            if hasDoubleMas(rows180deg, i, j):
                result += 1
            if hasDoubleMas(rows270deg, i, j):
                result += 1
                
    print(result)
    
print('Part 1: ', end='')
findXMAS('day3-input.txt')

print('Part 2: ', end='')
doubleMAS('day3-input.txt')