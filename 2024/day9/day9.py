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
        dataBlockGroup = list([dataID for _ in range(dataBlockGroupSize)])
        if (dataBlockGroupSize > 0):
            data.append(dataBlockGroup)
            
        emptyBlockGroupSize = int(compressedData[i + 1])
        emptyBlockGroup = list([-1 for _ in range(emptyBlockGroupSize)])
        if (emptyBlockGroupSize > 0):
            data.append(emptyBlockGroup)
            
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
    
def compressDataWithoutFragmentation(dataBlockGroups):
    lastGroupIndex = len(dataBlockGroups) - 1
    for groupIndex in range(len(dataBlockGroups)):
        
        if (groupIndex >= lastGroupIndex):
                break;
            
        group = dataBlockGroups[groupIndex]
        
        if group[0] == -1:
            lastGroup = dataBlockGroups[lastGroupIndex]
            while lastGroup[0] == -1 or len(lastGroup) > len(group):
                lastGroupIndex -= 1
                lastGroup = dataBlockGroups[lastGroupIndex]
                
            dataBlockGroups[groupIndex] = lastGroup
            dataBlockGroups[lastGroupIndex] = []
            
            lastGroupIndex -= 1
            
    return [dataBlock for dataBlockGroup in dataBlockGroups for dataBlock in dataBlockGroup]

def checkSum(data):
    return sum([data[i] * i for i in range(len(data))])
    
def part1(inputFile):
    with open(inputFile, 'r') as file:
            data = file.read().strip() + '0'
            
    parsedData = parseDataInGroups(data)
            
    compressedData = compressDataWithoutFragmentation(parsedData)
    
    print(checkSum(compressedData))
    
part1('day9-input.txt')