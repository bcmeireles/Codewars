# [Tic-Tac-Toe Checker](https://www.codewars.com/kata/525caa5c1bf619d28c000335)
by [eugene-bulkin](https://www.codewars.com/users/eugene-bulkin)
## Description
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty, `1` if it is an "X", or `2` if it is an "O", like so:

```
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

* `-1` if the board is not yet finished AND no one has won yet (there are empty spots),
* `1` if "X" won,
* `2` if "O" won,
* `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
## Solution:
```python
def is_solved(board):
    for row in board:
        if row == [1,1,1]:
            return 1
        elif row == [2,2,2]:
            return 2
        
    for i in range(0,3):
        col = []
        for j in range(0,3):
            col.append(board[j][i])
        if col == [1,1,1]:
            return 1
        elif col == [2,2,2]:
            return 2
        
    if (board[1][1] != 0) and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        return board[1][1]
    
    for row in board:
        if 0 in row:
            return -1
    return 0
```
###
Tags: `Arrays` `Algorithms`
<br>
# [The Hashtag Generator](https://www.codewars.com/kata/52449b062fb80683ec000024)
by [AKJ.IO](https://www.codewars.com/users/AKJ.IO)
## Description
The marketing team is spending way too much time typing in hashtags.   
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.


## Examples

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```
## Solution:
```python
def generate_hashtag(s):
    if s == "":
        return False
    
    words = [word.capitalize() for word in s.split()]
    a = "".join(words)
    if len(a) > 139:
        return False
    return "#" + a
    
```
###
Tags: `Strings` `Algorithms`
<br>
# [Did I Finish my Sudoku?](https://www.codewars.com/kata/53db96041f1a7d32dc0004d2)
by [suuuzi](https://www.codewars.com/users/suuuzi)
## Description
Write a function done_or_not/`DoneOrNot` passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:

<img src="http://www.sudokuessentials.com/images/Row.gif">

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

Columns:

<img src="http://www.sudokuessentials.com/images/Column.gif">

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

Regions

<img src="http://www.sudokuessentials.com/images/Region.gif">

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region. 

Valid board example:

<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/364px-Sudoku-by-L2G-20050714_solution.svg.png">

For those who don't know the game, here are some information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/
## Solution:
```python
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
```
###
Tags: `Lists` `Data Structures` `Mathematics` `Puzzles`
<br>
# [Where my anagrams at?](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)
by [sandbochs](https://www.codewars.com/users/sandbochs)
## Description
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```javascript
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

**Note for Go**\
For Go: Empty string slice is expected when there are no anagrams found.


## Solution:
```python
def anagrams(word, words):
    anagrams = []
    for w in words:
        if sorted(w) == sorted(word):
            anagrams.append(w)
    return anagrams
```
###
Tags: `Strings` `Algorithms`
<br>
# [Calculating with Functions](https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39)
by [BattleRattle](https://www.codewars.com/users/BattleRattle)
## Description
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```javascript
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```
```haskell
seven $ times $ five   ->  35 :: Int
four $ plus $ nine     ->  13 :: Int
eight $ minus $ three  ->   5 :: Int
six $ dividedBy $ two  ->   3 :: Int
```
```ruby
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
```
```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
```factor
seven multiplied-by five   ! must evaluate to 35
four plus nine             ! must evaluate to 13
eight minus three          ! must evaluate to 5
six divided-by two         ! must evaluate to 3
```

Requirements:
~~~if:ruby,python
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if:factor
* There must be a word for each number from 0 ("zero") to 9 ("nine")
* There must be a word for each of the following mathematical operations: plus, minus, multiplied-by, divided-by
* Each calculation consist of exactly one operation and two numbers
* The leftmost word represents the left operand, the rightmost word represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if-not:ruby,python,factor
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~

```javascript
eight(dividedBy(three()));
```
```haskell
eight $ dividedBy $ three
```
```ruby
eight(divided_by(three))
```
```python
eight(divided_by(three()))
```
```factor
eight divided-by three
```
## Solution:
```python
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
```
###
Tags: `Functional Programming`
<br>
