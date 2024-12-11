# Day 8: Resonant Collinearity

def addPoints(point1, point2):
    return tuple(a + b for a, b in zip(point1, point2))

def subtractPoints(point1, point2):
    return tuple(a - b for a, b in zip(point1, point2))

def isInMap(position, width, height):
    x, y = position
    return x >= 0 and x < width and y >= 0 and y < height

def getAntiNodesGen(antennaCoordniates):
    for coordinates in antennaCoordniates:
        for startPoint in range(len(coordinates) - 1):
            for endPoint in range(startPoint + 1, len(coordinates)):
                startPos = coordinates[startPoint]
                endPos = coordinates[endPoint]
                dPos1 = subtractPoints(endPos, startPos)
                dPos2 = subtractPoints(startPos, endPos)
                
                yield addPoints(endPos, dPos1)
                yield addPoints(startPos, dPos2)
                
def getAntiNodesWithResonantHarmonicsGen(antennaCoordniates, width, height):
    for coordinates in antennaCoordniates:
        for startPoint in range(len(coordinates) - 1):
            for endPoint in range(startPoint + 1, len(coordinates)):
                startPos = coordinates[startPoint]
                endPos = coordinates[endPoint]
                
                currPos = endPos
                dPos = subtractPoints(endPos, startPos)
                
                while isInMap(currPos, width, height):
                    yield currPos
                    currPos = addPoints(currPos, dPos)
                    
                currPos = startPos
                dPos = subtractPoints(startPos, endPos)
                
                while isInMap(currPos, width, height):
                    yield currPos
                    currPos = addPoints(currPos, dPos)

def getAntennaCoordinates(inputFile):
    antennas = {}

    with open(inputFile, 'r') as file:
            data = file.read().split('\n')
            
    for row in range(len(data)):
        for col in range(len(data[row])):
            currChar = data[row][col]
            if currChar == '.' :
                continue
            
            if not currChar in antennas:
                antennas[currChar] = []
                
            antennas[currChar].append((col, row))
            
    activeAntennas = dict(filter(lambda item: len(item[1]) > 1, antennas.items()))
    antiNodeGen = getAntiNodesGen([item[1] for item in activeAntennas.items()])
    
    antiNodes = set()
    for antiNode in antiNodeGen:
        if (isInMap(antiNode, len(data[0]), len(data))):
            antiNodes.add(antiNode)
            
    antiNodeGen = getAntiNodesWithResonantHarmonicsGen([item[1] for item in activeAntennas.items()], len(data[0]), len(data))
    antiNodesWithResonantHarmonics = set()  
    for antiNode in antiNodeGen:
        if (isInMap(antiNode, len(data[0]), len(data))):
            antiNodesWithResonantHarmonics.add(antiNode)
        
    print('Part 1: ', len(antiNodes))
    print('Part 2: ', len(antiNodesWithResonantHarmonics))
    
getAntennaCoordinates('day8-input.txt')

            