# Day 8: Resonant Collinearity

def isInMap(position, width, height):
    x, y = position
    return x >= 0 and x < width and y >= 0 and y < height

def generateAntennaAntinodes(antennas):
    for antenna in antennas:
        coordinates = antenna[1]
        for startPoint in range(len(coordinates) - 1):
            for endPoint in range(startPoint + 1, len(coordinates)):
                yield (coordinates[startPoint], coordinates[endPoint])

def getAntennaCoordinates(inputFile):
    antennas = {}

    with open(inputFile, 'r') as file:
            data = file.read().split('\n')
            
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '.' :
                continue
            
            if not data[row][col] in antennas:
                antennas[data[row][col]] = []
                
            antennas[data[row][col]].append((row, col))
            
    activeAntennas = dict(filter(lambda item: len(item[1]) > 1, antennas.items()))
    
    [print(f'{antenna}: {coordinates}') for antenna, coordinates in activeAntennas.items()]
    
getAntennaCoordinates('day8-input.txt')

            