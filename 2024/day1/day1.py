# Day 1: Historian Hysteria

# Part 1
def listDifferences(inputFile):
    list1 = []
    list2 = []

    with open(inputFile, 'r') as file:
        for line in file:
            data = line.strip().split('   ')
            list1.append(int(data[0]))
            list2.append(int(data[1]))
            
    list1.sort()
    list2.sort()

    diff = 0

    for i in range(0, len(list1)):
        diff += abs(list1[i] - list2[i])
        
    print(diff)
    
# Part 2
def occurences(inputFile):
    list1 = []
    list2 = []

    with open(inputFile, 'r') as file:
        for line in file:
            data = line.strip().split('   ')
            list1.append(int(data[0]))
            list2.append(int(data[1]))

    occurences = dict()
    numbers = set()

    for i in range(0, len(list1)):
        numbers.add(list1[i])
        if list2[i] in occurences:
            occurences[list2[i]] += 1
        else:
            occurences[list2[i]] = 1
        
    similarityScore = 0;
    for number in numbers:
        if number in occurences:
            similarityScore += number * occurences[number]
            
    print(similarityScore)
    
print('Part 1: ', end='')
listDifferences('day1-input.txt', False)

print('Part 2: ', end='')
occurences('day1-input.txt', True)