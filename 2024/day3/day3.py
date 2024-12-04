import re

def uncorruptedInstructionsResult(inputFile):
    
    data = ""
    with open(inputFile, 'r') as file:
        data = file.read()
    
    matches = re.finditer(r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', data)
    
    result = 0
    skipNext = False;
    
    for match in matches:
        if match.group(3) == 'do':
            skipNext = False;
        elif match.group(4) == 'don\'t':
            skipNext = True;
        elif not skipNext:
            result += int(match.group(1)) * int(match.group(2))
    
    print(result)
    
def uncorruptedInstructionsResult2(inputFile):
    
    data = ""
    with open(inputFile, 'r') as file:
        data = 'do()' + file.read() + 'don\'t()'
    
    multPattern = r'mul\((\d+),(\d+)\)'
    conditionalPattern = r'do\(\)(.*?)don\'t\(\)'

    enabledBlocks = re.finditer(conditionalPattern, data)
    
    result = 0
    
    for block in enabledBlocks:
        multiplications = re.finditer(multPattern, block.group(0))
        
        for match in multiplications:
            result += int(match.group(1)) * int(match.group(2))
    
    print(result)
    
uncorruptedInstructionsResult('day3-input.txt')