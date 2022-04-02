"""
Multiples of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""
def solution(number):
    sum = 0
    i = 0
    while i < number:
        if i % 15 == 0:
            sum += i
        elif ((i % 5)  == 0 )or ((i % 3) == 0):
            sum += i
        i += 1
    return sum


"""
Array.diff
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
"""
def array_diff(a, b):
    c = []
    for i in range(len(a)):
        if not a[i] in b:
            c.append(a[i])
    return c

"""
Who likes it?
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"