
# Hlulani Myambo
# Towers of Hanoi

"""
How it works:
1. You are given set of three pegs and n disks. Each disk has a different size.
2. Name of the pegs are A, B, C => pegs == Rods
3. disks are numbered from smallest to largest where the smallest == 1 and the largest == n
4. All disks are at peg A or Rod A and packed in decreasing order where the smallest is at the top and the largest is at the bottom.
5. The goal is to move from all disks from rod A to rod B

Rules:
    1. You are only allowed to move one disk at a time.
    2. The top disk must not be greater that the disk below it
     meaning if 4 is on a certain rod then all disks below it must be greater than it and what comes at the top must be smaller than 4

Time complexity(Asymptotic behaviour): O(2^n)
"""

def tower_of_hanoi(number):
    if number == 1:
        ...