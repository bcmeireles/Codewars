# [Multiply](https://www.codewars.com/kata/50654ddff44f800200000004)
by [Unknown](https://www.codewars.com/users/Unknown)
## Description
This code does not execute properly. Try to figure out why.
## Solution:
```python
def multiply(a, b):
    return a * b
```
###
Tags: `Bugs`
<br>
# [String cleaning](https://www.codewars.com/kata/57e1e61ba396b3727c000251)
by [mkelty](https://www.codewars.com/users/mkelty)
## Description
Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.

### Examples (input -> output)

```
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'

```

Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters `~#$%^&!@*():;"'.,?` all intact.

## Solution:
```python
def string_clean(s):
    """
    Function will return the cleaned string
    """
    f = ""
    for _ in s:
        if _ not in "1234567890":
            f += _
            
    return f
```
###
Tags: `Fundamentals` `Regular Expressions` `Declarative Programming` `Advanced Language Features` `Programming Paradigms` `Strings`
<br>
