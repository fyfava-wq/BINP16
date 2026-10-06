# 13. `%` String Formatting — Explained

The `%` operator can be used to **insert values into a string**.

Instead of building a sentence manually with `+`, you write a **format string** containing placeholders such as `%s`, `%d`, and `%f`, then provide the values that should fill those placeholders.

The basic pattern is:

```python
"some text %s more text" % value
```

For multiple values:

```python
"%s ... %d ..." % (value1, value2)
```

The values are inserted into the placeholders **from left to right**.

---

## 13.1 Format specifiers

A **format specifier** tells Python what kind of value will be inserted.

| Specifier | Meaning | Example |
|---|---|---|
| `%s` | string | `"Danny"` |
| `%d` | integer | `55` |
| `%f` | floating-point number | `78.23` |

Think of a placeholder as an empty space that says:

> "Put a value of this type here."

For example:

```python
"%s is %d years old."
```

contains two placeholders:

```text
%s → put a string here
%d → put an integer here
```

---

## 13.2 One value

Suppose:

```python
name = "Danny"
```

We can put `name` into `%s`:

```python
print("%s is here." % name)
```

Output:

```text
Danny is here.
```

The `%s` is replaced by the value stored in `name`.

---

## 13.3 Multiple values

Suppose:

```python
name = "Danny"
age = 55
```

We want:

```text
Danny is 55 years old.
```

Write:

```python
print("%s is %d years old." % (name, age))
```

There are two placeholders:

```text
%s → name
%d → age
```

The values are supplied in:

```python
(name, age)
```

Python matches them **from left to right**:

```text
%s  ← name
%d  ← age
```

So:

```python
"%s is %d years old." % (name, age)
```

produces:

```text
Danny is 55 years old.
```

### Important

The order matters.

```python
"%s is %d years old." % (name, age)
```

means:

```text
1st placeholder ← 1st value
2nd placeholder ← 2nd value
```

---

## 13.4 Why are parentheses used for multiple values?

With one value:

```python
"%s" % name
```

With several values, they are grouped together:

```python
"%s %d" % (name, age)
```

Here:

```python
(name, age)
```

is a **tuple** containing the values.

You can also create the tuple first:

```python
data = ("Danny", 55)

print("%s is %d years old." % data)
```

---

## 13.5 A list can also be inserted

`%s` can be used to insert a whole object such as a list:

```python
mylist = [1, 2, 3]

print("A list: %s" % mylist)
```

Output:

```text
A list: [1, 2, 3]
```

Here `%s` is replaced by the list.

---

## 13.6 Multiple values using a tuple

The lecture gives:

```python
data = ("Daniel", "LaRusso", 5)

format_string = "Hello %s %s. You finished season #%s."

print(format_string % data)
```

There are three placeholders:

```text
%s → first name
%s → surname
%s → season number
```

And `data` contains three values:

```text
"Daniel"
"LaRusso"
5
```

Python matches them by position:

```text
%s  ← "Daniel"
%s  ← "LaRusso"
%s  ← 5
```

Result:

```text
Hello Daniel LaRusso. You finished season #5.
```

---

## 13.7 The general rule

The easiest way to understand `%` formatting is:

```python
"FORMAT STRING" % VALUES
```

For example:

```python
"%s is %d years old." % ("Danny", 55)
```

Read it as:

> Take this string and replace `%s` with `"Danny"` and `%d` with `55`.

---

## 13.8 More examples

### Two strings

```python
first = "Daniel"
last = "LaRusso"

print("Name: %s %s" % (first, last))
```

Output:

```text
Name: Daniel LaRusso
```

### String + integer

```python
gene = "BRCA1"
length = 1863

print("%s has length %d." % (gene, length))
```

Output:

```text
BRCA1 has length 1863.
```

### String + floating-point number

```python
protein = "Ala"
weight = 89.1

print("%s has a molecular weight of %f." % (protein, weight))
```

Output:

```text
Ala has a molecular weight of 89.100000.
```

---

## 13.9 Matching placeholders and values

The number and order of placeholders should match the supplied values.

```python
"%s %s %d" % ("Daniel", "LaRusso", 5)
```

There are:

```text
3 placeholders
3 values
```

They correspond:

```text
%s → "Daniel"
%s → "LaRusso"
%d → 5
```

A useful way to think about it:

```text
FORMAT:   %s        %s          %d
VALUES:   Daniel    LaRusso     5
          ↓         ↓           ↓
RESULT:   Daniel    LaRusso     5
```

---

## 13.10 Common mistake: wrong order

Consider:

```python
name = "Danny"
age = 55

print("%s is %d years old." % (age, name))
```

The placeholders expect:

```text
%s → string
%d → integer
```

but the values are supplied as:

```text
%s → 55
%d → "Danny"
```

The order/types are wrong.

Correct:

```python
print("%s is %d years old." % (name, age))
```

---

## 13.11 `%` formatting vs `+`

Without formatting:

```python
name = "Danny"
age = 55

print(name + " is " + str(age) + " years old.")
```

`age` has to be converted to a string:

```python
str(age)
```

With `%` formatting:

```python
print("%s is %d years old." % (name, age))
```

you can put the integer directly into `%d`.

---

## 13.12 Quick reference

```python
%s      # string
%d      # integer
%f      # floating-point number
```

### One value

```python
"Name: %s" % name
```

### Multiple values

```python
"Name: %s, Age: %d" % (name, age)
```

### Using a tuple

```python
data = ("Daniel", "LaRusso", 5)
"Hello %s %s. Season #%s." % data
```

### Using a list

```python
mylist = [1, 2, 3]
"A list: %s" % mylist
```

---

## The key idea

```python
"%s is %d years old." % (name, age)
```

Break it into:

```text
"%s is %d years old."
 ↑          ↑
placeholders

        %

        ↓

(name, age)
 ↑       ↑
values
```

**The placeholders are filled from left to right:**

```text
%s ← first value
%d ← second value
```

So:

```python
"%s is %d years old." % ("Danny", 55)
```

becomes:

```text
Danny is 55 years old.
```

> **Remember:** `%s` = string, `%d` = integer, `%f` = float.
