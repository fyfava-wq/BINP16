# BINP16 Python — Lecture 5 Cheat Sheet: Functions

GitHub-ready notes based on **Lecture 5 – Functions** (`Lecture 5 - functions.pdf`) and the accompanying `Lecture 5.py` examples.

## 1. What is a function?

A function is a named block of code that performs a specific task. Defining a function does not run it; you must **call** it.

Why use functions?
- Reuse code instead of repeating it.
- Make the main program easier to read.
- Separate tasks into manageable pieces.
- Test a task independently.

```python
# Define the function

def say_hi():
    print("Hello World!")

# Call the function
say_hi()
say_hi()  # Can call it more than once
```

## 2. Parameters, arguments, and return values

- **Parameter**: a name in the function definition, e.g. `name`.
- **Argument**: the actual value supplied when calling the function, e.g. `"Moses"`.
- **`return`**: sends a value back to the code that called the function.
- **`print()`** displays something; it does not return that displayed text.

### No parameter

```python
def say_hi():
    print("Hello World!")

say_hi()
```

### One parameter; print only

```python
def say_hi(name):
    print("Hello " + name)

say_hi("Homer")
```

### One parameter; return a value

```python
def say_hi(name):
    response = "Hello " + name + "!"
    return response

print(say_hi("Moses"))
print(say_hi("Deborah"))
```

### Two parameters

```python
def say_hi(name1, name2):
    response = "Hello " + str(name1) + " and " + str(name2)
    return response

responses = say_hi("C. Darwin", "R. Dawkins")
print(responses)
print(say_hi(4, 5))
```

`str()` converts non-string arguments to strings before concatenation.

### Print vs return

```python
def show_square(x):
    print(x * x)       # displays the result

def get_square(x):
    return x * x       # gives the result back to the caller

show_square(4)
answer = get_square(4)
print(answer)
```

A function without a `return` value returns `None` automatically.

## 3. Returning values and ending a function

```python
def calc_func(x):
    return 2 * x * x + 4 * x

print(calc_func(5))  # 70
```

A function can have several `return` statements. As soon as one executes, the function ends; code below it in that path is not run.

```python
def classify_number(x):
    y = 2 * x + 4 * x

    if y > 0:
        return "Positive"
    elif y < 0:
        return "Negative"
    return "Zero"

print(classify_number(5))
print(classify_number(-5))
print(classify_number(0))
```

The lecture example returns `None` for zero by using a bare `return`. Returning an explicit string such as `"Zero"` is an optional clearer variation.

## 4. Default argument values

A default is used when the caller does not supply that argument.

```python
def run_simulation(x, num_steps=10):
    print(x)
    print(num_steps)

run_simulation(500, 20)  # uses 20
run_simulation(500)      # uses default 10
```

You can use positional or keyword arguments:

```python
def simulate(initial_temp=30, num_steps=1000):
    print(initial_temp, num_steps)

simulate(20, 800)
simulate(20)
simulate()
simulate(initial_temp=20, num_steps=800)
simulate(num_steps=800, initial_temp=20)  # valid, but less easy to maintain
```

**Rule:** mandatory parameters must come before parameters with defaults.

```python
def simulate(initial_temp, num_steps=1000):
    ...
```

When adding a new parameter to an existing function, the lecture recommends putting it at the end with a default value so old calls continue to work.

## 5. Avoid overwriting built-in function names

The lecture demonstrates accidentally defining a function called `abs`, which replaces the built-in name in the current scope:

```python
# Avoid this:
# def abs(name1, name2):
#     ...
```

After overwriting a built-in, `abs(-3.0)` no longer calls Python's original absolute-value function. In a notebook, `del abs` removes the name you defined, allowing the built-in to be found again (if you have not overwritten it elsewhere).

**Avoid using built-in names for variables or functions**, including `abs`, `list`, `str`, `sum`, `input`, and `chr`.

## 6. Mutable and immutable objects passed to functions

A function receives a reference to the object passed to it. Whether changes are visible outside the function depends on the object and operation.

### Mutable example: lists can change in place

```python
def add_100(param):
    param += [100]
    print(param)

param = [10]
add_100(param)  # [10, 100]
add_100(param)  # [10, 100, 100]
print(param)    # original list has changed
```

A list is **mutable**: it can be changed after creation. Here, `+= [100]` changes the same list.

### Separate lists are independent

```python
def add_100(param):
    param += [100]
    print(param)

add_100([1])
add_100([10])
add_100([100])
```

Each call receives a new list, so changes do not accumulate between calls.

### Immutable example: integers

```python
def add_100(param):
    param += 100
    print(param)

param = 10
add_100(param)
add_100(param)
print("Outside function:", param)  # still 10
```

Integers, strings, and tuples are immutable. `param += 100` binds the local parameter name to a new integer; it does not change the caller's `param`.

### Make a copy before passing a list

```python
param = [10]
temp = param.copy()  # creates a separate list

add_100(temp)
print("temp:", temp)    # changed
print("param:", param)  # unchanged
```

Do not use `temp = param` when you want a separate list: that gives two names for the same list object.

## 7. Never use a mutable object as a default value

Default arguments are evaluated **once**, when the function is defined. A default list can therefore keep changes between calls.

### Problematic pattern

```python
def add_100(param=[]):
    param.append(100)
    print(param)

add_100()  # [100]
add_100()  # [100, 100]
add_100()  # [100, 100, 100]
```

### Recommended pattern: use `None`

```python
def add_100(param=None):
    if param is None:
        param = []
    param.append(100)
    print(param)

add_100()  # [100]
add_100()  # [100] — fresh list for this call
add_100()  # [100]
```

**Remember:** `None` means “no value supplied” here. Create the new list inside the function.

## 8. Variable scope: local and global

### Local variables

A variable defined inside a function is local to that function and normally cannot be accessed outside it.

```python
def math_func(x, y):
    z = (x + y) * (x - y)
    return z

answer = math_func(6, 5)
print(answer)  # 11
# print(z)    # NameError: z is local to math_func
```

### Reading a global variable

A function can read a global variable:

```python
a = 100

def math_func(x, y):
    z = x + y + a
    return z

print(math_func(5, 6))  # 111
```

### Modifying a global variable

If you assign to a name inside a function, Python normally treats that name as local. To reassign the global variable, use `global` (though passing values and returning results is usually easier to reason about).

```python
a = 100

def add_to_a(x):
    global a
    a = a + x

add_to_a(5)
print(a)  # 105
```

Without `global`, `a = a + x` inside the function attempts to read a local `a` before it has a value, causing `UnboundLocalError`.

**Good practice:** prefer passing values as arguments and returning results rather than changing global variables.

## 9. Nested functions and closures

A nested function is defined inside another function. It can access variables in the enclosing function.

```python
def print_msg(msg):
    def printer():
        print(msg)

    printer()

print_msg("Hello from printers")
```

Here, `printer()` can use `msg`, even though `msg` is a parameter of the outer function.

### Returning a function

```python
def num1(x):
    def num2(y):
        return x * y
    return num2

res = num1(10)  # returns the function num2; it does not call num2 yet
print(res(2))   # 20

res = num1(2)
print(res(3))   # 6
```

A **closure** is a returned inner function that retains access to variables from the enclosing scope, such as `x` above.

## 10. Variable-length arguments: `*args` and `**kwargs` (optional)

- `*args` collects extra positional arguments into a **tuple**.
- `**kwargs` collects extra keyword arguments into a **dictionary**.

```python
def test_fun(item, *args, **kwargs):
    print("Mandatory argument:", item)
    print("Unnamed arguments:", args)
    print("Keyword arguments:", kwargs)

test_fun("Hello", 1, "Temp", 99, valueA="ABC", valueB=7)
test_fun("Hello world")
```

For the first call, `args` is `(1, 'Temp', 99)` and `kwargs` is `{'valueA': 'ABC', 'valueB': 7}`. In the second call, both are empty.

Use these when a function needs to accept a variable number of arguments. The lecture also shows forwarding them to another function with `other_function(*args, **kwargs)`.

## 11. Reverse complement of DNA or RNA

The lecture's bioinformatics example complements the bases and reverses the sequence.

```python
def reverse_complement(sequence, is_dna=True):
    if is_dna:
        sequence = sequence.replace("U", "T")
        trans_table = sequence.maketrans("ATGC", "TACG")
    else:
        sequence = sequence.replace("T", "U")
        trans_table = sequence.maketrans("AUGC", "UACG")

    complement = sequence.translate(trans_table)
    reverse_comp = complement[::-1]
    return reverse_comp

seq1 = "GATTACA"
seq2 = "GAUUGCU"

print(reverse_complement(seq1))               # TGTAATC
print(reverse_complement(seq1, is_dna=False)) # UGUAAUC
print(reverse_complement(seq2, False))        # AGCAAUC
```

- `str.maketrans()` creates a character translation table.
- `.translate()` applies the table.
- `[::-1]` reverses a string using slicing.
- `is_dna=True` is a default argument, so it can be omitted for DNA.

## 12. Recursion (optional)

**Recursion** means a function calls itself. It needs a stopping condition (base case); otherwise, it may never finish.

```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)
```

The calls count down from 6 to 0. As they return, the printed results are `1, 3, 6, 10, 15, 21`.

Be careful: recursion can use time and memory, and Python limits recursion depth. For many simple repetitions, a loop is usually simpler.

## 13. Lambda functions (optional)

A `lambda` creates a small anonymous function. The expression after `:` is its result.

```python
cube = lambda x: x * x * x
print(cube(3))  # 27
```

Equivalent named function:

```python
def cube(x):
    return x * x * x

print(cube(3))  # 27
```

The lecture also demonstrates creating functions that remember a multiplier:

```python
def make_multiplier(n):
    return lambda a: a * n

my_doubler = make_multiplier(2)
my_tripler = make_multiplier(3)

print(my_doubler(11))  # 22
print(my_tripler(11))  # 33
```

Use `lambda` for short expressions. Use `def` when the logic needs multiple lines or a descriptive name is helpful.

## 14. Testing functions with a driver

A **driver** is code that calls a function with different inputs to check its behavior, including invalid inputs and edge cases.

```python
def say_hi(name):
    return "Hello " + name + "!"

# Example driver calls
print(say_hi("Moses"))
print(say_hi(""))
# print(say_hi())       # missing required argument: TypeError
# print(say_hi(1))      # TypeError: int + str
# print(say_hi("A", "B"))  # too many arguments: TypeError
```

Test at least:
- A normal input.
- An empty input if it is possible.
- Boundary cases.
- Invalid types or missing/extra arguments, where relevant.

The lecture mentions `unittest` as Python's built-in unit-testing framework, and also lists `pytest`, `Nose2`, `doctest`, `coverage`, `Hypothesis`, `Selenium`, and `Tox` as other tools.

## 15. Good coding practices from the lecture

- **DRY** — Don't Repeat Yourself. Use a function or loop when code is repeated.
- **Abstraction** — use functions, modules, classes, and scripts to make the main workflow easier to understand.
- Give functions descriptive names.
- Keep each function focused on a specific task.
- Test functions with appropriate inputs, including incorrect ones.
- Avoid unnecessary changes to global variables.
- Avoid mutable default arguments.

## Quick reference

| Concept | Meaning |
|---|---|
| `def name(...):` | Define a function |
| `name(...)` | Call a function |
| `return value` | Send a value back and end the function |
| `print(value)` | Display a value; does not return it |
| `param=value` | Default argument |
| `name=value` in a call | Keyword argument |
| `*args` | Extra positional arguments as a tuple |
| `**kwargs` | Extra keyword arguments as a dictionary |
| Local variable | Name defined inside a function |
| Global variable | Name defined outside functions |
| `global x` | Declare that assignments to `x` refer to the global name |
| Mutable object | Can be changed in place, e.g. list or dictionary |
| Immutable object | Cannot be changed in place, e.g. int, str, tuple |
| Closure | Inner function retains access to enclosing variables |
| Recursion | A function calls itself |
| `lambda` | Short anonymous function expression |

## One-minute mental model

1. `def` defines a function; calling it runs it.
2. Arguments pass information in; `return` passes a result back.
3. A function without `return` gives back `None`.
4. A function can mutate a passed-in list, so changes may be visible outside it.
5. Use `None` instead of `[]` as a default when a fresh list is needed per call.
6. Variables inside a function are local unless explicitly declared global for assignment.
7. Nested functions can access enclosing variables.
8. Test functions with normal and unusual inputs.

---

**Source:** BINP16 Lecture 5 – Functions PDF and the accompanying `Lecture 5.py` examples. Optional topics (`*args`/`**kwargs`, recursion, and lambda) are marked as optional because the lecture labels them that way.
