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
Where my anagrams at?
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""
def anagrams(word, words):
    anagrams = []
    for w in words:
        if sorted(w) == sorted(word):
            anagrams.append(w)
    return anagrams

"""
Did I Finish my Sudoku?
https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
"""
def done_or_not(board):
    for row in board:
        if sorted(row) != [1,2,3,4,5,6,7,8,9]:
            return "Try again!"

        
    for i in range(0,9):
        col = []
        for row in board:
            col.append(row[i])
        if sorted(col) != [1,2,3,4,5,6,7,8,9]:
            return "Try again!"
        
    blocks = {1: (0,0), 2: (3,0), 3: (6,0),
             4: (0,3), 5: (3,3), 6: (6,3), 
             7: (0,6), 8: (3,6), 9: (6,6)}
    
    def check_block(block):
        coord1 = block[0]
        coord2 = block[1]

        zone = []
        for i in range(coord1, coord1 + 3):
            for j in range(coord2, coord2 + 3):
                zone.append(board[j][i])
               
        if sorted(zone) != [1,2,3,4,5,6,7,8,9]:
            return 0
        else:
            return 1

    for block in blocks:
        if check_block(blocks[block]) == 0:
            return "Try again!"
        
    return "Finished!"