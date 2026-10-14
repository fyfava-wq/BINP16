# BINP16 — Python Lecture 6 Cheat Sheet: Regular Expressions

> GitHub-ready notes based on **Lecture 6 – Regular expressions** and `Lecture 6 - RE.py`.
> Regular expressions (REs / regex) describe patterns for searching, extracting, replacing, or splitting text.

## 1. Import `re`

```python
import re
```

Use regex when you need to find a *pattern*, such as digits, a range of letters, or either of several words. For an exact substring, ordinary string methods such as `.find()` and `.replace()` are often simpler.

```python
text = "This is a survival story."
print(text.find("survival"))       # position of first occurrence
print(text.replace("survival", "success"))
```

## 2. The main `re` functions

| Function | What it does | Result |
|---|---|---|
| `re.search(pattern, text)` | Finds the **first** match anywhere in the string | Match object or `None` |
| `re.match(pattern, text)` | Checks for a match **at the beginning** of the string | Match object or `None` |
| `re.findall(pattern, text)` | Finds all non-overlapping matches | List |
| `re.finditer(pattern, text)` | Iterates over all matches, including their positions | Iterator of match objects |
| `re.sub(pattern, replacement, text)` | Replaces matches | New string |
| `re.split(pattern, text)` | Splits at matches of the pattern | List of strings |
| `re.compile(pattern)` | Creates a reusable pattern object | Pattern object |

### `search()` versus `match()`

```python
text = "Forever young"

print(re.search("young", text))  # finds young anywhere
print(re.match("young", text))   # None: young is not at the beginning
print(re.match("Forever", text)) # matches at the beginning
```

### First match versus all matches

```python
text = "Forever young, forever free"

print(re.search("forever", text))
# One match object: the first lowercase 'forever'

print(re.findall("forever", text))
# ['forever', 'forever']
```

Regex is case-sensitive by default: `"Forever"` and `"forever"` are different patterns.

## 3. Match objects and positions

A successful `search()`, `match()`, or `finditer()` match gives a match object.

```python
text = "A survival story"
match = re.search("survival", text)

if match:
    print(match.group())  # matched text: survival
    print(match.start())  # starting index: 2
    print(match.end())    # index just after the match: 10
    print(match.span())   # (2, 10)
```

- `.group()` or `.group(0)`: the entire matched substring.
- `.start()`: start index.
- `.end()`: index just **after** the match.
- `.span()`: `(start, end)` pair.
- If no match exists, `search()` returns `None`; check before calling `.group()`.

### Get positions for every match

```python
text = "Forever young, forever free"

positions = [(m.start(), m.end()) for m in re.finditer("Forever|forever", text)]
print(positions)
```

The equivalent loop:

```python
positions = []
for match in re.finditer("Forever|forever", text):
    positions.append((match.start(), match.end()))
```

## 4. Essential regex symbols

| Pattern | Meaning | Example match |
|---|---|---|
| `.` | Any character except newline by default | `a`, `7`, `?` |
| `^` | Start of string (or line in multiline mode) | `^DNA` |
| `$` | End of string (or line in multiline mode) | `DNA$` |
| `*` | Zero or more of previous item | `A*` |
| `+` | One or more of previous item | `\d+` |
| `?` | Zero or one of previous item; also makes repetition lazy | `colou?r` |
| `{n}` | Exactly `n` repetitions | `\d{4}` |
| `{n,m}` | From `n` to `m` repetitions | `A{2,4}` |
| `[ABC]` | One character from the listed set | `grade [ABC]` |
| `[A-E]` | One character in a range | `[A-E]` |
| `[^ABC]` | One character **not** in the set | `[^0-9]` |
| `(pattern)` | Capture a group | `(\d+)` |
| `A\|B` | Either pattern A or pattern B | `DNA\|RNA` |
| `\` | Escape a special character or introduce a code | `\.` means literal dot |

**Important:** `*`, `+`, and `?` apply to the item immediately before them.

```python
re.findall(r"\d+", "Room 12, floor 3")  # ['12', '3']
re.findall(r"\d\d", "Room 12, floor 345")  # ['12', '34']
```

## 5. Character codes

| Code | Meaning |
|---|---|
| `\d` | A digit |
| `\D` | A non-digit |
| `\s` | Whitespace (space, tab, newline, etc.) |
| `\S` | A non-whitespace character |
| `\w` | A word character (letters, digits, underscore) |
| `\W` | A non-word character |
| `\b` | Word boundary |

Examples:

```python
re.findall(r"\d+", "Years: 2012 and 2025")  # ['2012', '2025']
re.findall(r"\b\d{4}\b", "2012 25 2025")    # ['2012', '2025']
re.findall(r"\s\d+", "abc 12 abc34")        # [' 12']
```

`\s\d+` requires whitespace before the digits. `\d+` alone can find digits wherever they occur.

## 6. Character sets and ranges

```python
re.search(r"[Nn]atural", "Natural selection")  # accepts N or n
re.search(r"grade [A-E]", "grade B")           # accepts A through E
re.search(r"[A-Z0-9]", "grade 2")              # one uppercase letter or digit
```

A character set such as `[A-Z0-9]` matches **one character**. Add a repetition operator if you want more than one.

```python
re.findall(r"[A-Z]+", "DNA and RNA")  # ['DNA', 'RNA']
```

To search for literal regex-special characters, escape them:

```python
re.search(r"\[abc\]", "Text with exactly [abc] inside")
re.search(r"\.", "DNA.")  # literal full stop
```

Common special characters include `. ^ $ * + ? { } [ ] \ | ( )`.

## 7. Alternatives: `|`

Use `|` for “or”.

```python
re.findall(r"DNA|RNA", "The genome consists of DNA")
# ['DNA']

re.findall(r"DNA|RNA", "The genome consists of RNA")
# ['RNA']
```

Combine alternatives with other patterns:

```python
pattern = re.compile(r"\s(DNA|RNA)\.")
print(pattern.search("The genome consists of DNA."))
print(pattern.search("The genome consists of RNA."))
```

The pattern requires whitespace, then `DNA` or `RNA`, then a literal period.

## 8. Groups: `group()` and `groups()`

Parentheses capture parts of a match.

```python
text = "In the year of 2012 the world did not end, but maybe in 2025"

match = re.search(r"(\d+)\D+(\d+)", text)

print(match.group(0))  # entire match
print(match.group(1))  # first captured group: 2012
print(match.group(2))  # second captured group: 2025
print(match.groups())  # ('2012', '2025')
```

- `group(0)` is the **whole match**, not the first captured group.
- `group(1)` is the first set of parentheses.
- `group(2)` is the second set of parentheses.
- `groups()` returns all captured groups as a tuple.
- `search()` returns only the first match. Use `findall()` or `finditer()` to find multiple occurrences.

Example to extract all years:

```python
text = "Years 2012, 2025 and 2030"
print(re.findall(r"\d+", text))  # ['2012', '2025', '2030']
```

## 9. Greedy and lazy matching

By default, repetition is greedy: it tries to match as much text as possible.

```python
text = "young one? young two?"
print(re.search(r"young.+\?", text).group())
# Can include text through the last question mark
```

Adding `?` after a repetition makes it lazy (as short as possible while still matching):

```python
print(re.search(r"young.+?\?", text).group())
# 'young one?'
```

## 10. Newlines and `re.DOTALL`

Normally, `.` does not match a newline (`\n`). `re.DOTALL` changes this.

```python
text = "Line one\nLine two\nLine three"

print(re.findall(r".+", text))
# One match per non-empty line

print(re.findall(r".+", text, re.DOTALL))
# One match spanning the whole text
```

Use `re.DOTALL` when a pattern using `.` must cross line breaks.

## 11. Replacing with `re.sub()`

Syntax:

```python
re.sub(pattern, replacement, text, count=0)
```

`count=0` means replace all occurrences.

```python
text = "I am a harmless regex pattern, so harmless"

print(re.sub(r"harm", "", text))
# Removes every 'harm'

print(re.sub(r"less", "ful", "harmless"))
# harmful

print(re.sub(r"\s+", " ", "xxx  xxx      xxxx"))
# xxx xxx xxxx
```

The last example collapses one or more whitespace characters into a single space.

## 12. Splitting strings

### Regex split: `re.split()`

```python
text = "Forever young I want to be forever young"

print(re.split(r"young", text))
print(re.split(r"\s+", text))
```

`re.split()` splits wherever the pattern matches.

### Ordinary string methods

Use these if the separator is simple; they are often easier to read.

```python
text = "In the year of 2012 the world did not end"

text.split("2012")          # split at exact substring
text.split("year", 1)       # at most 1 split from the left
text.rsplit("year", 1)      # at most 1 split from the right
text.split()                # split on runs of whitespace
text.splitlines()           # split at line breaks
```

- `maxsplit=1` creates at most two pieces.
- `split()` with no separator uses whitespace.
- `splitlines()` splits at line breaks and removes the line-break characters.
- Use `re.split()` when the separator is a **pattern** or one of several different delimiters.

### Join a list of strings

```python
words = ["hello", "world"]
print(" ".join(words))  # hello world
```

The separator goes **between** list items.

### Slice a string

```python
text = "In the year of 2012"
print(text[5:12])
# Same idea as:
part = text[slice(5, 12, 1)]
```

Slice syntax is `text[start:stop:step]`; the stop index is excluded.

## 13. Compile and reuse a pattern

If you use the same pattern repeatedly, compile it once:

```python
pattern = re.compile(r"\d+")

print(pattern.findall("Room 101"))          # ['101']
print(pattern.findall("In 2025 things change"))  # ['2025']
```

A compiled pattern can use `.search()`, `.match()`, `.findall()`, `.finditer()`, `.sub()`, and `.split()`.

```python
pattern = re.compile(r"[Nn]atural")
match = pattern.search("Natural selection")
```

## 14. Raw strings: `r"..."`

Prefer raw strings for regex patterns, especially when using backslashes.

```python
re.findall(r"\d+", "Room 101")
re.search(r"\\documents", r"C:\documents")
```

The `r` prefix tells Python to keep backslashes in the string rather than interpreting them as Python string escapes. In regex, `\\` represents a literal backslash.

Without a raw string, backslashes often need extra escaping, making patterns harder to read.

## 15. Counting matches

Count occurrences by finding them and measuring the resulting list:

```python
import re

Z1 = "1 1 1 2 2 3 3 2 3"

print(len(re.findall(r"2", Z1)))  # 3
print(len(re.findall(r"3", Z1)))  # 3
```

Count the exact adjacent sequence `2 3`:

```python
print(len(re.findall(r"2\s3", Z1)))  # 2
```

For simple exact counting, no regex is needed:

```python
print(Z1.count("2"))    # 3
print(Z1.count("2 3"))  # exact substring occurrences
```

Be clear about what is being counted:
- `re.findall(r"[23]", Z1)` finds every individual `2` or `3`.
- `re.findall(r"2\s3", Z1)` finds a `2`, whitespace, and then `3`.
- `Z1.count("2 3")` counts exact occurrences of that substring.

## 16. Repeated characters and backreferences

A backreference such as `\1` matches the same text captured by the first group.

```python
text = "xx sdfewr aaaa BB xsdsd xx"
print(re.findall(r"([A-Za-z])\1+", text))
# ['x', 'a', 'B', 'x']
```

The pattern finds runs of repeated letters:
- `([A-Za-z])` captures one letter.
- `\1+` matches one or more additional copies of that same letter.

To return the entire repeated run rather than just the captured letter:

```python
print([m.group(0) for m in re.finditer(r"([A-Za-z])\1+", text)])
# ['xx', 'aaaa', 'BB', 'xx']
```

## 17. Bioinformatics-style examples

```python
import re

sequence = "ATGCGTNNATG"

# Find all runs of A, T, C, or G
print(re.findall(r"[ATCG]+", sequence))

# Check whether a sequence contains one or more N characters
print(re.search(r"N+", sequence))

# Find all three-digit numbers in a text
print(re.findall(r"\d{3}", "sample123 position456"))

# Replace runs of whitespace with one space
text = "sample   one\t sample two"
print(re.sub(r"\s+", " ", text))
```

These are demonstrations of the regex syntax; choose a pattern that matches the exact rules of your data.

## 18. Common mistakes

| Mistake | Why it is a problem | Better approach |
|---|---|---|
| Using `re.match()` to search anywhere | `match()` only checks the start | Use `re.search()` |
| Expecting `search()` to return every match | It stops at the first match | Use `findall()` or `finditer()` |
| Calling `.group()` when there is no match | The result is `None` | Check `if match:` first |
| Using `\d` for a multi-digit number | `\d` matches one digit | Use `\d+` or `\d{4}` |
| Forgetting that `[A-Z0-9]` matches one character | A character set describes one character | Add `+` for one or more |
| Forgetting to escape `.` | In regex, `.` means any non-newline character | Use `r"\."` for a literal dot |
| Using normal strings with many backslashes | Python may process escapes first | Prefer raw strings: `r"..."` |
| Expecting `.` to cross newlines | It does not by default | Use `re.DOTALL` if needed |
| Assuming `group(1)` is the entire match | It is the first captured group | Use `group(0)` for the full match |
| Using regex for a simple exact substring | Often less readable | Consider `.find()`, `.replace()`, or `.count()` |

## 19. Quick reference

| Goal | Example |
|---|---|
| First match anywhere | `re.search(r"\d+", text)` |
| Match only at beginning | `re.match(r"DNA", text)` |
| All matches as a list | `re.findall(r"\d+", text)` |
| Match objects with positions | `re.finditer(r"\d+", text)` |
| Start/end positions | `match.start()`, `match.end()`, `match.span()` |
| Whole match | `match.group(0)` |
| Captured groups | `match.groups()` |
| Replace pattern | `re.sub(r"\s+", " ", text)` |
| Split by pattern | `re.split(r"\W+", text)` |
| Reuse pattern | `pattern = re.compile(r"\d+")` |
| Match digits | `r"\d+"` |
| Match a four-digit number | `r"\b\d{4}\b"` |
| Match DNA or RNA | `r"DNA\|RNA"` |
| Match a literal dot | `r"\."` |
| Match a literal backslash | `r"\\"` |
| Allow dot to cross newlines | `re.DOTALL` |

## Mental model

- **Pattern** = the rule you want to find.
- **`search`** = first match anywhere.
- **`match`** = match at the beginning.
- **`findall`** = all matched text.
- **`finditer`** = all match objects, useful for positions.
- **Groups `()`** = capture useful parts of a match.
- **`sub`** = replace matches.
- **`split`** = divide text at matches.
- **`compile`** = prepare a pattern for reuse.
- **Raw strings `r"..."`** = easier-to-read patterns with backslashes.

## Lecture source

Prepared from the uploaded `Lecture 6 - Regular expression.pdf` and `Lecture 6 - RE.py`. The lecture's topics include `search`, `match`, `findall`, `finditer`, `sub`, `split`, `compile`, character codes and ranges, groups, raw strings, newline handling, and counting with regex.
