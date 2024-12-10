# Day 7: Bridge Repair

import math

def isValid(operands, result, concatenate = False):
    if operands[0] > result:
        return False
    
    if len(operands) == 1:
        return operands[0] == result
    
    if (isValid([operands[0] + operands[1]] + operands[2:], result, concatenate)):
        return True
    elif (isValid([operands[0] * operands[1]] + operands[2:], result, concatenate)):
        return True
    else:
        concatenated = operands[0] * 10**int(math.log10(operands[1]) + 1) + operands[1]
        return isValid([concatenated] + operands[2:], result, concatenate) if concatenate else False

def tryToFixEquation(inputFile):
    with open(inputFile, 'r') as file:
        data = file.read().split('\n')

    equations = []
    for line in data:
        parts = line.split(': ')
        result = int(parts[0])
        operands = [int(num) for num in parts[1].split(' ')]
        equations.append((result, operands))
        
    possibleResults = 0;
    possibleResults2 = 0;
    for result, operands in equations:
        possibleResults += result if isValid(operands, result) else 0
        possibleResults2 += result if isValid(operands, result, True) else 0 
                    
    print('Part 1: ', possibleResults)
    print('Part 2: ', possibleResults2)

        
tryToFixEquation('day7-input.txt')
        
