# BINP16 — Python Lecture 2 Cheat Sheet
## Collection Data Types

**Lecture:** 2 — Collection Data Types  
**Course:** BINP16 Bioinformatics: Programming in Python  
**Topics:** lists, tuples, sets, dictionaries, sequence operations, sorting, `zip()`, and output formatting.

---

## 1. The four main collection types

| Type | Ordered? | Mutable? | Duplicates? | Syntax |
|---|---|---|---|---|
| **List** | Yes | Yes | Yes | `[]` |
| **Tuple** | Yes | No | Yes | `()` |
| **Set** | No | Yes | No | `{}` |
| **Dictionary** | Yes* | Yes | Keys unique | `{key: value}` |

*Dictionaries preserve insertion order in Python 3.7+.

**Mental model:**
- **List** → ordered collection you can change.
- **Tuple** → ordered collection you cannot change.
- **Set** → unordered collection of unique elements.
- **Dictionary** → key → value mapping.

Python starts counting indexes at **0**, not 1.

```python
x = ['a', 'b', 'c']
x[0]       # 'a'
x[1]       # 'b'
x[-1]      # 'c'
```

---

# 2. Lists

Lists are mutable collections. They can contain different types, repeated items, and other lists.

```python
mylist = [42, 'RNA', 'noncoding DNA', 5234656]
empty = []
```

### Access / change / test

```python
mylist[0] = 'DNA'       # change an item
'apple' in mylist       # membership
'apple' not in mylist
len(mylist)             # length
```

### Slicing

General form:

```python
list[start:stop:step]
```

`start` is included; `stop` is excluded.

```python
Bag = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

Bag[2:5]       # ['cherry', 'orange', 'kiwi']
Bag[0:5:2]     # ['apple', 'cherry', 'kiwi']
Bag[:4]        # first 4
Bag[1:]        # second item onward
Bag[-2]        # second from the end
Bag[:]         # whole list
```

## List modification

```python
x.append(a)        # add ONE item to end
x.extend(y)        # add contents of y
x.insert(i, a)     # insert a at index i
x.remove(a)        # remove first occurrence of value a
x.pop(i)           # remove + return item at index i
x.pop()            # remove + return last item
del x[i]            # delete item by index
del x[i:j]          # delete slice
x.clear()           # remove all items
x.reverse()         # reverse in place
x.sort()            # sort in place
```

### `append()` vs `extend()`

```python
s = ['mRNA', 'tRNA']
t = ['ncRNA', 'rRNA']

s.append(t)
# ['mRNA', 'tRNA', ['ncRNA', 'rRNA']]

s.extend(t)
# ['mRNA', 'tRNA', 'ncRNA', 'rRNA']
```

**Remember:** `append()` adds `y` as one item; `extend()` adds the items inside `y`.

### `insert()`

```python
mylist = [2, 3, 4]
mylist.insert(0, 1)
# [1, 2, 3, 4]
```

### `remove()` vs `pop()`

```python
x = [1, 2, 3, 2]

x.remove(2)        # remove first VALUE 2
```

```python
x = [1, 2, 3]
a = x.pop(1)       # remove INDEX 1 and return it
# a == 2
# x == [1, 3]
```

Without an index, `pop()` removes the last item.

---

## `sort()` vs `sorted()`

`sort()` changes the original list and returns `None`:

```python
x = [3, 1, 2]
x.sort()
print(x)
# [1, 2, 3]
```

Do **not** do:

```python
print(x.sort())
# None
```

`sorted()` returns a new sorted list:

```python
x = [3, 1, 2]
y = sorted(x)

# y == [1, 2, 3]
# x == [3, 1, 2]
```

### List comprehension

```python
mynewlist = [x * 2 for x in range(0, 5)]
# [0, 2, 4, 6, 8]
```

### Convert

```python
list(my_tuple)
tuple(my_list)
list('ACGT')       # ['A', 'C', 'G', 'T']
```

---

# 3. Lists and references

Python variables refer to objects.

```python
b = [3, 4]
a = [1, 2, b, 5, 6]

b[0] = -1
print(a)
# [1, 2, [-1, 4], 5, 6]
```

`a` contains a reference to the same list object as `b`.

Use `.copy()` when you want a separate list:

```python
b = [3, 4]
a = [1, 2, b.copy(), 5, 6]

b[0] = -1
print(a)
# [1, 2, [3, 4], 5, 6]
```

Object identity:

```python
id(a)
id(b)
```

---

# 4. Tuples

A tuple is an **ordered, immutable** collection.

```python
DNA_counts = (123, 31, 21, 44)
```

Properties:
- ordered
- immutable
- can contain different types
- duplicates are allowed
- can be indexed/sliced
- cannot have items added or removed
- defined using parentheses / commas
- lecture notes that tuples are faster than lists

```python
T1 = ('Lion', 'Dog', 'Cat', 'Tiger', 'Monkey')

T1[0]       # 'Lion'
T1[1:3]     # ('Dog', 'Cat')
len(T1)     # 5
T1 == T1    # True
T1 + ('Cow',)  # ('Lion', 'Dog', 'Cat', 'Tiger', 'Monkey', 'Cow')
T1 * 2      # ('Lion', 'Dog', 'Cat', 'Tiger', 'Monkey', 'Lion', 'Dog', 'Cat', 'Tiger', 'Monkey')
```

### Single-item tuple: trailing comma is required

```python
x = (2)       # integer 2
x = (2,)      # tuple containing 2
```

```python
DNA = ("ACGA",)
```

### Tuple unpacking

```python
T2 = ('Cow', 'Sheep')
T4, T5 = T2

# T4 == 'Cow'
# T5 == 'Sheep'
```

The number of values must match the number of variables.

```python
T2 = ('Cow', 'Sheep', 'Dog')
T4, T5 = T2      # error
```

---

# 5. Sets

A set is an **unordered collection of unique elements**.

```python
s = {1, 2, 3, 4}
```

Duplicates disappear:

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange']
fruit = set(basket)

# {'apple', 'orange', 'pear'}
```

Do not rely on the displayed order of a set.

### Membership

```python
'apple' in fruit        # True
'crabgrass' in fruit    # False
```

### Add/remove

```python
s.add(77)
s.remove(54)       # error if 54 does not exist
s.pop()            # removes an arbitrary element
```

### Set operations

```python
S = {1, 2, 3, 4, 5}
T = {4, 5, 6, 7}

S & T              # intersection -> {4, 5}
S | T              # union -> {1, 2, 3, 4, 5, 6, 7}
S - T              # in S but not T
```

Bioinformatics-style duplicate removal:

```python
sequences = ['ATG', 'ATG', 'GGC', 'TAA']
unique_sequences = set(sequences)
```

Sets are useful when **membership and uniqueness matter more than order**.

---

# 6. Common sequence operations

The lecture presents these for common sequence types such as strings, lists and tuples.

Given:

```python
s = ['mRNA', 'tRNA', 'siRNA', 'rRNA', 'snRNA']
x = 'mRNA'
```

| Operation | Meaning |
|---|---|
| `x in s` | `True` if x occurs |
| `x not in s` | `True` if x does not occur |
| `s + t` | concatenate |
| `s * n` | repeat n times |
| `s[i]` | item at index i |
| `s[i:j]` | slice i through j-1 |
| `s[i:k:j]` | slice with step |
| `len(s)` | length |
| `min(s)` | smallest item |
| `max(s)` | largest item |
| `s.index(x)` | first index of x |
| `s.count(x)` | number of occurrences of x |

Examples:

```python
s[0]
# 'mRNA'

s[0:2]
# ['mRNA', 'tRNA']

s[0:5:2]
# ['mRNA', 'siRNA', 'snRNA']

len(s)
# 5

s.index(x)
# 0

s.count(x)
# 1
```

---

# 7. Mutable sequence operations

Mutable sequences such as lists additionally support:

```python
s[i] = x          # replace item
s[i:j] = t        # replace slice
del s[i:j]        # delete slice
s[i:j:k] = t      # replace stepped slice
del s[i:j:k]      # delete stepped slice
s.append(x)       # add to end
```

Example:

```python
x = [0, 1, 0, 1, 0, 1]

x[1::2] = [2, 2, 2]

# [0, 2, 0, 2, 0, 2]
```

---

# 8. `split()` vs `list()`

These are different.

### `split()`

Splits a string into pieces using a separator:

```python
names = 'ACG,GGT,AGA'
codons = names.split(',')

# ['ACG', 'GGT', 'AGA']
```

### `list()`

Converts the string into individual characters:

```python
list(names)

# ['A', 'C', 'G', ',', 'G', 'G', 'T', ',', 'A', 'G', 'A']
```

---

# 9. Dictionaries

A dictionary maps **keys to values**.

```python
d = {
    'Ala': 89.1,
    'Arg': 174.2
}
```

Bioinformatics example:

```python
weights = {
    'Ala': 89.1,
    'Arg': 174.2,
    'Gly': 75.1
}
```

Access by key:

```python
weights['Ala']
# 89.1
```

Dictionary keys must be unique.

### Membership and length

```python
'Ala' in weights
'Ala' not in weights
len(weights)
```

### Add/change/delete

```python
weights['Ser'] = 105.1       # add
weights['Ala'] = 90.0        # change
del weights['Ala']           # delete
```

Dictionaries are accessed by **keys**, not numerical indexes.

---

# 10. `get()` and `setdefault()`

Accessing a missing key directly causes an error:

```python
d['Gly']
```

Use `get()` when the key may not exist:

```python
d.get('Gly')
# None
```

Optional default:

```python
d.get('Gly', 75.1)
# 75.1
```

`get()` does **not** add the key.

### `setdefault()`

```python
d.setdefault('Gly', 75.1)
```

If `Gly` exists, its existing value is returned.

If it does not exist, `Gly` is added with `75.1`.

**Difference:**

```python
d.get(key, default)
# read / return; does not update dictionary

d.setdefault(key, default)
# read / return; adds key if missing
```

---

# 11. Dictionary keys, values and items

```python
d.keys()
d.values()
d.items()
```

For:

```python
d = {'Gly': 75.1, 'Arg': 174.2, 'Ser': 105.1}
```

you get the dictionary's:

```text
keys   -> Gly, Arg, Ser
values -> 75.1, 174.2, 105.1
items  -> ('Gly', 75.1), ('Arg', 174.2), ...
```

---

# 12. Nested dictionaries

Dictionaries can contain other dictionaries:

```python
thisdict = {
    "Molecule1": {"name": "DNA", "Content": "ACGT"},
    "Molecule2": {"name": "RNA", "Content": "ACGU"}
}
```

Access nested values:

```python
thisdict["Molecule1"]["name"]
# DNA
```

They can also contain sets or other collection types.

---

# [13. `%` string formatting](Supplementary/ 13_explained.md)

The lecture introduces `%` formatting with format specifiers:

| Code | Meaning |
|---|---|
| `%s` | string |
| `%d` | integer |
| `%f` | floating point |

```python
name = "Danny"
age = 55

print("%s is %d years old." % (name, age))
# Danny is 55 years old.
```

A list can be formatted too:

```python
mylist = [1, 2, 3]
print("A list: %s" % mylist)
```

Multiple values:

```python
data = ("Daniel", "LaRusso", 5)
format_string = "Hello %s %s. You finished season #%s."

print(format_string % data)
```

---

# 14. `.format()` output formatting

Use `{}` as placeholders:

```python
'X:{} Y:{}'.format(6, 7)
# 'X:6 Y:7'
```

### Positional identifiers

```python
'X:{1} Y:{0}'.format(6, 7)
# 'X:7 Y:6'
```

The numbers refer to the arguments passed to `.format()`.

### Named identifiers

```python
'X:{a} Y:{b}'.format(a=5, b=2)
# 'X:5 Y:2'
```

### Format an element of a list

```python
dList = [5, 7]

'X:{0[0]} Y:{0[1]}'.format(dList)
# 'X:5 Y:7'
```

Named version:

```python
'X:{data[0]} Y:{data[1]}'.format(data=dList)
```

### Format decimal places

```python
print(
    "My average of this {0} was {1:.2f}%"
    .format("semester", 78.234876)
)

# My average of this semester was 78.23%
```

`.2f` = floating point number with 2 decimal places.

### Binary formatting

```python
"The {0} of 100 is {1:b}".format("binary", 100)
# The binary of 100 is 1100100
```

Equivalent approach shown in the lecture:

```python
bin(100)[2:]
# '1100100'
```

---

# 15. `zip()`

`zip()` pairs corresponding elements from two objects.

```python
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]

data1 = list(zip(letters, numbers))

# [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
```

Think:

```text
b -> 2
a -> 4
d -> 3
c -> 1
```

### `zip()` + `sort()`

```python
data1.sort()
```

Sorts by the first element of each tuple:

```python
[('a', 4), ('b', 2), ('c', 1), ('d', 3)]
```

If you reverse the arguments:

```python
data2 = list(zip(numbers, letters))
data2.sort()
```

the numbers are first, so sorting is by number:

```python
[(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]
```

---

# 16. Avoid overwriting built-in names

The lecture warns about doing things like:

```python
int = 8
```

Now `int` is a variable rather than the normal built-in `int()` function.

If this happens:

```python
del int
```

clears the variable.

Avoid variable names such as:

```python
int
list
str
set
dict
tuple
sum
min
max
```

---

# 17. Quick comparison

```text
LIST
[1, 2, 2, 3]
ordered | mutable | duplicates allowed | indexable

TUPLE
(1, 2, 2, 3)
ordered | immutable | duplicates allowed | indexable

SET
{1, 2, 3}
unordered | mutable | duplicates removed | no normal indexing

DICTIONARY
{'Ala': 89.1, 'Arg': 174.2}
key -> value | mutable | keys unique | access by key
```

### Choosing the right structure

**Need an ordered collection that you will change?**  
→ `list`

**Need an ordered collection that should not change?**  
→ `tuple`

**Need unique elements / membership / set operations?**  
→ `set`

**Need a key → value relationship?**  
→ `dictionary`

---

# 18. High-yield exam/exercise reminders

### Indexing

```python
x[0]        # first item
x[-1]       # last item
```

### Slicing

```python
x[start:stop:step]
```

`stop` is excluded.

### Mutability

```text
list       mutable
tuple      immutable
string     immutable
set        mutable
dictionary mutable
```

### `sort()` vs `sorted()`

```python
x.sort()       # modifies x; returns None
sorted(x)      # returns a new sorted list
```

### `append()` vs `extend()`

```python
x.append(y)    # y becomes ONE item
x.extend(y)    # contents of y are added
```

### `remove()` vs `pop()`

```python
x.remove(value)   # remove by VALUE
x.pop(index)      # remove by INDEX and return it
```

### `split()` vs `list()`

```python
"ACG,GGT".split(",")
# ['ACG', 'GGT']

list("ACG,GGT")
# ['A', 'C', 'G', ',', 'G', 'G', 'T']
```

---

# 19. Bioinformatics examples

### Amino-acid collection

```python
amino_acids = ['Ala', 'Arg', 'Asn', 'Asp']
```

### Fixed amino-acid tuple

```python
amino_acids = ('Ala', 'Arg', 'Asn', 'Asp')
```

### Remove duplicate sequences

```python
sequences = ['ATG', 'ATG', 'GGC', 'TAA']
unique_sequences = set(sequences)
```

### Amino acid → molecular weight

```python
weights = {
    'Ala': 89.1,
    'Arg': 174.2,
    'Gly': 75.1
}

print(weights['Ala'])
# 89.1
```

### Pair genes and lengths

```python
genes = ['geneA', 'geneB', 'geneC']
lengths = [100, 250, 180]

data = list(zip(genes, lengths))
# [('geneA', 100), ('geneB', 250), ('geneC', 180)]
```

---

# 20. One-page mental model

```text
                  COLLECTIONS
                       |
       +---------------+---------------+
       |               |               |
     LIST            TUPLE            SET
      []              ()               {}
      |                |                |
   ordered          ordered         unordered
   mutable          immutable       unique


                DICTIONARY
                    {}
                     |
                  key -> value
                     |
                 access by key
```

## Source

Based on **BINP16 Bioinformatics: Programming in Python — Lecture 2: Collection data types**, Lund University, October 2026.

The lecture objectives are to practice tuples, lists, sets, dictionaries, common sequence operators/functions, and output formatting.
