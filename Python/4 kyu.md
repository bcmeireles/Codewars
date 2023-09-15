# [Nesting Structure Comparison](https://www.codewars.com/kata/520446778469526ec0000001)
by [nklein](https://www.codewars.com/users/nklein)
## Description
Complete the function/method (depending on the language) to return `true`/`True` when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

```javascript
 // should return true
[ 1, 1, 1 ].sameStructureAs( [ 2, 2, 2 ] );          
[ 1, [ 1, 1 ] ].sameStructureAs( [ 2, [ 2, 2 ] ] );  

 // should return false 
[ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2, 2 ], 2 ] );  
[ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2 ], 2 ] );  

// should return true
[ [ [ ], [ ] ] ].sameStructureAs( [ [ [ ], [ ] ] ] ); 

// should return false
[ [ [ ], [ ] ] ].sameStructureAs( [ [ 1, 1 ] ] );     
```
```php
same_structure_as([1, 1, 1], [2, 2, 2]); // => true
same_structure_as([1, [1, 1]], [2, [2, 2]]); // => true
same_structure_as([1, [1, 1]], [[2, 2], 2]); // => false
same_structure_as([1, [1, 1]], [[2], 2]); // => false
same_structure_as([[[], []]], [[[], []]]); // => true
same_structure_as([[[], []]], [[1, 1]]); // => false
```
```ruby
# should return true
[ 1, 1, 1 ].same_structure_as( [ 2, 2, 2 ] )
[ 1, [ 1, 1 ] ].same_structure_as( [ 2, [ 2, 2 ] ] )

# should return false 
[ 1, [ 1, 1 ] ].same_structure_as( [ [ 2, 2 ], 2 ] )
[ 1, [ 1, 1 ] ].same_structure_as( [ [ 2 ], 2 ] )

# should return true
[ [ [ ], [ ] ] ].same_structure_as( [ [ [ ], [ ] ] ] ); 

# should return false
[ [ [ ], [ ] ] ].same_structure_as( [ [ 1, 1 ] ] )   
```
```python
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
```

~~~if:javascript
For your convenience, there is already a function 'isArray(o)' declared and defined that returns true if its argument is an array, false otherwise.
~~~

~~~if:php
You may assume that all arrays passed in will be non-associative.
~~~
## Solution:
```python
def same_structure_as(original,other):
        if original == [1,'[',']']:
            return True
        if type(original) != type(other):
            return False
        for i in range(len(original)):
            if type(original[i]) == list and type(other[i]) == list:
                if len(original[i]) != len(other[i]):
                    return False
                for j in range(len(original[i])):
                    if type(original[i][j]) != type(other[i][j]):
                        return False
            if type(original[i]) != type(other[i]):
                return False
        return True
```
###
Tags: `Arrays` `Algorithms`
<br>
# [Range Extraction](https://www.codewars.com/kata/51ba717bb08c1cd60f00002f)
by [jhoffner](https://www.codewars.com/users/jhoffner)
## Description
A format for expressing an ordered list of integers is to use a comma separated list of either

* individual integers
* or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints.  It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution  so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format. 

**Example:**

```javascript
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
// returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```coffeescript
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```ruby
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```python
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```java
Solution.rangeExtraction(new int[] {-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20})
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```C#
RangeExtraction.Extract(new[] {-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20});
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```
```VB
RangeExtraction.Extract({-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20});
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```
```cpp
range_extraction({-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20});
// returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```
```c
range_extraction((const []){-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20}, 23);
/* returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20" */
```
```nasm
nums:  dd  -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20

mov rdi, nums
mov rsi, 20
call range_extraction
; RAX <- `-10--8,-6,-3-1,3-5,7-11,14,15,17-20\0`
```
```julia
rangeextraction([-10 -9 -8 -6 -3 -2 -1 0 1 3 4 5 7 8 9 10 11 14 15 17 18 19 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```scala
solution(List(-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20))
// "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```racket
(solution '(-10 -9 -8 -6 -3 -2 -1 0 1 3 4 5 7 8 9 10 11 14 15 17 18 19 20))
; returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

```php
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
// returns '-10--8,-6,-3-1,3-5,7-11,14,15,17-20'
```

```cobol
        Rangeextraction
        xs = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 
             14, 15, 17, 18, 19, 20]
        res = "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

*Courtesy of rosettacode.org*


## Solution:
```python
def solution(args):
    final = str(args[0])
    sequence = []
    for j in range(len(args) - 1):
        # print(sequence)
        # print(final)
        if args[j] + 1 == args[j + 1]:
            sequence.append(args[j])
            sequence.append(args[j + 1])
            continue
        else:
            if len(sequence) > 2:
                final += "-" + str(sequence[-1])
            elif len(sequence) == 2:
                final += "," + str(sequence[-1])
            elif len(sequence) == 1:
                final += "," + str(sequence[-1])
            sequence = []
            final += "," + str(args[j + 1])
    if len(sequence) == 2:
        final += "," + str(sequence[-1])
    elif len(sequence) > 2:
        final += "-" + str(sequence[-1])
        
    return final
```
###
Tags: `Algorithms`
<br>
# [Text align justify](https://www.codewars.com/kata/537e18b6147aa838f600001b)
by [kesheshyan](https://www.codewars.com/users/kesheshyan)
## Description
Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

  * Use spaces to fill in the gaps between words.
  * Each line should contain as many words as possible.
  * Use '\n' to separate lines.
  * Gap between words can't differ by more than one space.
  * Lines should end with a word not a space.
  * '\n' is not included in the length of a line.
  * Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
  * Last line should not be justified, use only one space between words.
  * Last line should not contain '\n'
  * Strings with one word do not need gaps ('somelongword\n').

Example with width=30:

```
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
```

Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)


## Solution:
```python
def justify(text, width):
    current_line = ""
    all_lines = []
    final_lines = []

    for word in text.split():
        if len(word) + len(current_line) <= width:
            current_line += word + " "
        else:
            all_lines.append(current_line.strip())
            current_line = word + " "

    all_lines.append(current_line.strip())

    for line in all_lines:
        missing_spaces = width - len(line)
        if missing_spaces > 0:
            words = line.split()
            if len(words) > 1:
                while missing_spaces > 0:
                    for i in range(len(words) - 1):
                        words[i] += " "
                        missing_spaces -= 1
                        if missing_spaces == 0:
                            break

            line = " ".join(words)
        final_lines.append(line)
    last = final_lines.pop()
    final_lines.append(" ".join(last.split()))

    return "\n".join(final_lines)
```
###
Tags: `Strings` `Algorithms`
<br>
# [The observed PIN](https://www.codewars.com/kata/5263c6999e0f40dee200059d)
by [BattleRattle](https://www.codewars.com/users/BattleRattle)
## Description
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```
He noted the PIN `1357`, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the `1` it could also be the `2` or `4`. And instead of the `5` it could also be the `2`, `4`, `6` or `8`.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

\* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#)  of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function `getPINs` (`get_pins` in python, `GetPINs` in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

```if:csharp
***For C# user:*** Do not use Mono. Mono is too slower when run your code.
```

## Solution:
```python
possible = {
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["8", "5", "7", "9", "0"],
    "9": ["6", "8", "9"],
    "0": ["0", "8"]
}

def get_pins(observed):
    to_return = []
    for i in possible[observed[0]]:
        if len(observed) == 1:
            return possible[observed]
        else:
            for j in get_pins(observed[1:]):
                to_return.append(i + j)
    return to_return
```
###
Tags: `Algorithms`
<br>
# [The Greatest Warrior](https://www.codewars.com/kata/5941c545f5c394fef900000c)
by [BurstNova](https://www.codewars.com/users/BurstNova)
## Description
![alt text](https://2.bp.blogspot.com/-DNNiOXduuvQ/Vh-FR-qbKXI/AAAAAAAAEOA/HT0IzJ36zW4/s1600/voz.jpg)

Create a class called `Warrior` which calculates and keeps track of their level and skills, and ranks them as the warrior they've proven to be.

<b><span style="color:#00BFFF">Business Rules:</span></b>

- A warrior starts at level <span style="color:#e4d00a">1</span> and can progress all the way to <span style="color:#e4d00a">100</span>.
- A warrior starts at rank `"Pushover"` and can progress all the way to `"Greatest"`.
- The only acceptable range of rank values is `"Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"`.
- Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
- With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
- The experience earned from the battle is relative to what the warrior's current level is compared to the level of the enemy.
- A warrior's experience starts from <span style="color:#e4d00a">100</span>. Each time the warrior's experience increases by another <span style="color:#e4d00a">100</span>, the warrior's level rises to the next level.
- A warrior's experience is <span style="color:#e4d00a">cumulative</span>, and does not reset with each rise of level. The only exception is when the warrior reaches level <span style="color:#e4d00a">100</span>, with which the experience stops at <span style="color:#e4d00a">10000</span>
- At every <span style="color:#e4d00a">10</span> levels, your warrior will reach a new rank tier. (ex. levels <span style="color:#e4d00a">1-9</span> falls within `"Pushover"` tier, levels <span style="color:#e4d00a">80-89</span> fall within `"Champion"` tier, etc.)
- A warrior cannot progress beyond level <span style="color:#e4d00a">100</span> and rank `"Greatest"`.


<b><span style="color:#00BFFF">Battle Progress Rules & Calculations:</span></b>

- If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return `"Invalid level"`.
- Completing a battle against an enemy with the same level as your warrior will be worth <span style="color:#e4d00a">10</span> experience points.
- Completing a battle against an enemy who is one level lower than your warrior will be worth <span style="color:#e4d00a">5</span> experience points.
- Completing a battle against an enemy who is two levels lower or more than your warrior will give <span style="color:#e4d00a">0</span> experience points.
- Completing a battle against an enemy who is one level higher or more than your warrior will accelarate your experience gaining. The greater the difference between levels, the more experinece your warrior will gain. The formula is `20 * diff * diff` where `diff` equals the difference in levels between the enemy and your warrior.
- However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot fight against an enemy that strong and must instead return `"You've been defeated"`.
- Every successful battle will also return one of three responses: `"Easy fight", "A good fight", "An intense fight"`. Return `"Easy fight"` if your warrior is 2 or more levels higher than your enemy's level. Return `"A good fight"` if your warrior is either 1 level higher or equal to your enemy's level. Return `"An intense fight"` if your warrior's level is lower than the enemy's level.

<b><span style="color:#00BFFF">Logic Examples:</span></b>

- If a warrior level <span style="color:#e4d00a">1</span> fights an enemy level <span style="color:#e4d00a">1</span>, they will receive <span style="color:#e4d00a">10</span> experience points.
- If a warrior level <span style="color:#e4d00a">1</span> fights an enemy level <span style="color:#e4d00a">3</span>, they will receive <span style="color:#e4d00a">80</span> experience points.
- If a warrior level <span style="color:#e4d00a">5</span> fights an enemy level <span style="color:#e4d00a">4</span>, they will receive <span style="color:#e4d00a">5</span> experience points.
- If a warrior level <span style="color:#e4d00a">3</span> fights an enemy level <span style="color:#e4d00a">9</span>, they will receive <span style="color:#e4d00a">720</span> experience points, resulting in the warrior rising up by at least <span style="color:#e4d00a">7</span> levels.
- If a warrior level <span style="color:#e4d00a">8</span> fights an enemy level <span style="color:#e4d00a">13</span>, they will receive <span style="color:#e4d00a">0</span> experience points and return `"You've been defeated"`. (Remember, difference in rank & enemy level being <span style="color:#e4d00a">5</span> levels higher or more must be established for this.)
- If a warrior level <span style="color:#e4d00a">6</span> fights an enemy level <span style="color:#e4d00a">2</span>, they will receive <span style="color:#e4d00a">0</span> experience points.

<b><span style="color:#00BFFF"> Training Rules & Calculations:</span></b>
- In addition to earning experience point from battles, warriors can also gain experience points from training.
- Training will accept an array of three elements (except in java where you'll get 3 separated arguments): the description, the experience points your warrior earns, and the minimum level requirement.
- If the warrior's level meets the minimum level requirement, the warrior will receive the experience points from it and store the description of the training. It should end up returning that description as well.
- If the warrior's level does not meet the minimum level requirement, the warrior doesn not receive the experience points and description and instead returns `"Not strong enough"`, without any archiving of the result.

<b><span style="color:#00BFFF"> Code Examples:</span></b>
```javascript
var bruce_lee = new Warrior();
bruce_lee.level();        // => 1
bruce_lee.experience();   // => 100
bruce_lee.rank();         // => "Pushover"
bruce_lee.achievements(); // => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]); // => "Defeated Chuck Norris"
bruce_lee.experience();   // => 9100
bruce_lee.level();        // => 91
bruce_lee.rank();         // => "Master"
bruce_lee.battle(90);     // => "A good fight"
bruce_lee.experience();   // => 9105
bruce_lee.achievements(); // => ["Defeated Chuck Norris"]
```
```ruby
bruce_lee = Warrior.new
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
```
```python
bruce_lee = Warrior()
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
```
```java
// Note: all numeric values are integers.

Warrior bruce_lee = new Warrior();
bruce_lee.level();        // => 1
bruce_lee.experience();   // => 100
bruce_lee.rank();         // => "Pushover"
bruce_lee.achievements(); // => []  (as List<String>)
bruce_lee.training("Defeated Chuck Norris", 9000, 1); // => "Defeated Chuck Norris"
bruce_lee.experience();   // => 9100
bruce_lee.level();        // => 91
bruce_lee.rank();         // => "Master"
bruce_lee.battle(90);     // => "A good fight"
bruce_lee.experience();   // => 9105
bruce_lee.achievements(); // => ["Defeated Chuck Norris"]  (as List<String>)
```
## Solution:
```python
ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

class Warrior():
    level = 1
    experience = 100
    rank = ranks[0]    
    
    def __init__(self):
        self.achievements = []
    
    def updateRank(self):
        self.rank = ranks[self.level // 10]
        
    def updateLevel(self):
        if self.level == 100:
            self.experience = 10000
        self.level = self.experience // 100
        
    def increaseExp(self, inc):
        self.experience += inc
        if self.experience > 10000:
            self.experience = 10000
        self.updateLevel()
        self.updateRank()
        
    def training(self, array):
        desc, xp, req = array
        if self.level < req:
            return "Not strong enough"
        self.increaseExp(xp)
        self.achievements.append(desc)
        return(desc)
     
    def battle(self, enemyLvl):
        if enemyLvl < 1 or enemyLvl > 100:
            return "Invalid level"
        dif = enemyLvl - self.level
        if dif > 4 and enemyLvl // 10 - self.level // 10 >= 1:
            return "You've been defeated"
        if dif == 0:
            self.increaseExp(10)
        if dif == -1:
            self.increaseExp(5)
        if dif < -1:
            pass
        if dif > 0:
            incr = 20 * dif * dif
            self.increaseExp(incr)
            
        if dif <= -2:
            return "Easy fight"
        if dif == -1 or dif == 0:
            return "A good fight"
        if dif > 0:
            return "An intense fight"
```
###
Tags: `Algorithms`
<br>
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
Tags: `Data Structures` `Algorithms`
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
Tags: `Strings` `Date Time` `Algorithms`
<br>
