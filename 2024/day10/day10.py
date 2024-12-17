# Day 10: Hoof It

from utils import Direction, isInbounds
    
def findPeaksHelper(pos, direction: Direction, grid):
    newPos = direction.move(pos)
    nRow, nCol = newPos
    row, col = pos
    
    if (not isInbounds(newPos, len(grid[0]), len(grid))
        or grid[nRow][nCol] != grid[row][col] + 1):
        return []
    elif grid[nRow][nCol] == 9:
        return [newPos]
    else:
        return (
            findPeaksHelper(newPos, direction, grid)
            + findPeaksHelper(newPos, direction.turnRight(), grid)
            + findPeaksHelper(newPos, direction.turnLeft(), grid)
        )
        
def findPeaks(pos, grid):
    peaks = {
        peak
        for direction in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        for peak in (findPeaksHelper(pos, direction, grid) or [])
        if peak is not None
    }
    
    return peaks

def findPathsHelper(pos, direction: Direction, grid):
    newPos = direction.move(pos)
    nRow, nCol = newPos
    row, col = pos
    
    if (not isInbounds(newPos, len(grid[0]), len(grid))
        or grid[nRow][nCol] != grid[row][col] + 1):
        return 0
    elif grid[nRow][nCol] == 9:
        return 1
    else:
        return (
            findPathsHelper(newPos, direction, grid)
            + findPathsHelper(newPos, direction.turnRight(), grid)
            + findPathsHelper(newPos, direction.turnLeft(), grid)
        )

def findPaths(pos, grid):
    totalPaths = sum([
        findPathsHelper(pos, direction, grid)
        for direction in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    ])
    
    return totalPaths


with open('day10-input.txt', 'r') as file:
    grid = [[int(char) if char != '.' else -1 for char in line] for line in file.read().strip().split('\n')]

statsPerTrailheads = [
    (findPeaks((row, col), grid), findPaths((row, col), grid))
    for row in range(len(grid))
    for col in range(len(grid[0]))
    if grid[row][col] == 0
]

totalPeaks = sum([len(stats[0]) for stats in statsPerTrailheads])
totalPaths = sum([stats[1] for stats in statsPerTrailheads])

print('Part 1: ', totalPeaks)
print('Part 2: ', totalPaths)