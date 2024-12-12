import math
from itertools import islice

def chunked(generator, chunk_size):
    """Yield chunks of data from a generator."""
    iterator = iter(generator)
    while True:
        chunk = list(islice(iterator, chunk_size))
        if not chunk:
            break
        yield chunk

def blink(stones):
    for stone in stones:
        if (stone == '0'):
            yield '1'
            continue;
        
        stoneNumber = int(stone)
        if (math.floor(math.log10(stoneNumber)) + 1) % 2 == 0:
            yield str(stoneNumber // 10**(len(stone) // 2))
            yield str(stoneNumber % 10**(len(stone) // 2))
        else:
            yield str(stoneNumber * 2024)

with open('day11-input.txt', 'r') as file:
    stones = file.read().split(' ')
    
for _ in range(45):
    stones = blink(stones)
    
print('Part 1:', sum([1 for _ in stones]))