# [Square Every Digit](https://www.codewars.com/kata/546e2562b03326a88e000020)
by [MysteriousMagenta](https://www.codewars.com/users/MysteriousMagenta)
## Description
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 7<sup>2</sup> is 49, 6<sup>2</sup> is 36, and 5<sup>2</sup> is 25. (49-36-25)

**Note:** The function accepts an integer and returns an integer.

Happy Coding!

## Solution:
```python
def square_digits(num):
    base = ""
    for digit in str(num):
        base += str(int(digit)**2)
    return int(base)
```
###
Tags: `Mathematics` `Fundamentals`
<br>
# [String ends with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)
by [jhoffner](https://www.codewars.com/users/jhoffner)
## Description
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 

Examples:

```javascript
solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
```
```coffeescript
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```
```python
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```
```go
solution("abc", "bc") // returns true
solution("abc", "d") // returns false
```
```prolog
solution("abc", "bc"). % match
\+ solution("abc", "d"). % no match
```
```clojure
(solution "abc" "bc") ; returns true
(solution "abc" "d'" ; returns false
```
```lua
strEndsWith('abc', 'bc') -- returns true
strEndsWith('abc', 'd') -- returns false
```
```cobol
      StringEndsWith('abc', 'bc')
      *     -->      result = 1
      StringEndsWith('abc', 'd')
      *     -->      result = 0
```
```scala
solution("abc", "bc") // returns true
solution("abc", "d") //returns false
```
## Solution:
```python
def solution(text, ending):
    return text[-len(ending):] == ending
```
###
Tags: `Strings` `Fundamentals`
<br>
# [Is this a triangle?](https://www.codewars.com/kata/56606694ec01347ce800001b)
by [silentZaika](https://www.codewars.com/users/silentZaika)
## Description
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

## Solution:
```python
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
```
###
Tags: `Mathematics` `Fundamentals`
<br>
# [Growth of a Population](https://www.codewars.com/kata/563b662a59afc2b5120000c6)
by [g964](https://www.codewars.com/users/g964)
## Description
In a small town the population is `p0 = 1000` at the beginning of a year. The population
regularly increases by `2 percent` per year and moreover `50` new inhabitants per year come to live in the town. 
How many years does the town need to see its population
greater or equal to `p = 1200` inhabitants?

```
At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
```
More generally given parameters:

`p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)`

the function `nb_year` should return `n` number of entire years needed to get a population greater or equal to `p`.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

```
Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
```

#### Note: 
Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.


## Solution:
```python
def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        i += 1
        p0 += p0 * (percent / 100) + aug
        p0 = int(p0)
    return i
```
###
Tags: `Fundamentals`
<br>
# [Sum of odd numbers](https://www.codewars.com/kata/55fd2d567d94ac3bc9000064)
by [hhelwich](https://www.codewars.com/users/hhelwich)
## Description
Given the triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

Calculate the sum of the numbers in the n<sup>th</sup> row of this triangle (starting at index 1) e.g.: (**Input --> Output**)

```
1 -->  1
2 --> 3 + 5 = 8
```

## Solution:
```python
def row_sum_odd_numbers(n):
    return n**3
```
###
Tags: `Arrays` `Lists` `Mathematics` `Fundamentals`
<br>
# [Isograms](https://www.codewars.com/kata/54ba84be607a92aa900000f1)
by [chunjef](https://www.codewars.com/users/chunjef)
## Description
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**
```if-not:factor
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```

```if:factor
"Dermatoglyphics" -> t
"aba" -> f
"moOse" -> f (ignore letter case)
```
```fsharp
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
```

## Solution:
```python
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
```
###
Tags: `Strings` `Fundamentals`
<br>
# [Complementary DNA](https://www.codewars.com/kata/554e4a2f232cdd87d9000038)
by [JustyFY](https://www.codewars.com/users/JustyFY)
## Description
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (**input --> output**)
~~~if-not:haskell
```
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
```
~~~
```if:haskell
dnaStrand []        `shouldBe` []
dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]
```

## Solution:
```python
def DNA_strand(dna):
    final = ""
    for letter in dna:
        if letter == "A":
            final += "T"
        elif letter == "T":
            final += "A"
        elif letter == "C":
            final += "G"
        elif letter == "G":
            final += "C"
        else:
            final += letter
    return final
```
###
Tags: `Strings` `Fundamentals`
<br>
# [Categorize New Member](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa)
by [Brynx](https://www.codewars.com/users/Brynx)
## Description
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
## Input

Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

## Output
Output will consist of a list of string values (in Haskell and C: `Open` or `Senior`) stating whether the respective member is to be placed in the senior or open category.

### Example

```
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
```

## Solution:
```python
def open_or_senior(data):
    list = []
    for member in data:
        list.append("Senior") if (member[0] > 54 and member[1] > 7) else list.append("Open")
    return list
            
        
            
```
###
Tags: `Fundamentals`
<br>
# [Binary Addition](https://www.codewars.com/kata/551f37452ff852b7bd000139)
by [garrettguy457](https://www.codewars.com/users/garrettguy457)
## Description
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

**Examples:(Input1, Input2 --> Output (explanation)))**
```
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
```

## Solution:
```python
def add_binary(a,b):
    s = str(bin(a + b))
    return s[2:]
```
###
Tags: `Binary` `Fundamentals`
<br>
