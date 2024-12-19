# Day 13: Claw Contraption

class Machine():
    def __init__(self, a, b, prize):
        self.a = a  # Button a value
        self.b = b # Button b value
        self.prize = prize

def cheapestReward(machine: Machine, prizeAdjustment = 0):
    aX, aY = machine.a
    bX, bY = machine.b
    pX = machine.prize[0] + prizeAdjustment
    pY = machine.prize[1] + prizeAdjustment
    
    # We need to solve the following system of equations: 
    # 
    # | c * Ax + d * Bx = Px
    # | c * Ay + d * By = Py
    # 
    # Which is represented as the following matrix:
    #
    # | Ax  Bx | | c | = | Px |
    # | Ay  By | | d | = | Py |
    #     A        x   =   P
    
    # We can use cramer's rule to solve this system of equations
    # 
    #          | Px  Bx | 
    # c = det( | Py  By | ) / det ( A ) = (Px * By - Py * Bx) / (Ax * By - Ay * Bx)
    # 
    #          | Ax  Px |
    # d = det( | Ay  Py | ) / det ( A ) = (Ax * Py - Ay * Px) / (Ax * By - Ay * Bx)
    # 
    # Then we just calculate the number of tokens:
    # 
    # c, d = pressesA, pressesB; tokens = 3 * pressesA + pressesB
    
    detA = aX * bY - aY * bX
    pressesA = (pX * bY - pY * bX) / detA
    pressesB = (aX * pY - aY * pX) / detA
    
    if pressesA == int(pressesA) and pressesA >= 0 and pressesB == int(pressesB) and pressesB >= 0:
        return int(pressesA * 3 + pressesB)
    else:
        return 0

machines = []
with open('day13-input.txt', 'r') as file:
    lines = [file.readline() for _ in range(4)]
    while len(lines) > 0:
        values = lines[0].strip().removeprefix('Button A: ').split(', ')
        buttonA = (int(values[0].removeprefix('X+')), int(values[1].removeprefix('Y+')))

        values = lines[1].strip().removeprefix('Button B: ').split(', ')
        buttonB = (int(values[0].removeprefix('X+')), int(values[1].removeprefix('Y+')))
        
        values = lines[2].strip().removeprefix('Prize: ').split(', ')
        prize = (int(values[0].removeprefix('X=')), int(values[1].removeprefix('Y=')))
        
        machines.append(Machine(buttonA, buttonB, prize))
        
        lines = [line for line in [file.readline() for _ in range(4)] if line != '']
        
print('Part 1: ', sum([cheapestReward(machine) for machine in machines]))
print('Part 2: ', sum([cheapestReward(machine, 10000000000000) for machine in machines]))