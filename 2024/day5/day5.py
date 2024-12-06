# Day 5: Print Queue

# Part 1
def isOrderedCorrecrtly(pageNumbers, smallerPerPage): 
    checked = []
    
    for i in range(len(pageNumbers)):
        for number in checked:
            if number in smallerPerPage and pageNumbers[i] in smallerPerPage[number]:
                return 0;
        checked.append(pageNumbers[i])
            
    return int(pageNumbers[(len(pageNumbers) + 2 - 1) // 2 - 1])

# Part 2
def fixOrder(pageNumbers, smallerPerPage):
    fixed = []
    
    for currentPage in range(len(pageNumbers)):
        indexToInsert = currentPage
        
        for indexInFixed in range(len(fixed)):
            if fixed[indexInFixed] in smallerPerPage and pageNumbers[currentPage] in smallerPerPage[fixed[indexInFixed]]:
                indexToInsert = min(indexToInsert, indexInFixed)
                
        fixed.insert(indexToInsert, pageNumbers[currentPage])
        
    return int(fixed[(len(fixed) + 2 - 1) // 2 - 1])  

# Calculating result for both parts
def orderPages(inputFile):
    with open(inputFile, 'r') as file:
        data = file.read().split('\n\n')
    
    orderRules = data[0].split('\n')
    pageLists = data[1].split('\n')
    
    smallerPerNumber = dict()
    
    for rule in orderRules:
        value, key = rule.split('|')
        
        if not key in smallerPerNumber:
            smallerPerNumber[key] = set()
        smallerPerNumber[key].add(value)
        
    result = 0;
    fixedResult = 0
    
    for pageList in pageLists:
        pageNumbers = pageList.split(',')
        
        middleElement = isOrderedCorrecrtly(pageNumbers, smallerPerNumber);
        
        if middleElement == 0:
            fixedResult += fixOrder(pageNumbers, smallerPerNumber)
        else:
            result += middleElement

    print(f'Part 1: {result}')
    print(f'Part 2: {fixedResult}')
        
orderPages('day5-input.txt')