# [Battleship field validator](https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7)
by [romanzes](https://www.codewars.com/users/romanzes)
## Description
<p>Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.</p>
<p><b>Battleship</b> (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.</p>
<img src="http://i.imgur.com/IWxeRBV.png"><br>
Before the game begins, players set up the board and place the ships accordingly to the following rules:<br>
<ul>
<li>There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.</li>
<li>Each ship must be a straight line, except for submarines, which are just single cell.<br>
<img src="http://i.imgur.com/FleBpT9.png"></li>
<li>The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.<br>
<img src="http://i.imgur.com/MuLvnug.png"></li>
</ul>
This is all you need to solve this kata. If you're interested in more information about the game, visit <a href="http://en.wikipedia.org/wiki/Battleship_(game)">this link</a>.
## Solution:
```python
surroundings = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_surroundings(row, col):
    return [(row + surrounding[0], col + surrounding[1]) for surrounding in surroundings if (row + surrounding[0] >= 0 and row + surrounding[0] <= 9) and (col + surrounding[1] >= 0 and col + surrounding[1] <= 9)]

def validate_battlefield(field):
    battleship = 1
    cruiser = 2
    destroyer = 3
    submarine = 4
    checked = []
    
    for row_index, row in enumerate(field):
        for col_index, col in enumerate(row):
            if (row_index, col_index) in checked:
                continue
            if field[row_index][col_index] == 1 and all([field[surrounding[0]][surrounding[1]] == 0 for surrounding in get_surroundings(row_index, col_index)]):
                submarine -= 1
                checked.extend([(row_index, col_index)])
            
            # battleship to the right
            elif (col_index == 6 or (col_index < 6 and field[row_index][col_index + 4] == 0)) and all([field[row_index][col_index] == 1, field[row_index][col_index + 1] == 1, field[row_index][col_index + 2] == 1, field[row_index][col_index + 3] == 1]):
                battleship -= 1
                checked.extend([(row_index, col_index), (row_index, col_index + 1), (row_index, col_index + 2), (row_index, col_index + 3)])

            # battleship down
            elif (row_index == 6 or (row_index < 6 and field[row_index + 4][col_index] == 0)) and all([field[row_index][col_index] == 1, field[row_index + 1][col_index] == 1, field[row_index + 2][col_index] == 1, field[row_index + 3][col_index] == 1]):
                battleship -= 1
                checked.extend([(row_index, col_index), (row_index + 1, col_index), (row_index + 2, col_index), (row_index + 3, col_index)])

            # cruiser to the right
            elif (col_index == 7 or (col_index < 7 and field[row_index][col_index + 3] == 0)) and all([field[row_index][col_index] == 1, field[row_index][col_index + 1] == 1, field[row_index][col_index + 2] == 1]):
                cruiser -= 1
                checked.extend([(row_index, col_index), (row_index, col_index + 1), (row_index, col_index + 2)])

            # cruiser down
            elif (row_index == 7 or (row_index < 7 and field[row_index + 3][col_index] == 0)) and all([field[row_index][col_index] == 1, field[row_index + 1][col_index] == 1, field[row_index + 2][col_index] == 1]):
                cruiser -= 1
                checked.extend([(row_index, col_index), (row_index + 1, col_index), (row_index + 2, col_index)])

            # destroyer to the right
            elif (col_index == 8 or (col_index < 8 and field[row_index][col_index + 2] == 0)) and all([field[row_index][col_index] == 1, field[row_index][col_index + 1] == 1]):
                destroyer -= 1
                checked.extend([(row_index, col_index), (row_index, col_index + 1)])
            
            # destroyer down
            elif (row_index == 8 or (row_index < 8 and field[row_index + 2][col_index] == 0)) and all([field[row_index][col_index] == 1, field[row_index + 1][col_index] == 1]):
                destroyer -= 1
                checked.extend([(row_index, col_index), (row_index + 1, col_index)])
            
    return battleship == cruiser == destroyer == submarine == 0
```
###
Tags: `Games` `Arrays` `Algorithms`
<br>
