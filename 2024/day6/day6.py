# Day 6: Guard Gallivant

from utils import Direction, isInbounds

def mapGuardPath(guardMap):
    guardPosition = None
    for row in range(len(guardMap)):
        for col in range(len(guardMap[0])):
            if guardMap[row][col] == '^':
                guardPosition = (row, col)
                break
        if guardPosition:
            break
        
    startingGuardPosition = guardPosition
    
    visited = set()
    visited.add(guardPosition)
    direction = Direction.NORTH

    while (True):
        currentPos = direction.move(guardPosition)
        row, col = currentPos
        
        if not isInbounds(currentPos, len(guardMap), len(guardMap[0])):
            break
        
        if guardMap[row][col] == '#':
            direction = direction.turnRight()
        else:
            visited.add(currentPos)
            guardPosition = currentPos
            
    return (visited, startingGuardPosition)
    
def hasCycles(guardMap, startingPosition, placedObstacle):
        
    direction = Direction.NORTH
    guardPosition = startingPosition
    visited = set()
    visited.add((guardPosition, direction))
        
    while (True):
        currentPos = direction.move(guardPosition)
        row, col = currentPos
        
        if not isInbounds(currentPos, len(guardMap), len(guardMap[0])):
            return False
        
        if guardMap[row][col] == '#' or currentPos == placedObstacle:
            direction = direction.turnRight()
        elif (currentPos, direction) in visited:
            return True
        else:
            visited.add((currentPos, direction))
            guardPosition = currentPos

def guardPathLength(inputFile):
    with open(inputFile, 'r') as file:
        guardMap = file.read().split('\n')
        
    print('Part 1: ', len(mapGuardPath(guardMap)[0]))

def possibleCyclesCount(inputFile):
    with open(inputFile, 'r') as file:
        guardMap = file.read().split('\n')
        
    guardPosition = mapGuardPath(guardMap)[1]
    visited = mapGuardPath(guardMap)[0]
        
    cyclesCount = 0;
    for pos in visited:
        if hasCycles(guardMap, guardPosition, pos):
            cyclesCount += 1
    
    print('Part 2: ', cyclesCount)

guardPathLength('day6-input.txt')
possibleCyclesCount('day6-input.txt')