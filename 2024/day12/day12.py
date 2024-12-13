from enum import Enum

class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)
    
    def move(self, position):
        row, col = position
        dRow, dCol = self.value
        return (row + dRow, col + dCol)
    
    def turnRight(self):
        directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        
        return directions[(directions.index(self) + 1) % len(directions)]
    
    def turnLeft(self):
        directions = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
        
        return directions[(directions.index(self) + 1) % len(directions)]

def isInsideMap(pos, rows, cols):
    row, col = pos
    return not (row < 0 or row >= rows or col < 0 or col >= cols)

def exploreRegion(symbol, pos, direction, garden):
    if not isInsideMap(pos, len(garden), len(garden[0])) or symbol != garden[pos[0]][pos[1]]:
        return []
    
    newPos = direction.move(pos)
    return [pos] + exploreRegion(symbol, newPos, direction, garden) + exploreRegion(symbol, newPos, direction.turnLeft(), garden) + exploreRegion(symbol, newPos, direction.turnRight(), garden)
    

with open('day12-input.txt', 'r') as file:
    garden = file.read()
    
    print(exploreRegion('C', (0, 0), Direction.EAST, garden))