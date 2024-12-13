import math

def blink(stone):
        if (stone == 0):
            yield [1]
        
        stoneNumber = int(stone)
        digitsCount = (math.floor(math.log10(stoneNumber)) + 1)
        if digitsCount % 2 == 0:
            halfDigits = 10**(digitsCount // 2)
            yield [stoneNumber // halfDigits, stoneNumber % halfDigits]
        else:
            yield [stoneNumber * 2024]

with open('day11-input.txt', 'r') as file:
    stones = file.read().split(' ')
    
countPerStone = dict()
for stone in map(int, stones):
    if not stone in countPerStone:
        countPerStone[stone] = 1
    else:
        countPerStone[stone] += 1
   
part1 = 0
part2 = 0
        
for i in range(75):
    newCountPerStone = dict()
    for stone, count in countPerStone.items():
        newStones = next(blink(stone))
        for newStone in newStones:
            if not newStone in newCountPerStone:
                newCountPerStone[newStone] = count
            else:
                newCountPerStone[newStone] += count
    if (i == 25):
        part1 = sum(countPerStone.values())
    countPerStone = newCountPerStone

print('Part 1:', part1)
print('Part 2:', sum(countPerStone.values()))