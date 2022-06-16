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

`p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)`

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
Tags: `Arrays` `Lists` `Data Structures` `Fundamentals`
<br>
# [Isograms](https://www.codewars.com/kata/54ba84be607a92aa900000f1)
by [chunjef](https://www.codewars.com/users/chunjef)
## Description
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**
```
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
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
