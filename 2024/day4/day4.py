import re

def getColumns(text):
    lines = text.split('\n')
    
    rows = len(lines)
    columnsCount = len(lines[0])
    
    columns = ['' for _ in range(columnsCount)]
    
    for row in range(rows):
        for col in range(columnsCount):
            columns[col] = columns[col] + lines[row][col]
            
    return '\n'.join(columns)

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
            
    return '\n'.join(diagonals)
            

def findXMAS(inputFile):
    
    with open(inputFile, 'r') as file:
        data = file.read()
        
        pattern = r'(?=(XMAS|SAMX))'

        matchesHorisontal = re.finditer(pattern, data)
        countHorizontal = sum(1 for _ in matchesHorisontal)
        
        columns = getColumns(data)
        matchesVertical = re.finditer(pattern, columns)
        countVertical = sum(1 for _ in matchesVertical)

        diagonals = getDiagonals(data)
        matchesDiagonal = re.finditer(pattern, diagonals)
        countDiagonals = sum(1 for _ in matchesDiagonal)
        
        
    result = countHorizontal + countVertical + countDiagonals
        
    print(result)
    
findXMAS('day4-input.txt')