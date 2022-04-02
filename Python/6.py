"""
Create Phone Number
https://www.codewars.com/kata/525f50e3b73515a6db000b83
"""

def create_phone_number(n):
    return f"""({''.join(map(str, n[:3]))}) {''.join(map(str, n[3:6]))}-{''.join(map(str, n[6:]))}"""

"""
Multiples of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006
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
https://www.codewars.com/kata/523f5d21c841566fde000009
"""
def array_diff(a, b):
    c = []
    for i in range(len(a)):
        if not a[i] in b:
            c.append(a[i])
    return c

"""
Who likes it?
https://www.codewars.com/kata/5266876b8f4bf2da9b000362
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
    
"""
Sum of Digits / Digital Root
https://www.codewars.com/kata/541c8630095125aba6000c00
"""
def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        i = 0
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i])
        return digital_root(sum)
    
"""
Find the unique number
https://www.codewars.com/kata/585d7d5adb20cf33cb000235
"""
def find_uniq(arr):
    first = arr[0]
    arr2 = [y for y in arr if y != arr[0]]
    if len(arr2) == 1:
        return arr2[0]
    else:
        arr = [y for y in arr2 if y != arr2[0]]
        if len(arr) == 1:
            return arr[0]
        else:
            return first

"""
Break camelCase
https://www.codewars.com/kata/5208f99aee097e6552000148
"""
import string

def solution(s):
    final = ""
    for i in range(len(s)):
        if s[i].isupper():
            final += " " + s[i]
        else:
            final += s[i]
    return final

"""
Calculating with Functions
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""
def zero(operation = None): return 0 if operation is None else operation(0)
def one(operation = None): return 1 if operation is None else operation(1)
def two(operation = None): return 2 if operation is None else operation(2)
def three(operation = None): return 3 if operation is None else operation(3)
def four(operation = None): return 4 if operation is None else operation(4)
def five(operation = None): return 5 if operation is None else operation(5)
def six(operation = None): return 6 if operation is None else operation(6)
def seven(operation = None): return 7 if operation is None else operation(7)
def eight(operation = None): return 8 if operation is None else operation(8)
def nine(operation = None): return 9 if operation is None else operation(9)

def plus(a): return lambda b: a + b
def minus(a): return lambda b: b - a
def times(a): return lambda b: a * b
def divided_by(a): return lambda b: b // a

"""
Simple Fun #354: Lonely Frog III
https://www.codewars.com/kata/59c9e82ea25c8c05860001aa
"""
def jump_to(x, y):
    moves = 0
    while x != y:
        if (y / 2 >= x) and (y % 2 == 0):
            y = y / 2
        else:
            y -= 1
        moves += 1
    return moves
