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

def exploreRegion(symbol, pos, direction, garden, visited, edges):
    if not isInsideMap(pos, len(garden), len(garden[0])) or symbol != garden[pos[0]][pos[1]]:
        edges.append(pos)
        return
    elif pos in visited:
        return
    else:    
        visited.add(pos)
        exploreRegion(symbol, direction.move(pos), direction, garden, visited, edges)
        exploreRegion(symbol, direction.turnLeft().move(pos), direction.turnLeft(), garden, visited, edges)
        exploreRegion(symbol, direction.turnRight().move(pos), direction.turnRight(), garden, visited, edges)
    

with open('day12-input.txt', 'r') as file:
    garden = file.read().split('\n')
    
    result = 0
    regions = []
    for row in range(len(garden)):
        for col in range(len(garden[0])):
            if all(not (row, col) in region[0] for region in regions):
                region = set()
                edges = [(row - 1, col)]
                exploreRegion(garden[row][col], (row, col), Direction.EAST, garden, region, edges)
                regions.append((region, edges))
                print(len(region), end = " ")
                print(len(edges) + 1)
                
print(sum([len(region[0]) * len(region[1]) for region in regions]))