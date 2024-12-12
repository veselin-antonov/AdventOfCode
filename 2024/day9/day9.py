# Day 9: Disk Fragmenter

import sys, re

sys.setrecursionlimit(10**5)

def parseData(compressedData):
    data = []
    dataID = 0
    for i in range(0, len(compressedData) - 1, 2):
        dataBlockSize = int(compressedData[i])
        
        for _ in range (dataBlockSize):
            data.append(str(dataID))
            
        emptyBlockSize = int(compressedData[i + 1])
        
        for _ in range (emptyBlockSize):
            data.append('.')
            
        dataID += 1
            
    return data

def parseFileDataRecursively(compressedData, dataID = 0):
    if len(compressedData) == 0:
        return []
    else:
        data = list([str(dataID) for _ in range(int(compressedData[0]))])
        data.extend(list(['.' for _ in range(int(compressedData[1]))]))
        data.extend(parseFileDataRecursively(compressedData[2:], dataID + 1))
        return data
    
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
        if dataBlocks[index] == '.':
            while dataBlocks[len(dataBlocks) - 1] == '.':
                dataBlocks.pop()
                
            if (index >= len(dataBlocks)):
                break;
            
            dataBlocks[index] = dataBlocks.pop()
        index += 1
            
    return dataBlocks

def compressDataRecursively(dataBlocks):
    if len(dataBlocks) == 0:
        return []
    elif dataBlocks[0] != '.':
        data = [dataBlocks[0]]
        data.extend(compressDataRecursively(dataBlocks[1:]))
        return data
    elif dataBlocks[-1] == '.':
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
    
def part1(inputFile):
    with open(inputFile, 'r') as file:
            data = file.read().strip() + '0'
            
    parsedData = parseDataInGroups(data)
            
    compressedData = compressDataWithoutFragmentation(parsedData)
    
    print(compressedData)
    print(checkSum(compressedData))
    
part1('day9-input.txt')