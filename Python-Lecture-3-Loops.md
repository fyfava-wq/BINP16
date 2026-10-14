# BINP16 Python — Lecture 3 Cheat Sheet
## Program Control and Logic

> Based on Lecture 3: *Program control and logic* (BINP16 Bioinformatics: Programming in Python, Lund University, October 2026).

---

## 1. Learning objectives

The lecture covers:

1. Controlling command execution with code blocks
2. Conditional execution
   - logical operations
   - `if`, `elif`, `else`
   - comparisons and truth
3. Loops
   - `for`
   - `while`
   - `break`, `continue`, `pass`
   - loop `else`
   - `enumerate()`
4. Error exceptions
   - `raise`
   - `try`
   - `except`
   - `finally`
5. Calling modules

---

# 2. Code blocks and indentation

Python uses **indentation** to define code blocks.

```python
if condition:
    print("This belongs to the if block")
```

Whitespace is significant: changing indentation can change the meaning of the program.

```python
for i in range(3):
    print(i)

print("Done")
```

Here `"Done"` runs once, after the loop.

```python
for i in range(3):
    print(i)
    print("Done")
```

Here `"Done"` runs during every iteration.

**Key rule:** always check which block a line is indented inside.

---

# 3. Comparison operators

Comparisons produce a truth value.

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal to | `a == b` |
| `!=` | not equal to | `a != b` |
| `<` | less than | `a < b` |
| `<=` | less than or equal | `a <= b` |
| `>` | greater than | `a > b` |
| `>=` | greater than or equal | `a >= b` |

### `=` vs `==`

```python
x = 5
```

`=` means **assignment**.

```python
x == 5
```

`==` means **comparison**.

---

# 4. Logical operators

Python has three logical operators:

```python
and
or
not
```

## `and`

Both operands/conditions must be true.

```python
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

Example:

```python
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

## `or`

At least one operand/condition must be true.

```python
True or True     # True
True or False    # True
False or True    # True
False or False   # False
```

## `not`

Reverses the truth value.

```python
not True     # False
not False    # True
```

---

# 5. Truth values

The lecture highlights these falsy values:

```python
None
False
0
0.0
""
()
[]
{}
set(())
```

Examples:

```python
bool(1)       # True
bool(0)       # False
bool("hello") # True
bool("")      # False
bool([1, 2])  # True
bool([])      # False
```

Mental model:

```text
zero / empty / False / None → falsy
non-zero / non-empty        → truthy
```

---

# 6. `and` / `or` can return values

Logical operations do not always return `True` or `False`.

For `x and y`:

```text
if x is truthy → result is y
if x is falsy  → result is x
```

Examples from the lecture:

```python
True and False   # False
True and True    # True
0 and 3          # 0
1 and 2          # 2
5 and 0          # 0
True and 5       # 5
False and 99     # False
99 and False     # False
99 and 99        # 99
```

### Why?

Python uses short-circuit evaluation.

```python
0 and 3
```

Since `0` is falsy, Python already knows the `and` expression must be falsy and returns `0`.

```python
1 and 2
```

Since `1` is truthy, Python evaluates the second operand and returns `2`.

**Do not treat `and` as addition.**

```python
3 and 5   # 5
3 + 5     # 8
```

---

# 7. `if`

Basic form:

```python
if expression:
    statements
```

The block runs only if the expression is true.

```python
a = 1

if a:
    print("a is true!")
```

Another example:

```python
b = 0

if not b:
    print("b is false!")
```

---

# 8. `if` / `elif` / `else`

General structure:

```python
if condition1:
    statements
elif condition2:
    statements
else:
    statements
```

Example:

```python
x = 7

if x > 10:
    print("greater than 10")
elif x > 5:
    print("greater than 5")
else:
    print("5 or less")
```

Python checks from top to bottom. Once a matching branch runs, the remaining branches are skipped.

---

# 9. Nested `if`

An `if` can contain another `if`.

```python
a = 1
b = 0
c = 2

if a > b:
    if a > c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b > c:
    print("b is greatest")
else:
    print("c is greatest")
```

Indentation determines which block each `else` belongs to.

---

# 10. `==` vs `is`

This is important for Python objects.

### `==`

Compares **contents/values**:

```python
x = [123, 43, 56, 32]
y = [123, 43, 56, 32]

x == y
# True
```

### `is`

Compares **identity** — whether two names refer to the same object:

```python
x = [123, 43, 56, 32]
y = x

x is y
# True
```

The lecture's key distinction:

```text
==  → same contents/value
is  → same object/identity
```

---

# 11. Copying with `[:]`

The lecture uses:

```python
x = [123, 43, 56, 32]
y = x[:]
```

Then:

```python
y == x
# True

y is x
# False
```

`x[:]` creates a new list with the same contents.

Mental model:

```text
y = x       → same object
y = x[:]    → new object, same contents
```

---

# 12. Why loops?

Loops avoid repeating the same code manually.

Without a loop:

```python
print(1)
print(1)
print(1)
print(1)
print(1)
```

A loop can repeat work:

```python
for index in range(1, 6):
    print(index)
```

Mental model:

```text
for   → iterate over values
while → repeat while a condition is true
```

---

# 13. `for` loop

General form:

```python
for variable in values:
    statements
```

The variable is assigned each item in `values`.

```python
values = [10, -3, 8, 10, 100]

for v in values:
    print(v)
```

A string is iterable too:

```python
for letter in "aeiou":
    print("vowel:", letter)
```

---

# 14. `for` with `range()`

```python
for i in range(0, 3):
    print(i)
```

Output:

```text
0
1
2
```

`range(start, stop)` includes `start` but excludes `stop`.

So:

```python
range(0, 3)
```

means:

```text
0, 1, 2
```

---

# 15. Nested `for` loops

A loop can contain another loop:

```python
for letter in ['a', 'b', 'c']:
    print(letter)

    for i in range(0, 3):
        print(i)
```

The inner loop runs completely for each outer-loop item.

### Lecture warning

Do not use the same index variable in nested loops.

Avoid:

```python
for i in outer:
    for i in inner:
        ...
```

Prefer:

```python
for letter in outer:
    for i in inner:
        ...
```

---

# 16. `while` loop

A `while` loop repeats as long as its condition is true.

```python
while expression:
    statements
```

Example:

```python
i = 1

while i < 4:
    print(i)
    i = i + 1
```

Output:

```text
1
2
3
```

Something must eventually make the condition false.

---

# 17. `while` with multiple conditions

A `while` condition can contain logical operators:

```python
flag = True

while flag and i < 8:
    print(flag, i)
    i = i + 1
```

The loop continues while the whole expression is true.

---

# 18. `while` through a list

Lecture example:

```python
fruits = ["banana", "apple", "orange", "kiwi"]
position = 0

while position < len(fruits):
    print(position + 1, fruits[position])
    position = position + 1
```

Output:

```text
1 banana
2 apple
3 orange
4 kiwi
```

---

# 19. `for` vs `while`

### `for`

Use when iterating over a collection or range:

```python
for item in my_list:
    print(item)
```

### `while`

Use when repetition depends on a condition:

```python
while condition:
    do_something()
```

Simple mental model:

```text
for   → "for each..."
while → "while..."
```

---

# 20. `else` with loops

Python allows `else` after both `for` and `while`.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed.")
```

The loop `else` runs only if the loop finishes normally.

---

# 21. Loop `else` + `break`

Important rule:

> Loop `else` runs only when the loop completes without `break`.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 3:
        break
else:
    print("Loop completed.")
```

Output:

```text
1
2
3
```

`"Loop completed."` is not printed because `break` interrupted the loop.

Mental model:

```text
loop finishes naturally
        ↓
      else

loop hits break
        ↓
    skip else
```

---

# 22. `break`

`break` terminates the **current loop** immediately.

```python
for num in range(1, 11):
    if num == 5:
        break
    print(num)
```

Output:

```text
1
2
3
4
```

### Nested loops

A `break` inside an inner loop exits the **inner loop**, not the outer loop.

---

# 23. `continue`

`continue` skips the rest of the current iteration and starts the next iteration.

```python
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
```

Output:

```text
1
3
5
7
9
```

### `break` vs `continue`

```text
break
→ stop the current loop

continue
→ skip this iteration
→ go to the next iteration
```

---

# 24. `pass`

`pass` means **do nothing**.

It is useful when Python requires a statement syntactically but you do not want to execute anything yet.

```python
if condition:
    pass
```

It is different from `continue`:

```text
pass     → do nothing
continue → skip to next loop iteration
```

---

# 25. Loop control summary

| Statement | Effect |
|---|---|
| `break` | Stop the current loop |
| `continue` | Skip current iteration |
| `pass` | Do nothing |
| `else` | Run if the loop finishes without `break` |

---

# 26. `enumerate()`

`enumerate()` gives both:

- the index
- the corresponding item

Instead of:

```python
i = 0

for item in my_list:
    print(i, item)
    i += 1
```

you can write:

```python
for i, item in enumerate(my_list):
    print(i, item)
```

Use it when you need both the position and the value.

---

# 27. Loop warnings

The lecture gives three important warnings.

### 1. Do not modify the loop index from inside the loop

Avoid unexpectedly changing the variable controlling the loop.

### 2. Do not alter the number of items in a list while looping over it

If you need to modify the list, duplicate it and modify the duplicate.

### 3. Watch for infinite loops

Example:

```python
var = 1

while var == 1:
    print("You are stuck here forever")
```

The condition never becomes false.

---

# 28. Infinite `while` loops

Common mistake:

```python
i = 1

while i < 10:
    print(i)
```

`i` never changes, so `i < 10` stays true.

Correct:

```python
i = 1

while i < 10:
    print(i)
    i += 1
```

---

# 29. Indentation changes program flow

Compare:

```python
for i in range(10):
    if i > 5:
        print(i, "I am happy")
    else:
        print(i, "Not so great")

print("End of the test")
```

`"End of the test"` runs once.

Now:

```python
for i in range(10):
    if i > 5:
        print(i, "I am happy")
    else:
        print(i, "Not so great")
    print("End of the test")
```

`"End of the test"` runs once per iteration.

**Indentation is part of the program logic.**

---

# 30. Exercise: first 100 prime numbers

The lecture asks for a program that prints the first 100 prime numbers.

The lecture describes a prime as a number that does not divide evenly by another number.

If a number is not prime, print two of its factors.

Example:

```text
6 → 2, 3
```

The exercise specifically says not to google the answer.

This exercise combines:

- loops
- `%`
- conditions
- variables
- `break` / loop control

---

# 31. Catching errors

The goal of error handling is to predict which errors may occur and write code that can deal with them.

The lecture distinguishes:

```text
preventing an error
vs.
catching an error
```

"Catching" means programming your code to handle the problem in real time or provide a useful error message.

---

# 32. Exceptions

Python raises an exception when an illegal operation occurs.

Example:

```python
1 / 0
```

produces:

```text
ZeroDivisionError
```

Python has built-in exception types for many errors.

---

# 33. `raise`

You can deliberately raise an exception when your program detects an invalid situation.

Lecture example:

```python
num_of_children = -1

if num_of_children < 0:
    raise Exception("Number of children cannot be negative")
```

Why?

Python can execute:

```python
num_of_children = -1
```

without a syntax error, but your program can decide that the value is logically invalid.

### Mental model

```text
raise → deliberately signal an error
```

---

# 34. `try` / `except`

Basic structure:

```python
try:
    risky_code()
except SomeError:
    handle_error()
```

Lecture example:

```python
while True:
    try:
        x = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Oops! That was not a valid integer. Try again...")
```

### What happens?

1. Execute the `try` block.
2. If no exception occurs, skip `except`.
3. If a matching exception occurs, execute `except`.
4. Continue after the `try` statement.
5. If an exception does not match the named exception, it can be passed to an outer handler; if none handles it, execution stops.

---

# 35. Example: invalid input

Without handling:

```python
x = int(input("Enter an integer: "))
```

Entering:

```text
hello
```

causes a `ValueError`.

With handling:

```python
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer.")
```

---

# 36. Catch the specific exception

Catch the exception you expect.

```python
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer.")
```

Here `ValueError` is the expected problem when converting invalid text to an integer.

---

# 37. `finally`

`finally` contains code that runs whether or not an exception occurs.

```python
try:
    risky_code()
except SomeError:
    handle_error()
finally:
    cleanup()
```

Lecture example:

```python
input_num1 = int(input("Please enter the first number: "))
input_num2 = int(input("Please enter the second number: "))

try:
    x = input_num1 / input_num2
except ZeroDivisionError:
    print("Error: Divided by zero")
finally:
    print("You finished this exercise")
```

The `finally` block runs regardless of whether the division succeeds or raises `ZeroDivisionError`.

---

# 38. Exception-handling summary

| Part | Purpose |
|---|---|
| `try` | Code that might raise an exception |
| `except` | Handle a matching exception |
| `finally` | Run code regardless of exception |
| `raise` | Trigger an exception yourself |

---

# 39. Exiting a program

The lecture presents two ways to force program termination.

## `sys.exit()`

```python
import sys

sys.exit()
```

The lecture notes that this raises a `SystemExit` exception, which can be intercepted using `try`/`except`.

Example:

```python
import sys

while True:
    print("Exiting before getting stuck in loop")
    sys.exit()

print("This never gets printed")
```

## `os._exit()`

```python
import os

os._exit(0)
```

The lecture describes this as an unconditional exit.

### Mental model

```text
sys.exit()  → exit using SystemExit
os._exit()  → unconditional exit
```

---

# 40. `raise` vs `sys.exit()`

They have different purposes.

```python
raise Exception("Something is wrong")
```

means:

> Signal an error/exception.

Whereas:

```python
import sys
sys.exit()
```

means:

> Stop the program.

---

# 41. Fibonacci exercise

The lecture gives:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

Each new term is generated by adding the previous two terms.

The exercise asks:

> Considering Fibonacci terms whose values do not exceed 1000, find the sum of the even-valued terms.

This combines:

- variables
- arithmetic
- loops
- conditions
- `%`
- an accumulating sum

Useful pattern:

```python
total = 0

# when a value should be included:
total += value
```

---

# 42. Useful loop patterns

## Count

```python
count = 0

for item in my_list:
    if condition:
        count += 1
```

## Sum

```python
total = 0

for value in values:
    total += value
```

## Search until found

```python
for item in values:
    if item == target:
        break
```

## Skip unwanted values

```python
for value in values:
    if condition:
        continue
    print(value)
```

## Repeat until a condition changes

```python
while condition:
    do_something()
    update_condition()
```

---

# 43. Common mistakes

### `=` vs `==`

Wrong:

```python
if x = 5:
```

Correct:

```python
if x == 5:
```

### Missing `:`

Wrong:

```python
if x > 5
```

Correct:

```python
if x > 5:
```

### Wrong indentation

Wrong:

```python
if x > 5:
print(x)
```

Correct:

```python
if x > 5:
    print(x)
```

### Infinite loop

Wrong:

```python
i = 0

while i < 10:
    print(i)
```

Correct:

```python
i = 0

while i < 10:
    print(i)
    i += 1
```

### Confusing `break` and `continue`

```text
break     → leave the loop
continue  → go to the next iteration
```

### Expecting loop `else` after `break`

```python
for x in values:
    if condition:
        break
else:
    print("Done")
```

If `break` happens, `"Done"` does not run.

### Modifying a list while iterating

The lecture warns against changing the number of list items while looping over it.

---

# 44. High-yield table

| Concept | Meaning |
|---|---|
| `=` | Assignment |
| `==` | Same value/content |
| `is` | Same object/identity |
| `!=` | Not equal |
| `and` | Logical AND / short-circuit |
| `or` | Logical OR |
| `not` | Reverse truth value |
| `if` | Conditional execution |
| `elif` | Additional condition |
| `else` | Alternative branch |
| `for` | Iterate over values |
| `while` | Repeat while condition is true |
| `break` | Stop current loop |
| `continue` | Skip current iteration |
| `pass` | Do nothing |
| loop `else` | Runs if loop finishes without `break` |
| `enumerate()` | Index + item |
| `raise` | Trigger an exception |
| `try` | Try potentially failing code |
| `except` | Handle an exception |
| `finally` | Always execute final/cleanup code |
| `sys.exit()` | Exit using `SystemExit` |
| `os._exit()` | Unconditional exit |

---

# 45. One-page mental model

```text
PROGRAM CONTROL
│
├── CONDITIONS
│   ├── comparisons
│   │   ├── ==
│   │   ├── !=
│   │   ├── <
│   │   ├── <=
│   │   ├── >
│   │   └── >=
│   │
│   ├── logical operators
│   │   ├── and
│   │   ├── or
│   │   └── not
│   │
│   └── if / elif / else
│
├── LOOPS
│   ├── for
│   └── while
│
├── LOOP CONTROL
│   ├── break
│   ├── continue
│   ├── pass
│   ├── else
│   └── enumerate()
│
└── ERRORS
    ├── raise
    ├── try
    ├── except
    ├── finally
    ├── sys.exit()
    └── os._exit()
```

---

# 46. Final checklist

- [ ] Explain why Python indentation matters
- [ ] Know `=` vs `==`
- [ ] Know `==` vs `is`
- [ ] Explain `and`, `or`, and `not`
- [ ] Recognize common falsy values
- [ ] Use `if`, `elif`, and `else`
- [ ] Understand nested `if`
- [ ] Use a `for` loop
- [ ] Use `range()`
- [ ] Understand nested loops
- [ ] Use a `while` loop
- [ ] Avoid infinite loops
- [ ] Use `break`
- [ ] Use `continue`
- [ ] Know what `pass` does
- [ ] Understand loop `else`
- [ ] Know why loop `else` is skipped after `break`
- [ ] Use `enumerate()`
- [ ] Avoid modifying a list while iterating
- [ ] Use `raise`
- [ ] Use `try` / `except`
- [ ] Use `finally`
- [ ] Understand `sys.exit()` and `os._exit()`
- [ ] Combine loops and conditions to solve programming problems

---

## Source

**Lecture 3 — Program control and logic**  
BINP16 Bioinformatics: Programming in Python  
Lund University, October 2026

The lecture recommends completing the **Program control and logic** questions in `PythonExercises.pdf` and then taking self-quiz #3.
