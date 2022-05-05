# [Sudoku Solution Validator](https://www.codewars.com/kata/529bf0e9bdf7657179000008)
by [xDranik](https://www.codewars.com/users/xDranik)
## Description
### Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. <br/>
(More info at: http://en.wikipedia.org/wiki/Sudoku)

### Sudoku Solution Validator

Write a function `validSolution`/`ValidateSolution`/`valid_solution()` that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
 

### Examples

```
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
```

```
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
```
## Solution:
```python
def valid_solution(board):
    for r in board:
        if 0 in r:
            return False
        
    for row in board:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    
    for i in range(0,9):
        column = []
        for j in range(0,9):
            column.append(board[j][i])
        if sorted(column) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            
            if sorted(region) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
    return True
```
###
Tags: `Algorithms` `Data Structures` `Logic` `Validation`
<br>
# [Human readable duration format](https://www.codewars.com/kata/52742f58faf5485cae000b9a)
by [davazp](https://www.codewars.com/users/davazp)
## Description
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise,  the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```text
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.


### Detailed rules

The resulting expression is made of components like `4 seconds`, `1 year`, etc.  In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (`", "`). Except the last component, which is separated by `" and "`, just like it would be written in English. 

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero.  Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

 A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead.  Formally, the duration specified by  of a component must not be greater than any valid more significant unit of time.

## Solution:
```python
def format_duration(seconds):
    if seconds == 0:
        return "now"

    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    days = hours // 24
    hours = hours - (24 * days)
    years = days // 365
    days = days - (365 * years)
    
    sec_str = " second" if seconds == 1 else " seconds"
    min_str = " minute" if minutes == 1 else " minutes"
    hr_str = " hour" if hours == 1 else " hours"
    day_str = " day" if days == 1 else " days"
    year_str = " year" if years == 1 else " years"

    duration = ""
    indendation_aux = [years, days, hours, minutes, seconds]
    diff0 = 0
    for n in indendation_aux:
        if n != 0:
            diff0 += 1

    if years != 0:
        if diff0 == 1:
            duration += str(years) + year_str
            return duration
        elif diff0 == 2:
            duration += str(years) + year_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(years) + year_str + ", "
            diff0 -= 1
    
    if days != 0:
        if diff0 == 1:
            duration += str(days) + day_str
            return duration
        elif diff0 == 2:
            duration += str(days) + day_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(days) + day_str + ", "
            diff0 -= 1
            
    if hours != 0:
        if diff0 == 1:
            duration += str(hours) + hr_str
            return duration
        elif diff0 == 2:
            duration += str(hours) + hr_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(hours) + hr_str + ", "
            diff0 -= 1
            
    if minutes != 0:
        if diff0 == 1:
            duration += str(minutes) + min_str
            return duration
        elif diff0 == 2:
            duration += str(minutes) + min_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(minutes) + min_str + ", "
            diff0 -= 1
        
    if seconds != 0:
        duration += str(seconds) + sec_str
        return duration
```
###
Tags: `Algorithms` `Formats` `Strings` `Data Types` `Dates/Time` `Formatting` `Logic`
<br>
