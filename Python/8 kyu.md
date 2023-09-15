# [Are You Playing Banjo?](https://www.codewars.com/kata/53af2b8861023f1d88000832)
by [MRodalgaard](https://www.codewars.com/users/MRodalgaard)
## Description
Create a function which answers the question "Are you playing banjo?".  
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
```
name + " plays banjo" 
name + " does not play banjo"
```
Names given are always valid strings.
## Solution:
```python
def are_you_playing_banjo(name):
    # Implement me!
    if name[0] in ["r", "R"]:
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
```
###
Tags: `Strings` `Fundamentals`
<br>
# [Convert boolean values to strings 'Yes' or 'No'.](https://www.codewars.com/kata/53369039d7ab3ac506000467)
by [weavermedia](https://www.codewars.com/users/weavermedia)
## Description
Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

## Solution:
```python
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'
```
###
Tags: `Fundamentals`
<br>
# [Remove String Spaces](https://www.codewars.com/kata/57eae20f5500ad98e50002c5)
by [PG1](https://www.codewars.com/users/PG1)
## Description
Write a function that removes the spaces from the string, then return the resultant string.

Examples:
```
Input -> Output
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"
```

~~~if:bf
The input string will be terminated with a null character `\0`.
~~~
~~~if:c,nasm
For C and Nasm, you must return a new dynamically allocated string.
~~~

## Solution:
```python
def no_space(x):
    return x.replace(" ", "")
```
###
Tags: `Fundamentals` `Strings`
<br>
# [Opposite number](https://www.codewars.com/kata/56dec885c54a926dcd001095)
by [sergioet](https://www.codewars.com/users/sergioet)
## Description
Very simple, given an integer or a floating-point number, find its opposite.

Examples:
```
1: -1
14: -14
-34: 34
```

~~~if:sql
You will be given a table: `opposite`, with a column: `number`. Return a table with a column: `res`.
~~~

## Solution:
```python
def opposite(number):
    return -number
```
###
Tags: `Fundamentals`
<br>
# [Opposites Attract](https://www.codewars.com/kata/555086d53eac039a2a000083)
by [jbarget](https://www.codewars.com/users/jbarget)
## Description
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love. 

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
## Solution:
```python
def lovefunc( flower1, flower2 ):
    return flower1 % 2 != flower2 % 2
```
###
Tags: `Fundamentals`
<br>
# [Convert a String to a Number!](https://www.codewars.com/kata/544675c6f971f7399a000e79)
by [bkaes](https://www.codewars.com/users/bkaes)
## Description
Note: This kata is inspired by [Convert a Number to a String!](http://www.codewars.com/kata/convert-a-number-to-a-string/). Try that one too.

## Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

## Examples
```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```


## Solution:
```python
def string_to_number(s):
    return int(s)
```
###
Tags: `Parsing` `Strings` `Fundamentals`
<br>
# [String repeat](https://www.codewars.com/kata/57a0e5c372292dd76d000d7e)
by [wichu](https://www.codewars.com/users/wichu)
## Description
~~~if:bf
Write a program which accepts a single byte `n` and then a sequence of bytes `string` and outputs the `string` exactly `n` times.

The first input byte will be `n`. Following bytes will be characters of `string`. The end of the input `string` will be indicated with a null byte `\0`.

### Examples:

"\6I" -> "IIIIII"
"\5Hello" -> "HelloHelloHelloHelloHello"
~~~

Write a function that accepts an integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

### Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

## Solution:
```python
def repeat_str(repeat, string):
    return string * repeat
```
###
Tags: `Fundamentals` `Strings`
<br>
# [Counting sheep...](https://www.codewars.com/kata/54edbc7200b811e956000556)
by [tfKamran](https://www.codewars.com/users/tfKamran)
## Description
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

```javascript
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```crystal
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```python
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```
```csharp
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```c
{ true,  true,  true,  false,
  true,  true,  true,  true,
  true,  false, true,  false,
  true,  false, false, true,
  true,  true,  true,  true,
  false, false, true,  true }
```
```cpp
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```haskell
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```
```elixir
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```rust
&[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
```scala
Array(
  true,  true,  true,  false,
  true,  true,  true,  true,
  true,  false, true,  false,
  true,  false, false, true,
  true,  true,  true,  true,
  false, false, true,  true
)
```
```racket
;for racket in this kata, 
;only values that are exactly #t count as sheep. 
;any other value is not a sheep.
(count-sheeps '(#t #t #t #f #t #t 1
                #t #f #f #f #f #f #f
                #t #f #t #t #t #t #t
                #t #t #f #t #t #t 5))
```
```factor
{ t t t f
  t t t t
  t f t f
  t f f t
  t t t t
  f f t t }
```
```bf
"tttftttttftftfftttttfftt"
```


The correct answer would be `17`.

Hint: Don't forget to check for bad values like `null`/`undefined`

```if:bf
In BF, true is represented as the letter 't' (ASCII 116), while false is represented as the letter 'f' (ASCII 102) 

Input streams will be terminated with a null character
```

## Solution:
```python
def count_sheeps(sheep):
    i = 0
    for x in sheep:
        if x:
            i += 1
    return i
```
###
Tags: `Arrays` `Fundamentals`
<br>
# [Is n divisible by x and y?](https://www.codewars.com/kata/5545f109004975ea66000086)
by [naaz](https://www.codewars.com/users/naaz)
## Description
Create a function that checks if a number `n` is divisible by two numbers `x` **AND** `y`. All inputs are positive, non-zero numbers.

```text
Examples:
1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5
```

## Solution:
```python
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False
```
###
Tags: `Refactoring`
<br>
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
Tags: `Debugging` `Fundamentals`
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
Tags: `Regular Expressions` `Fundamentals` `Strings`
<br>
