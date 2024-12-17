from enum import Enum

class Direction(Enum):
    NORTH = (-1, 0)
    NORTH_EAST = (-1, 1)
    EAST = (0, 1)
    SOUTH_EAST = (1, 1)
    SOUTH = (1, 0)
    SOUTH_WEST = (1, -1)
    WEST = (0, -1)
    NORTH_WEST = (-1, -1)
    
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
    


def isInbounds(pos, rows, cols):
    row, col = pos
    return 0 <= row < rows and 0 <= col < cols