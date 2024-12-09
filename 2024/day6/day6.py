from enum import Enum

def isInsideMap(position, width, height):
    return position[0] >= 0 and position[0] < width and position[1] >= 0 and position[1] < height

class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)
    
    def move(self, position):
        x, y = position
        dx, dy = self.value
        return (x + dx, y + dy)
    
    def turnRight(self):
        directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        
        return directions[(directions.index(self) + 1) % len(directions)]

def mapGuardPath(guardMap):
    guardPosition = None
    for y in range(len(guardMap)):
        for x in range(len(guardMap[0])):
            if guardMap[y][x] == '^':
                guardPosition = (x, y)
                break
        if guardPosition:
            break
        
    startingGuardPosition = guardPosition
    
    visited = set()
    visited.add(guardPosition)
    direction = Direction.NORTH

    while (True):
        currentPos = direction.move(guardPosition)
        cX, cY = currentPos
        
        if not isInsideMap(currentPos, len(guardMap), len(guardMap[0])):
            break
        
        if guardMap[cY][cX] == '#':
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
        cX, cY = currentPos
        
        if not isInsideMap(currentPos, len(guardMap), len(guardMap[0])):
            return False
        
        if guardMap[cY][cX] == '#' or currentPos == placedObstacle:
            direction = direction.turnRight()
        elif (currentPos, direction) in visited:
            return True
        else:
            visited.add((currentPos, direction))
            guardPosition = currentPos

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
    
def guardPathLength(inputFile):
    with open(inputFile, 'r') as file:
        guardMap = file.read().split('\n')
        
    print('Part 1: ', len(mapGuardPath(guardMap)[0]))

guardPathLength('day6-input.txt')
possibleCyclesCount('day6-input.txt')