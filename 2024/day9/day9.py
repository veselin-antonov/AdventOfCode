# Day 9: Disk Fragmenter

import sys

sys.setrecursionlimit(10**5)

def parseData(compressedData):
    data = []
    dataID = 0
    for i in range(0, len(compressedData) - 1, 2):
        dataBlockSize = int(compressedData[i])
        
        for _ in range (dataBlockSize):
            data.append(dataID)
            
        emptyBlockSize = int(compressedData[i + 1])
        
        for _ in range (emptyBlockSize):
            data.append(-1)
            
        dataID += 1
            
    return data

def parseDataRecursively(data, dataID = 0):
    if len(data) == 0:
        return []
    else:
        parsedData = list([dataID for _ in range(int(data[0]))])
        parsedData.extend(list([-1 for _ in range(int(data[1]))]))
        parsedData.extend(parseDataRecursively(data[2:], dataID + 1))
        return parsedData
    
def parseDataInGroups(compressedData):
    data = []
    dataID = 0
    for i in range(0, len(compressedData) - 1, 2):
        dataBlockGroupSize = int(compressedData[i])
        data.append(list([dataID for _ in range(dataBlockGroupSize)]))
            
        emptyBlockGroupSize = int(compressedData[i + 1])
        data.append(list([-1 for _ in range(emptyBlockGroupSize)]))
            
        dataID += 1
            
    return data
    

def compressData(dataBlocks):
    index = 0
    while index < len(dataBlocks):
        if dataBlocks[index] == -1:
            while dataBlocks[len(dataBlocks) - 1] == -1:
                dataBlocks.pop()
                
            if (index >= len(dataBlocks)):
                break;
            
            dataBlocks[index] = dataBlocks.pop()
        index += 1
            
    return dataBlocks

def compressDataRecursively(dataBlocks):
    if len(dataBlocks) == 0:
        return []
    elif dataBlocks[0] != -1:
        data = [dataBlocks[0]]
        data.extend(compressDataRecursively(dataBlocks[1:]))
        return data
    elif dataBlocks[-1] == -1:
        return compressDataRecursively(dataBlocks[:-1])
    else:
        data = [dataBlocks.pop()]
        data.extend(compressDataRecursively(dataBlocks[1:]))
        return data
    
def compressDataWithoutFragmentation(dataBlockGroups: list):
    currentFileID = dataBlockGroups[-2][0]
    for currentFileIndex in range(len(dataBlockGroups) - 1, 0, -1):
        currentFile = dataBlockGroups[currentFileIndex]
        currentFileSize = len(currentFile)
        if currentFileSize > 0 and currentFile[0] == currentFileID:
            for emptySpanIndex in range(currentFileIndex):
                emptySpan = dataBlockGroups[emptySpanIndex]
                emptySpanSize = len(emptySpan)
                if emptySpanSize > 0 and emptySpan[0] == -1 and len(currentFile) <= len(emptySpan):
                    dataBlockGroups[emptySpanIndex] = emptySpan[len(currentFile):]
                    dataBlockGroups.insert(emptySpanIndex, currentFile)
                    dataBlockGroups[currentFileIndex + 1] = [-1 for _ in range(currentFileSize)]
                    currentFileIndex += 1
                    break
            currentFileID -= 1;
            
    return [dataBlock for dataBlockGroup in dataBlockGroups for dataBlock in dataBlockGroup]

def checkSum(data):
    return sum([data[i] * i for i in range(len(data)) if data[i] > 0])
    
def variant1(inputFile):
    with open(inputFile, 'r') as file:
            data = file.read().strip() + '0'
            
    parsedData = parseData(data)
    # parsedData = parseDataRecursively(data)
    parsedData2 = parseDataInGroups(data)
            
    compressedData = compressData(parsedData)
    # compressedData = compressDataRecursively(parsedData)
    compressedData2 = compressDataWithoutFragmentation(parsedData2)
    
    print('Part 1: ', checkSum(compressedData))
    print('Part 2: ', checkSum(compressedData2))
    
variant1('day9-input.txt')

class Memory():
    def __init__(b, pos, size):
        b.pos = pos  # Starting position of the block
        b.size = size  # Length of the block
        
    def __repr__(b):
        return f'Mem(pos: {b.pos}, size: {b.size})'
    
    # Calculate the value of the block based on the indexes it takes up using teh formula for Arithmetic Progression
    def value(b):
        return (2 * b.pos + b.size - 1) * b.size // 2
    
def parseMemoryBlocks(diskData):
    memoryBlocks = []
    position = 0
    for bitSize in map(int, diskData):
        memoryBlocks.append(Memory(position, bitSize))
        position += bitSize
        
    return memoryBlocks

def compressMemory(memoryBLocks):
    for fileBlock in memoryBLocks[::-2]:
        for emptyBlock in memoryBLocks[1::2]:
            if (emptyBlock.pos < fileBlock.pos
            and emptyBlock.size >= fileBlock.size):
                fileBlock.pos = emptyBlock.pos
                emptyBlock.pos += fileBlock.size
                emptyBlock.size -= fileBlock.size
                
def checkSumMemory(memoryBlocks):
    return sum(id * memoryBlock.value() for id, memoryBlock in enumerate(memoryBlocks[::2]))
        
def variant2(inputFile):
    with open(inputFile, 'r') as file:
        diskData = file.read().strip()
        
    memoryBlocks = parseMemoryBlocks(diskData)
    
    compressMemory(memoryBlocks)
    
    print('Part 2 (V2): ', checkSumMemory(memoryBlocks))
    
variant2('day9-input.txt')