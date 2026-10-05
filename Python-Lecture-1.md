# BINP16 — Python Lecture 1 Cheat Sheet
## Simple Data Types, Variables, Arithmetic & Strings
**Lund University | BINP16 Bioinformatics: Programming in Python | October 2026**

## 1. Running Python

Interactive mode:
```bash
python
```

Python prompt:
```text
>>>
```

Exit:
```python
exit()
```

Run a script:
```bash
python script.py
```

Three ways to run Python code:
1. IDE/editor
2. Interactive mode (IPython/Python interpreter)
3. Command prompt/terminal

---

## 2. Documentation and comments

For this course, programs should start with a formatted documentation section containing:
- Title
- Description
- User-defined functions
- Modules used
- Procedure
- Input/output
- Usage
- Version (if relevant)
- Date
- Author

Shebang:
```python
#!/usr/bin/python3
```

Single-line comment:
```python
# This is a comment
```

Multi-line comment/documentation block:
```python
"""
Longer comment
or documentation block
"""
```

Code section marker:
```python
#%%
```

---

## 3. Data types

| Type | Example |
|---|---|
| `int` | `-1`, `0`, `42` |
| `float` | `-1.22`, `3.14` |
| `str` | `"ACGBA"`, `"Hello"` |
| `bool` | `True`, `False` |
| `None` | `None` |

Check a type:
```python
type(1)
type("GATCCT")
type(True)
type(-1.22)
type(0.00)
```

Remember:
```python
True       # Boolean
"True"     # string
```

---

## 4. Variables

A variable is a named container for data.

```python
my_DNA = "ATGCGTA"
gene_length = 467
pi_short = 3.14
alive = True
```

Assignment uses `=`:
```python
x = 5
```

Python is **dynamically typed**: you do not declare the variable type before using it.

```python
var = 42
var = "Hello"
```

Python is also **strongly typed**: incompatible types cannot simply be combined.

```python
2 + "four"     # TypeError
```

### Naming rules

- Start with a letter
- May contain letters, numbers and `_`
- Case-sensitive
- Use meaningful names
- Avoid `__` for variable names
- Do not use Python keywords

Examples of keywords:
```text
False None True and as assert break class continue
def del elif else except finally for from global if
import in is lambda not or pass raise return try while
with yield
```

---

## 5. Arithmetic

```python
2 + 2
6 - 3
9 * 3
8 / 3.0
6 ** 2
```

| Operator | Meaning |
|---|---|
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `**` | exponent/power |
| `%` | remainder/modulus |
| `//` | floor division |

Example:
```python
mass = 5
volume = 1.08
density = mass / volume
print(density)
```

### Assignment shortcuts

| Operator | Meaning |
|---|---|
| `=` | assign |
| `+=` | add and assign |
| `-=` | subtract and assign |
| `*=` | multiply and assign |
| `/=` | divide and assign |
| `%=` | modulus and assign |
| `**=` | exponent and assign |
| `//=` | floor-divide and assign |

Example:
```python
x = 5
x += 2
```

---

## 6. Importing modules

Use `import` to access functionality from a module.

```python
import math

math.sqrt(16)
math.log10(100)
```

The lecture also introduces `random`:

```python
import random

random.random()
random.randrange(1, 10)
random.choice("abcd")
random.shuffle(my_list)
```

---

## 7. Indexing — Python starts at 0

Python indexes sequences from **0**, not 1.

```text
 H   e   l   l   o
 0   1   2   3   4
```

Therefore:
```python
"Hello"[0]    # H
"Hello"[-1]   # o
```

Negative indexes count from the end.

---

## 8. Strings

Strings contain characters and use single or double quotes:

```python
mystring = "I'm a string"
mystring = 'Hello'
```

The course recommends using double quotes.

Strings are **immutable**: individual characters cannot be changed.

```python
mystring[0] = "X"    # Error
```

But you can create a new string:
```python
mystring = mystring + " too"
```

---

## 9. String slicing

General form:
```python
sequence[start:stop:step]
```

**The stop index is not included.**

```python
seq = "ABCDEFGHIJKLMNOP"

seq[0:3]      # ABC
seq[1:5]      # BCDE
seq[:5]       # ABCDE
seq[5:]       # FGHIJKLMNOP
seq[-1]       # P
seq[::2]      # ACEGIKMO
seq[0:5:2]    # ACE
seq[::-1]     # reverse
seq[::-2]     # every second character backwards
```

---

## 10. String membership and searching

```python
mystring = "I'm a DNA sequence"

"DNA" in mystring
# True

"RNA" in mystring
# False

"RNA" not in mystring
# True
```

### `index()` vs `find()`

```python
mystring.index("DNA")
mystring.find("DNA")
```

If the substring is absent:

```python
mystring.index("RNA")   # error
mystring.find("RNA")    # -1
```

---

## 11. Useful string methods

```python
line = " ACG CGA GCA ATA "

line.strip()      # remove whitespace at both ends
line.lstrip()     # remove left whitespace
line.rstrip()     # remove right whitespace
line.split()      # split into pieces
line.split("CGA") # split using specific text
```

Other useful methods:
```python
s.count("A")
s.lower()
s.upper()
s.capitalize()
s.replace("T", "U")
len(s)
```

---

## 12. Concatenating and joining strings

Concatenate with `+`:
```python
dna1 = "ACGT"
dna2 = "TGCA"

dna1 + dna2
```

Join a list of strings:
```python
seq = ["A", "C", "T", "G"]

"".join(seq)      # ACTG
"|".join(seq)     # A|C|T|G
```

`join()` puts the separator between **list elements**.

Convert another type to a string:
```python
"I have " + str(3) + " apples."
```

---

## 13. String formatting

The lecture introduces `%` formatting:

```python
x = 3
y = 5.5121212
z = "in my bag"

"I have %d apples and %.2f oranges %s." % (x, y, z)
```

Common formats:
```text
%d    integer
%.2f  float with 2 decimal places
%s    string
```

---

## 14. `print()`

```python
print("Hello")
print(variable)
print(2 + 2)
```

Print several values:
```python
first_name = "Charles"
last_name = "Darwin"
book = "On the Origin of Species"

print(first_name, last_name, "wrote the book:", book)
```

Useful examples:
```python
print(Book.count("i"))
print(first_name.upper())
```

Escape sequences:
```python
print("	Hello,
World!")
```

| Escape | Meaning |
|---|---|
| `
` | new line |
| `	` | tab |

Raw string:
```python
print(r"	World!
")
```

---

## 15. Bioinformatics string examples

```python
myDNA = "ACGTAGCTAGCTAGTGT"
yourDNA = "AAACCCGGGTTT"
```

Count G:
```python
myDNA.count("G")
```

Lowercase:
```python
myDNA.lower()
```

Combine sequences:
```python
myDNA + yourDNA
```

Print both:
```python
print("My DNA is: " + myDNA + " and your DNA is: " + yourDNA)
```

Length:
```python
len(myDNA)
```

Find first `GT`:
```python
myDNA.find("GT")
```

DNA → RNA:
```python
myRNA = myDNA.replace("T", "U")
```

---

## 16. Booleans

Boolean objects:
```python
True
False
```

Logical operations:
```python
not hungry
hungry and chocolate
hungry or chocolate
```

Example:
```python
hungry = True
chocolate = False

happiness = (not hungry) or (hungry and chocolate)
```

Comparisons and truth tests produce `True` or `False`.

---

## 17. `None`

`None` represents an undefined/no-value object.

```python
X = None
print(X)
```

Output:
```text
None
```

---

## 18. Converting data types

### Float → integer
```python
a = 1.4
int(a)       # 1
```

### Number → string
```python
str(1.4)
```

### String → float
```python
float("2.5")
```

### Decimal string → integer

This fails:
```python
int("2.5")
```

Use two steps:
```python
int(float("2.5"))     # 2
```

Invalid conversion:
```python
int("hus")            # error
```

---

## 19. Quick reference

### Types
```python
type(1)          # int
type(1.0)        # float
type("ABC")      # str
type(True)       # bool
type(None)       # NoneType
```

### Variables
```python
name = "Vaiva"
length = 467
pi = 3.14
alive = True
```

### Arithmetic
```text
+  -  *  /  **  %  //
```

### Conversion
```python
int(x)
float(x)
str(x)
```

### Strings
```python
s[0]
s[-1]
s[1:5]
s[:5]
s[5:]
s[::2]
s[::-1]
```

### String methods
```python
s.count("A")
s.find("DNA")
s.index("DNA")
s.strip()
s.lstrip()
s.rstrip()
s.split()
s.lower()
s.upper()
s.capitalize()
s.replace("T", "U")
len(s)
```

### Modules
```python
import math
math.sqrt(16)
math.log10(100)

import random
random.random()
random.randrange(1, 10)
random.choice("abcd")
random.shuffle(my_list)
```

---

## 20. Course coding principles

Your code is evaluated by:

- **Accuracy** — does it do what it should?
- **Robustness** — how easy is it to break?
- **Readability** — how easy is it to understand?
- **Simplicity** — how easy is it to maintain?

Use meaningful variable names and document your code.

---

## Key things to remember

1. Python indexes from **0**, not 1.
2. `=` assigns a value.
3. Strings are **immutable**.
4. `sequence[start:stop]` excludes `stop`.
5. Python is **dynamically typed** and **strongly typed**.
6. Use `type()` to inspect a value's type.
7. Use `import` to access module functionality.
8. Use `int()`, `float()`, and `str()` for explicit conversions.
9. `True`, `False`, and `None` are special Python objects.
10. Good code should be accurate, robust, readable, and simple.
