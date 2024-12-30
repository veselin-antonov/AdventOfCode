def moveTimes(count: int, robot: tuple[tuple[int, int], tuple[int, int]], mapSize: tuple[int, int]):
    pos, v = robot
    pX, pY = pos
    vX, vY = v
    width, height = mapSize
    
    x = (pX + ((((vX * count) % width) + width) % width)) % width
    y = (pY + ((((vY * count) % height) + height) % height)) % height
    
    
    return ((x, y), v)

def getQuadrant(pos: tuple[int, int], mapSize: tuple[int, int]):
    x, y = pos
    width, height = mapSize
    
    if x < width // 2:
        if y < height // 2:
            return 1
        elif y > height // 2:
            return 4
    elif x > width // 2:
        if y < height // 2:
            return 2
        elif y > height // 2:
            return 3
        
    return 0

def christmasTree(robots: list):
    robots = sorted(robots)
    

robots = []
with open('day14-input.txt', 'r') as file:
    for line in file:
        data = line.split(' ')
        
        pos = data[0].removeprefix('p=').split(',')
        pos = (int(pos[0]), int(pos[1]))

        vel = data[1].removeprefix('v=').split(',')
        vel = (int(vel[0]), int(vel[1]))
        
        robots.append((pos, vel))
  
print('Robots: ', robots)
robotsInQuadrants = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
mapSize = (101, 103)
for robot in robots:
    robotsInQuadrants[getQuadrant(moveTimes(100, robot, mapSize)[0], mapSize)] += 1
    
result = 1
for i in range(1, 5):
    result *= robotsInQuadrants[i]
print(result)

while not christmasTree([robot[0] for robot in robots]):
    