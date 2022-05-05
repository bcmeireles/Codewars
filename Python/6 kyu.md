# [Highest Scoring Word](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272)
by [PG1](https://www.codewars.com/users/PG1)
## Description
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
## Solution:
```python
def high(x):
    word_list = x.split(" ")
    max_score = 0
    for i in range(len(word_list)):
        word_score = 0
        for letter in word_list[i]:
            word_score += (ord(letter) - 96)
        
        if word_score > max_score:
            max_score = word_score
            max_word = word_list[i]
    return max_word
```
###
Tags: `Fundamentals` `Strings` `Data Types` `Arrays` `Numbers`
<br>
# [Simple Fun #354: Lonely Frog III](https://www.codewars.com/kata/59c9e82ea25c8c05860001aa)
by [myjinxin2015](https://www.codewars.com/users/myjinxin2015)
## Description
# Task

You are a lonely frog. 

You live on a coordinate axis.

The meaning of your life is to jump and jump..

Two actions are allowed:

- `forward`: Move forward 1 unit.

- `double`: If you at `x` point, then you can move to `x*2` point. 

Now, here comes your new task. Your starting point is `x`, the target point is `y`.

You need to jump to the target point with `minimal steps`. Please tell me, what's the `minimal steps`?

`1 <= x <= 10`, `x < y <= 100000`

# Example

For `x = 1, y = 8`, the output should be `3`.
```
 step  from   to      action
  1:     1 --> 2     forward(or double)
  2:     2 --> 4       double
  3:     4 --> 8       double
```

For `x = 1, y = 17`, the output should be `5`.
```
 step  from    to      action
  1:     1  --> 2     forward(or double)
  2:     2  --> 4       double
  3:     4  --> 8       double
  4:     8  --> 16      double
  5:     16 --> 17     forward
```

For `x = 1, y = 15`, the output should be `6`.
```
 step  from    to      action
  1:     1  --> 2      forward(or double)
  2:     2  --> 3      forward
  3:     3  --> 6      double
  5:     6  --> 7      forward
  6:     7  --> 14     double
  7:     14 --> 15     forward
```

For `x = 3, y = 12`, the output should be `2`.
```
 step  from    to       action
  1:     3  --> 6       double
  2:     6  --> 12      double
```

For `x = 3, y = 16`, the output should be `3`.
```
 step  from    to       action
  1:     3  --> 4      forward
  2:     4  --> 8       double
  3:     8  --> 16      double
```
## Solution:
```python
def jump_to(x, y):
    moves = 0
    while x != y:
        if (y / 2 >= x) and (y % 2 == 0):
            y = y / 2
        else:
            y -= 1
        moves += 1
    return moves
```
###
Tags: `Algorithms` `Logic`
<br>
# [Break camelCase](https://www.codewars.com/kata/5208f99aee097e6552000148)
by [hakt](https://www.codewars.com/users/hakt)
## Description
Complete the solution so that the function will break up camel casing, using a space between words.

### Example 

```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```
## Solution:
```python
import string

def solution(s):
    final = ""
    for i in range(len(s)):
        if s[i].isupper():
            final += " " + s[i]
        else:
            final += s[i]
    return final
```
###
Tags: `Fundamentals` `Strings` `Data Types` `Formatting` `Algorithms` `Logic`
<br>
# [Find the unique number](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
by [isqua](https://www.codewars.com/users/isqua)
## Description
There is an array with some numbers. All numbers are equal except for one. Try to find it!

```javascript
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
```

```swift
findUniq([ 1, 1, 1, 2, 1, 1 ]) == 2
findUniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```ruby
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```java
Kata.findUniq(new double[]{ 1, 1, 1, 2, 1, 1 }); // => 2
Kata.findUniq(new double[]{ 0, 0, 0.55, 0, 0 }); // => 0.55
```

```haskell
getUnique [1, 1, 1, 2, 1, 1] -- Result is 2
getUnique [0, 0, 0.55, 0, 0] -- Result is 0.55
```

```fsharp
findUniq([ 1; 1; 1; 2; 1; 1 ]) = 2
findUniq([ 0; 0; 0.55; 0; 0 ]) = 0.55
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

1. Find the unique number (this kata)
2. [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

## Solution:
```python
def find_uniq(arr):
    first = arr[0]
    arr2 = [y for y in arr if y != arr[0]]
    if len(arr2) == 1:
        return arr2[0]
    else:
        arr = [y for y in arr2 if y != arr2[0]]
        if len(arr) == 1:
            return arr[0]
        else:
            return first
```
###
Tags: `Fundamentals` `Algorithms` `Logic` `Numbers` `Data Types` `Arrays`
<br>
# [Sum of Digits / Digital Root](https://www.codewars.com/kata/541c8630095125aba6000c00)
by [user578387](https://www.codewars.com/users/user578387)
## Description
[Digital root](https://en.wikipedia.org/wiki/Digital_root) is the _recursive sum of all the digits in a number._

Given `n`, take the sum of the digits of `n`. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

## Examples
```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

## Solution:
```python
def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        i = 0
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i])
        return digital_root(sum)
```
###
Tags: `Algorithms` `Mathematics` `Logic` `Numbers` `Arithmetic`
<br>
# [Who likes it?](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)
by [BattleRattle](https://www.codewars.com/users/BattleRattle)
## Description
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```


```if:c
* return must be an allocated string
* do not mutate input
```

Note: For 4 or more names, the number in `"and 2 others"` simply increases.

## Solution:
```python
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
```
###
Tags: `Fundamentals` `Formatting` `Algorithms` `Logic` `Strings` `Data Types`
<br>
# [Array.diff](https://www.codewars.com/kata/523f5d21c841566fde000009)
by [marcinbunsch](https://www.codewars.com/users/marcinbunsch)
## Description
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list `a`, which are present in list `b` keeping their order.

```c
array_diff({1, 2}, 2, {1}, 1, *z) == {2} (z == 1)
```
```javascript
arrayDiff([1,2],[1]) == [2]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```crystal
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2],[1]) == [2]
```
```coffeescript
arrayDiff([1,2],[1]) == [2]
```
```haskell
difference [1,2] [1] == [2]
```
```csharp
Kata.ArrayDiff(new int[] {1, 2}, new int[] {1}) => new int[] {2}
```
```fsharp
arrayDiff [|1|] [|1; 2|] = [|2|]
```
```rust
array_diff(vec![1,2], vec![1]) == vec![2]
```
```clojure
(= (array-diff [1 2] [1]) [2])
```
```groovy
Kata.arrayDiff([1,2],[1]) == [2]
```
```java
Kata.arrayDiff(new int[] {1, 2}, new int[] {1}) => new int[] {2}
```
```julia
arraydiff([1,2],[1]) == [2]
```
```nim
arrayDiff(@[1,2],@[1]) == @[2]
```
```php
arrayDiff([1,2],[1]) == [2]
```
```r
array_diff(c(1, 2), 1) == 2
```
```prolog
array_diff([1, 2], [1], [2]). % Result = [2]
```
```scala
arrayDiff(Seq(1, 2), Seq(1)) == Seq(2)
```
```cobol
      ArrayDiff([1, 2], [1]) = [2]
```

If a value is present in `b`, all of its occurrences must be removed from the other:

```c
array_diff({1, 2, 2, 2, 3}, 5, {2}, 1, *z) == {1, 3} (z == 2)
```
```javascript
arrayDiff([1,2,2,2,3],[2]) == [1,3]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2,2,2,3],[2]) == [1,3]
```
```coffeescript
arrayDiff([1,2,2,2,3],[2]) == [1,3]
```
```haskell
difference [1,2,2,2,3] [2] == [1,3]
```
```csharp
Kata.ArrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}) => new int[] {1, 3}
```
```fsharp
arrayDiff [|2|] [|1; 2; 2; 2; 3|] = [|1; 3|]
```
```rust
array_diff(vec![1,2,2,2,3], vec![2]) == vec![1,3]
```
```clojure
(= (array-diff [1,2,2,2,3] [2]) [1,3])
```
```groovy
Kata.arrayDiff([1,2,2,2,3],[2]) == [1,3]
```
```java
Kata.arrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}) => new int[] {1, 3}
```
```julia
arraydiff([1,2,2,2,3],[2]) == [1,3]
```
```nim
arrayDiff(@[1,2,2,2,3],@[2]) == @[1,3]
```
```php
arrayDiff([1,2,2,2,3],[2]) == [1,3]
```
```r
array_diff(c(1, 2, 2, 2, 3), 2) == c(1, 3)
```
```prolog
array_diff([1, 2, 2, 2, 3], [2], [1, 3]). % Result = [1, 3]
```
```scala
arrayDiff(Seq(1, 2, 2, 2, 2, 2, 3), Seq(2)) == Seq(1, 3)
```
```cobol
      ArrayDiff([1,2,2,2,3],[2]) = [1,3]
```
~~~ if:c
NOTE: In C, assign return array length to pointer *z
~~~
## Solution:
```python
def array_diff(a, b):
    c = []
    for i in range(len(a)):
        if not a[i] in b:
            c.append(a[i])
    return c
```
###
Tags: `Fundamentals` `Arrays` `Data Types`
<br>
# [Multiples of 3 or 5](https://www.codewars.com/kata/514b92a657cdc65150000006)
by [jhoffner](https://www.codewars.com/users/jhoffner)
## Description
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 **below** the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).

**Note:** If the number is a multiple of **both** 3 and 5, only count it *once*.
  
***Courtesy of projecteuler.net** ([Problem 1](https://projecteuler.net/problem=1))*

## Solution:
```python
def solution(number):
    sum = 0
    i = 0
    while i < number:
        if i % 15 == 0:
            sum += i
        elif ((i % 5)  == 0 )or ((i % 3) == 0):
            sum += i
        i += 1
    return sum
```
###
Tags: `Algorithms` `Mathematics` `Logic` `Numbers`
<br>
# [Create Phone Number](https://www.codewars.com/kata/525f50e3b73515a6db000b83)
by [xDranik](https://www.codewars.com/users/xDranik)
## Description
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

### Example

```javascript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```cpp
createPhoneNumber(int[10]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```crystal
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```ruby
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```coffeescript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```java
Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```dart
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```haskell
createPhoneNumber [1,2,3,4,5,6,7,8,9,0] -- => returns "(123) 456-7890"
```
```csharp
Kata.CreatePhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```fsharp
createPhoneNumber [1; 2; 3; 4; 5; 6; 7; 8; 9; 0] // => returns "(123) 456-7890"
```
```python
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```scala
Kata.createPhoneNumber(Seq(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)) # => returns "(123) 456-7890"
```
```php
createPhoneNumber([1,2,3,4,5,6,7,8,9,0]); // => returns "(123) 456-7890"
```
```f#
createPhoneNumber [1; 2; 3; 4; 5; 6; 7; 8; 9; 0] // => returns "(123) 456-7890"
```
```clojure
(create-phone-number [1 2 3 4 5 6 7 8 9 0]) ;; => returns "(123) 456-7890"
```
```rust
create_phone_number(&[1,2,3,4,5,6,7,8,9,0]); // returns "(123) 456-7890"
```
```go
CreatePhoneNumber([10]uint{1,2,3,4,5,6,7,8,9,0})  // returns "(123) 456-7890"
```
```c
create_phone_number(phnum, (const unsigned char[]){1,2,3,4,5,6,7,8,9,0});
    /* phnum <- "(123) 456-7890" */
```
```nasm
phnum:  resb 15
nums:   db  1,2,3,4,5,6,7,8,9,0

mov rdi, phnum
mov rsi, nums
call create_phone_number  ; RAX <- phnum <- "(123) 456-7890" 
```
```typescript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```julia
createphonenumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # -> returns "(123) 456-7890"
```
```cfml
createPhoneNumber( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ) // => returns "(123) 456-7890"
```
```factor
{ 1 2 3 4 5 6 7 8 9 0 } create-phone-number ! returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge.  
Don't forget the space after the closing parentheses!

## Solution:
```python
def create_phone_number(n):
    return f"""({''.join(map(str, n[:3]))}) {''.join(map(str, n[3:6]))}-{''.join(map(str, n[6:]))}"""
```
###
Tags: `Algorithms` `Arrays` `Data Types` `Strings` `Loops` `Control Flow` `Basic Language Features` `Fundamentals` `Formatting` `Logic` `Regular Expressions` `Declarative Programming` `Advanced Language Features` `Programming Paradigms`
<br>
