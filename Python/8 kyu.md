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


The correct answer would be `17`.

Hint: Don't forget to check for bad values like `null`/`undefined`

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
Create a function that checks if a number `n` is divisible by two numbers `x` **AND** `y`. All inputs are positive, non-zero digits.

```JS
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
Tags: `Regular Expressions` `Fundamentals`
<br>
