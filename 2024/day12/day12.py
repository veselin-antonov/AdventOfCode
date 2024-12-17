# Day 12: Garden Groups

from utils import Direction, isInbounds

def countEdgesForPos(pos, region):
    directions = [
        (Direction.NORTH, Direction.EAST, Direction.NORTH_EAST),
        (Direction.EAST, Direction.SOUTH, Direction.SOUTH_EAST),
        (Direction.SOUTH, Direction.WEST, Direction.SOUTH_WEST),
        (Direction.WEST, Direction.NORTH, Direction.NORTH_WEST),
    ]
    
    edges = 0
    for d1, d2, diag in directions:
        # Outer Edges
        if d1.move(pos) not in region and d2.move(pos) not in region:
            edges += 1
        # Inner Edges
        if d1.move(pos) in region and d2.move(pos) in region and diag.move(pos) not in region:
            edges += 1
            
    return edges

def countEdges(region):
    sides = 0
    for pos in region:
        sides += countEdgesForPos(pos, region)

    return sides

def exploreRegion(symbol, pos, direction, garden, visited, boundries):
    if not isInbounds(pos, len(garden), len(garden[0])) or symbol != garden[pos[0]][pos[1]]:
        boundries.append(pos)
        return
    elif pos in visited:
        return
    else:    
        visited.add(pos)
        exploreRegion(symbol, direction.move(pos), direction, garden, visited, boundries)
        exploreRegion(symbol, direction.turnLeft().move(pos), direction.turnLeft(), garden, visited, boundries)
        exploreRegion(symbol, direction.turnRight().move(pos), direction.turnRight(), garden, visited, boundries)

with open('day12-input.txt', 'r') as file:
    garden = file.read().split('\n')

result = 0
regions = []
for row in range(len(garden)):
    for col in range(len(garden[0])):
        if all(not (row, col) in region[0] for region in regions):
            region = set()
            boundries = [(row - 1, col)]
            exploreRegion(garden[row][col], (row, col), Direction.EAST, garden, region, boundries)
            regions.append((region, boundries))
            print('Region:', garden[row][col])
            print('Plots:', len(region))
            print('Sides:', countEdges(region))
            print()

print('Part 1:', sum([len(region) * len(boundries) for region, boundries in regions]))
print('Part 2:', sum([len(region) * countEdges(region) for region, _ in regions]))