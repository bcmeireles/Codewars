# [Complementary DNA](https://www.codewars.com/kata/554e4a2f232cdd87d9000038)
by [JustyFY](https://www.codewars.com/users/JustyFY)
## Description
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (**input --> output**)
~~~if-not:haskell
```
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
```
~~~
```if-haskell
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
Tags: `Fundamentals` `Strings` `Data Types`
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
Tags: `Fundamentals` `Rules`
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
Tags: `Fundamentals` `Binary`
<br>
