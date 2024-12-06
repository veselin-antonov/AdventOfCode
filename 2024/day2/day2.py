# Day 2: Red-Nosed Reports

def removeElementAt(list: list, index: int):
    '''
    Returns a new list with the element ath the provided index removed
    '''
    return list[:index] + list[index + 1:]

def isReportSafe(levels: list, enableDampener: bool, depth: int = 0):
    
    '''
    The function checks if the conditions for a safe level are met
    
    We check each pair of consecutive levels for 2 things:

        1. Checks the dirrection of the progression between the first two elements
           and then uses it to see if it switches somewhere in the report
           
        2. We check if the difference between every 2 levels obides the requirements
    
    When an unsafe level is found, if the dampening is enabled, then the function calles itself
    recusively with the curent, last and second-last levels removed to try and secure the report
    '''
    # Call recursively only once (requirements)
    if depth > 1:
        return False
    
    # Get the direction of the progression
    isAscending = levels[1] > levels[0]
    
    #Check the 2 conditions for every pair of consecutive levels in the report
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        
        if ((isAscending and diff <= 0) 
            or (not(isAscending) and diff >= 0)
            or abs(diff) < 1 
            or abs(diff) > 3):
            
            # If dampener is enabled, try to remove the current, last and second-last
            # levels to secure the report, if not - the directly return false
            if (enableDampener):
                return isReportSafe(removeElementAt(levels, i - 2), True, depth + 1) or isReportSafe(removeElementAt(levels, i - 1), True, depth + 1) or isReportSafe(removeElementAt(levels, i), True, depth + 1)
            else:
                return False
    
    # If no unsafe levels are found - return true
    return True;

# Part 1 and 2 (with dampener on and off)
# We call the isReportSafe function for every line of the input and count the safe reports
def safeReportsCount(inputFile, enableDampener):
    safeLevels = 0
    
    with open(inputFile, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split(' ')))
            
            if isReportSafe(levels, enableDampener):
                safeLevels += 1
                
    print(safeLevels)

print('Part 1: ', end='')
safeReportsCount('day2-input.txt', False)

print('Part 2: ', end='')
safeReportsCount('day2-input.txt', True)