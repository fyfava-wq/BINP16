# BINP16 Python Function Lookup

> **Purpose:** a fast `Ctrl+F` index of functions, built-ins, methods, and common library calls appearing in the Python lecture notes. Search by goal or function name, then select **More** to jump to the relevant section in that lecture's companion notes.

## How to use this lookup

- Press **Ctrl+F** and search for what you want to do (`read a file`, `sort`, `regex`, `plot`, `train model`) or the function name (`read_csv`, `findall`, `enumerate`).
- **More** links jump to the closest relevant heading in the corresponding lecture notes in this repository.
- The uploaded ZIP contains Markdown lecture notes/cheat sheets, not the original slide PDFs. Therefore, links below point to the closest available lecture-note section; they cannot link to exact slide numbers.
- Some entries are methods (`text.strip()`), constructors (`DataFrame(...)`), or statements (`break`, `return`), not standalone functions. They are included because they are things you look up while coding.
- `x`, `items`, `df`, `plt`, etc. are placeholders for your own variable/object names.

## Quick finder by goal

- **Ask the user for input:** `input()`
- **Display output:** `print()`
- **Convert text to a number:** `int(x) / float(x) / str(x)`
- **Count items or characters:** `len(x)`
- **Search text:** `s.find(sub) / s.index(sub) / re.search(pattern, text)`
- **Replace text:** `s.replace(old, new) / re.sub(pattern, repl, text)`
- **Split text into pieces:** `s.split(sep) / re.split(pattern, text)`
- **Join strings:** `sep.join(items)`
- **Loop with indexes:** `enumerate(items)`
- **Pair two lists:** `zip(a, b)`
- **Sort values:** `sorted(items) / items.sort()`
- **Add/remove list items:** `items.append(x) / items.remove(x) / items.pop(i)`
- **Safely read a dictionary key:** `d.get(key, default)`
- **Read a file:** `open(path, mode) / f.read() / f.readline()`
- **Write a file:** `f.write(text) / f.writelines(lines)`
- **Check a path:** `os.path.exists(path) / Path(path)`
- **Parse a FASTA file:** `SeqIO.parse(handle, format)`
- **Work with DNA sequences:** `dna.complement() / dna.reverse_complement() / dna.transcribe() / dna.translate()`
- **Find regex matches:** `re.findall(pattern, text) / re.finditer(pattern, text)`
- **Load a table:** `pd.read_csv(path) / pd.read_table(path)`
- **Summarise a DataFrame:** `df.describe() / df.groupby(keys) / df.agg(func)`
- **Combine tables:** `pd.merge(left, right, ...) / pd.concat(frames)`
- **Create a plot:** `plt.bar(x, y) / plt.scatter(x, y) / plt.hist(x)`
- **Train and use an ML model:** `model.fit(X, y) / model.predict(X)`
- **Evaluate a classifier:** `accuracy_score(...) / precision_score(...) / recall_score(...) / confusion_matrix(...)`
- **Inspect a module:** `dir(object) / help(object) / inspect.getmembers(obj)`
- **Run external software:** `subprocess.run(args, ...)`
- **Compare floating-point values:** `math.isclose(a, b)`

---

## Complete lookup by lecture

### Lecture 1 — Types, numbers, strings

| Search for | Use it when… | More |
|---|---|---|
| `print()` | Display text or values in the output. | [More](Python-Lecture-1-Data_Types.md#14-print) |
| `type(x)` | Find the type of a value or variable. | [More](Python-Lecture-1-Data_Types.md#3-data-types) |
| `int(x)` | Convert a value to an integer. | [More](Python-Lecture-1-Data_Types.md#18-converting-data-types) |
| `float(x)` | Convert a value to a decimal number. | [More](Python-Lecture-1-Data_Types.md#18-converting-data-types) |
| `str(x)` | Convert a value to a string. | [More](Python-Lecture-1-Data_Types.md#18-converting-data-types) |
| `len(x)` | Count items or characters. | [More](Python-Lecture-1-Data_Types.md#8-strings) |
| `exit()` | Leave the interactive Python interpreter. | [More](Python-Lecture-1-Data_Types.md#1-running-python) |
| `s.find(sub)` | Find a substring; returns -1 if absent. | [More](Python-Lecture-1-Data_Types.md#10-string-membership-and-searching) |
| `s.index(sub)` | Find a substring; raises ValueError if absent. | [More](Python-Lecture-1-Data_Types.md#10-string-membership-and-searching) |
| `s.count(sub)` | Count occurrences of a substring. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.lower()` | Convert text to lowercase. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.upper()` | Convert text to uppercase. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.capitalize()` | Capitalize the first character of text. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.replace(old, new)` | Replace occurrences of one substring with another. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.strip()` | Remove whitespace from both ends. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.lstrip() / s.rstrip()` | Remove whitespace from the left / right end. | [More](Python-Lecture-1-Data_Types.md#11-useful-string-methods) |
| `s.split(sep)` | Split a string into a list of pieces. | [More](Python-Lecture-1-Data_Types.md#12-concatenating-and-joining-strings) |
| `sep.join(items)` | Join strings using a separator. | [More](Python-Lecture-1-Data_Types.md#12-concatenating-and-joining-strings) |
| `math.sqrt(x)` | Calculate a square root. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |
| `math.log10(x)` | Calculate the base-10 logarithm. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |
| `random.random()` | Generate a random float from 0 up to 1. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |
| `random.randrange(...)` | Choose a random integer from a range. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |
| `random.choice(items)` | Choose one random item. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |
| `random.shuffle(items)` | Shuffle a list in place. | [More](Python-Lecture-1-Data_Types.md#6-importing-modules) |

### Lecture 2 — Collections

| Search for | Use it when… | More |
|---|---|---|
| `list(iterable)` | Create a list from an iterable. | [More](Python-Lecture-2-Collection_Data_Types.md#2-lists) |
| `tuple(iterable)` | Create an immutable tuple. | [More](Python-Lecture-2-Collection_Data_Types.md#4-tuples) |
| `set(iterable)` | Create a set of unique items. | [More](Python-Lecture-2-Collection_Data_Types.md#5-sets) |
| `len(x)` | Count items in a collection. | [More](Python-Lecture-2-Collection_Data_Types.md#6-common-sequence-operations) |
| `range(start, stop, step)` | Generate a sequence of integers, often for loops. | [More](Python-Lecture-2-Collection_Data_Types.md#6-common-sequence-operations) |
| `sorted(items)` | Return a new sorted list; original is unchanged. | [More](Python-Lecture-2-Collection_Data_Types.md#sort-vs-sorted) |
| `items.sort()` | Sort a list in place; returns None. | [More](Python-Lecture-2-Collection_Data_Types.md#sort-vs-sorted) |
| `items.append(x)` | Add one item to the end of a list. | [More](Python-Lecture-2-Collection_Data_Types.md#list-modification) |
| `items.extend(iterable)` | Add each item from an iterable to a list. | [More](Python-Lecture-2-Collection_Data_Types.md#list-modification) |
| `items.insert(i, x)` | Insert an item at a chosen index. | [More](Python-Lecture-2-Collection_Data_Types.md#insert) |
| `items.remove(x)` | Remove the first matching value. | [More](Python-Lecture-2-Collection_Data_Types.md#remove-vs-pop) |
| `items.pop(i)` | Remove and return an item by index (last by default). | [More](Python-Lecture-2-Collection_Data_Types.md#remove-vs-pop) |
| `items.clear()` | Remove all items from a list. | [More](Python-Lecture-2-Collection_Data_Types.md#list-modification) |
| `items.reverse()` | Reverse a list in place. | [More](Python-Lecture-2-Collection_Data_Types.md#list-modification) |
| `items.copy()` | Make a shallow copy of a list or collection. | [More](Python-Lecture-2-Collection_Data_Types.md#3-lists-and-references) |
| `items.count(x)` | Count occurrences of a value. | [More](Python-Lecture-2-Collection_Data_Types.md#6-common-sequence-operations) |
| `items.index(x)` | Find the index of a value. | [More](Python-Lecture-2-Collection_Data_Types.md#6-common-sequence-operations) |
| `s.add(x)` | Add an item to a set. | [More](Python-Lecture-2-Collection_Data_Types.md#5-sets) |
| `s.remove(x)` | Remove an item from a set; errors if missing. | [More](Python-Lecture-2-Collection_Data_Types.md#5-sets) |
| `d.get(key, default)` | Read a dictionary value safely; can return a default. | [More](Python-Lecture-2-Collection_Data_Types.md#10-get-and-setdefault) |
| `d.setdefault(key, default)` | Return a value; add the key with default if missing. | [More](Python-Lecture-2-Collection_Data_Types.md#10-get-and-setdefault) |
| `d.keys()` | View dictionary keys. | [More](Python-Lecture-2-Collection_Data_Types.md#11-dictionary-keys-values-and-items) |
| `d.values()` | View dictionary values. | [More](Python-Lecture-2-Collection_Data_Types.md#11-dictionary-keys-values-and-items) |
| `d.items()` | View dictionary key–value pairs. | [More](Python-Lecture-2-Collection_Data_Types.md#11-dictionary-keys-values-and-items) |
| `zip(a, b)` | Pair items from iterables position by position. | [More](Python-Lecture-2-Collection_Data_Types.md#15-zip) |
| `format(...) / '{}'.format(x)` | Insert values into a formatted string. | [More](Python-Lecture-2-Collection_Data_Types.md#14-format-output-formatting) |

### Lecture 3 — Control flow, loops, exceptions

| Search for | Use it when… | More |
|---|---|---|
| `input(prompt)` | Ask the user for input; returns a string. | [More](Python-Lecture-3-Loops.md#35-example-invalid-input) |
| `bool(x)` | Convert a value to True or False. | [More](Python-Lecture-3-Loops.md#5-truth-values) |
| `range(...)` | Generate integers for a loop. | [More](Python-Lecture-3-Loops.md#14-for-with-range) |
| `enumerate(items)` | Loop over items with their index. | [More](Python-Lecture-3-Loops.md#26-enumerate) |
| `break` | Exit the nearest loop immediately (statement, not function). | [More](Python-Lecture-3-Loops.md#22-break) |
| `continue` | Skip to the next loop iteration (statement). | [More](Python-Lecture-3-Loops.md#23-continue) |
| `pass` | Do nothing; placeholder statement. | [More](Python-Lecture-3-Loops.md#24-pass) |
| `raise Exception(...)` | Raise an error deliberately. | [More](Python-Lecture-3-Loops.md#33-raise) |
| `sys.exit()` | Exit the program via SystemExit. | [More](Python-Lecture-3-Loops.md#39-exiting-a-program) |
| `os._exit(code)` | Immediately terminate the process; bypasses normal cleanup. | [More](Python-Lecture-3-Loops.md#39-exiting-a-program) |

### Lecture 4 — Files, input/output, operating system

| Search for | Use it when… | More |
|---|---|---|
| `open(path, mode)` | Open a file for reading, writing, or appending. | [More](Python-Lecture-4-File_Handling.md#3-opening-files) |
| `input(prompt)` | Read a line from the user as text. | [More](Python-Lecture-4-File_Handling.md#1-user-input) |
| `int(x) / float(x) / str(x)` | Convert user or file text to numeric/string types. | [More](Python-Lecture-4-File_Handling.md#1-user-input) |
| `f.read()` | Read all remaining file content (or a specified number of characters). | [More](Python-Lecture-4-File_Handling.md#4-reading-files) |
| `f.readline()` | Read one line from a file. | [More](Python-Lecture-4-File_Handling.md#4-reading-files) |
| `f.readlines()` | Read remaining lines into a list. | [More](Python-Lecture-4-File_Handling.md#4-reading-files) |
| `f.write(text)` | Write a string to a file. | [More](Python-Lecture-4-File_Handling.md#12-writing-files) |
| `f.writelines(lines)` | Write an iterable of strings; does not add newlines automatically. | [More](Python-Lecture-4-File_Handling.md#12-writing-files) |
| `f.close()` | Close a file handle; usually prefer `with open(...)`. | [More](Python-Lecture-4-File_Handling.md#3-opening-files) |
| `line.strip() / line.rstrip()` | Remove surrounding or trailing whitespace/newlines. | [More](Python-Lecture-4-File_Handling.md#5-newlines-and-whitespace) |
| `line.split(sep)` | Split a line into columns or fields. | [More](Python-Lecture-4-File_Handling.md#6-whitespace-separated-files) |
| `sep.join(parts)` | Join strings into one output string. | [More](Python-Lecture-4-File_Handling.md#9-fasta-+-vs-join) |
| `enumerate(items)` | Get each item and its index while looping. | [More](Python-Lecture-4-File_Handling.md#14-writing-a-fasta-file) |
| `os.getcwd()` | Get the current working directory. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.chdir(path)` | Change the working directory. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.listdir(path)` | List names in a directory. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.remove(path)` | Delete a file. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.rename(src, dst)` | Rename or move a filesystem path. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.path.exists(path)` | Check whether a path exists. | [More](Python-Lecture-4-File_Handling.md#10-checking-files) |
| `os.path.isfile(path)` | Check whether a path is a file. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.path.isdir(path)` | Check whether a path is a directory. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `os.path.join(a, b)` | Build a path using the correct separator. | [More](Python-Lecture-4-File_Handling.md#16-os-and-ospath) |
| `subprocess.call(...)` | Run an external command; check the lecture's safety notes. | [More](Python-Lecture-4-File_Handling.md#additional-material-from-lecture-4py) |
| `urlopen(url)` | Open a URL for reading in the XML example. | [More](Python-Lecture-4-File_Handling.md#xml) |
| `etree.XML(text)` | Parse XML text into an element tree. | [More](Python-Lecture-4-File_Handling.md#xml) |

### Lecture 5 — Defining and using functions

| Search for | Use it when… | More |
|---|---|---|
| `def name(...)` | Define a reusable function (syntax, not a function call). | [More](Python-Lecture-5-Functions.md#1-what-is-a-function) |
| `return value` | Send a result back to the caller (statement). | [More](Python-Lecture-5-Functions.md#2-parameters-arguments-and-return-values) |
| `abs(x)` | Return the absolute value of a number. | [More](Python-Lecture-5-Functions.md#5-avoid-overwriting-built-in-function-names) |
| `sequence.replace(old, new)` | Replace characters or substrings in a sequence string. | [More](Python-Lecture-5-Functions.md#11-reverse-complement-of-dna-or-rna) |
| `str.maketrans(...)` | Build a translation table for character substitution. | [More](Python-Lecture-5-Functions.md#11-reverse-complement-of-dna-or-rna) |
| `sequence.translate(table)` | Apply a character-translation table. | [More](Python-Lecture-5-Functions.md#11-reverse-complement-of-dna-or-rna) |
| `param.append(x)` | Append an item to a list parameter. | [More](Python-Lecture-5-Functions.md#6-mutable-and-immutable-objects-passed-to-functions) |
| `param.copy()` | Copy a list before passing it if mutation should be avoided. | [More](Python-Lecture-5-Functions.md#6-mutable-and-immutable-objects-passed-to-functions) |
| `lambda args: expression` | Create a small anonymous function. | [More](Python-Lecture-5-Functions.md#13-lambda-functions-optional) |

### Lecture 6 — Regular expressions (`re`)

| Search for | Use it when… | More |
|---|---|---|
| `re.search(pattern, text)` | Find the first match anywhere in the text. | [More](Python-Lecture-6-RE.md#2-the-main-re-functions) |
| `re.match(pattern, text)` | Check for a match at the start of the text. | [More](Python-Lecture-6-RE.md#2-the-main-re-functions) |
| `re.findall(pattern, text)` | Return all non-overlapping matches as a list. | [More](Python-Lecture-6-RE.md#2-the-main-re-functions) |
| `re.finditer(pattern, text)` | Iterate over match objects for all matches. | [More](Python-Lecture-6-RE.md#3-match-objects-and-positions) |
| `re.sub(pattern, repl, text)` | Replace matches with replacement text. | [More](Python-Lecture-6-RE.md#11-replacing-with-resub) |
| `re.split(pattern, text)` | Split text wherever the regex matches. | [More](Python-Lecture-6-RE.md#12-splitting-strings) |
| `re.compile(pattern)` | Compile a pattern for repeated use. | [More](Python-Lecture-6-RE.md#13-compile-and-reuse-a-pattern) |
| `match.group(n)` | Get the full match or a captured group. | [More](Python-Lecture-6-RE.md#8-groups-group-and-groups) |
| `match.groups()` | Get all captured groups as a tuple. | [More](Python-Lecture-6-RE.md#8-groups-group-and-groups) |
| `match.start() / match.end()` | Get the start / end index of a match. | [More](Python-Lecture-6-RE.md#3-match-objects-and-positions) |
| `match.span()` | Get the (start, end) indices of a match. | [More](Python-Lecture-6-RE.md#3-match-objects-and-positions) |
| `text.split(sep)` | Split on a literal separator, not a regex pattern. | [More](Python-Lecture-6-RE.md#12-splitting-strings) |
| `text.rsplit(sep)` | Split from the right side. | [More](Python-Lecture-6-RE.md#12-splitting-strings) |
| `text.splitlines()` | Split text into lines. | [More](Python-Lecture-6-RE.md#12-splitting-strings) |
| `text.find(sub) / text.replace(a, b)` | Simple substring search or replacement without regex. | [More](Python-Lecture-6-RE.md#12-splitting-strings) |

### Lecture 7 — Modules, packages, inspection, Biopython

| Search for | Use it when… | More |
|---|---|---|
| `help(object)` | Display built-in documentation for an object. | [More](Python-Lecture-7-Modules.md#10-inspect-your-own-modules) |
| `dir(object)` | List names/attributes available on an object or module. | [More](Python-Lecture-7-Modules.md#10-inspect-your-own-modules) |
| `hasattr(obj, name)` | Check whether an object has a named attribute. | [More](Python-Lecture-7-Modules.md#10-inspect-your-own-modules) |
| `inspect.getmembers(obj)` | List members of an object or module. | [More](Python-Lecture-7-Modules.md#10-inspect-your-own-modules) |
| `os.getcwd()` | Show the current working directory. | [More](Python-Lecture-7-Modules.md#4-standard-library-examples) |
| `math.sqrt(x) / math.factorial(x)` | Square root / factorial from the math module. | [More](Python-Lecture-7-Modules.md#4-standard-library-examples) |
| `statistics.mean(items)` | Calculate the arithmetic mean. | [More](Python-Lecture-7-Modules.md#4-standard-library-examples) |
| `np.array(items)` | Create a NumPy array. | [More](Python-Lecture-7-Modules.md#5-third-party-packages-install-then-import) |
| `np.mean(x) / np.std(x)` | Calculate mean / standard deviation with NumPy. | [More](Python-Lecture-7-Modules.md#5-third-party-packages-install-then-import) |
| `np.max(x) / np.min(x)` | Find maximum / minimum with NumPy. | [More](Python-Lecture-7-Modules.md#5-third-party-packages-install-then-import) |
| `Seq(sequence)` | Create a Biopython sequence object. | [More](Python-Lecture-7-Modules.md#8-biopython-dna-sequence-operations) |
| `dna.complement()` | Return the complementary DNA sequence. | [More](Python-Lecture-7-Modules.md#8-biopython-dna-sequence-operations) |
| `dna.reverse_complement()` | Return the reverse-complement sequence. | [More](Python-Lecture-7-Modules.md#8-biopython-dna-sequence-operations) |
| `dna.transcribe()` | Convert a DNA sequence to RNA. | [More](Python-Lecture-7-Modules.md#8-biopython-dna-sequence-operations) |
| `dna.translate()` | Translate a nucleotide sequence to amino acids. | [More](Python-Lecture-7-Modules.md#8-biopython-dna-sequence-operations) |
| `SeqIO.parse(handle, format)` | Iterate through sequences in a file such as FASTA. | [More](Python-Lecture-7-Modules.md#read-sequence-files-with-seqio) |
| `pd.Series(data) / pd.DataFrame(data)` | Create a Pandas Series / DataFrame. | [More](Python-Lecture-7-Modules.md#5-third-party-packages-install-then-import) |

### Lecture 8 — NumPy, Pandas, Matplotlib

| Search for | Use it when… | More |
|---|---|---|
| `np.array(data)` | Create an array for numerical or sequence data. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#2-numpy-arrays) |
| `np.arange(start, stop, step)` | Create regularly spaced values using a step. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#create-ranges-of-values) |
| `np.linspace(start, stop, num)` | Create a fixed number of evenly spaced values. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#create-ranges-of-values) |
| `np.unique(x)` | Return unique values (optionally with counts). | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#count-dna-bases-and-calculate-gc-percentage) |
| `np.ndim(x)` | Get the number of array dimensions. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#dimensions-shape-and-size) |
| `x.reshape(...)` | Change an array's shape without changing its data. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#reshape) |
| `np.sum(x) / np.mean(x)` | Calculate sum / mean. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#count-dna-bases-and-calculate-gc-percentage) |
| `np.argmax(x)` | Return the index of the maximum value. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#count-dna-bases-and-calculate-gc-percentage) |
| `pd.read_csv(path)` | Read a comma-separated file into a DataFrame. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#read-and-write-files) |
| `pd.read_table(path)` | Read a tab-delimited file into a DataFrame. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#read-and-write-files) |
| `pd.DataFrame(data)` | Create a table-like DataFrame. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#series-and-dataframe) |
| `df.head(n)` | Preview the first rows. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#4-inspect-summarize-and-sort-a-dataframe) |
| `df.describe()` | Summarize numeric columns statistically. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#4-inspect-summarize-and-sort-a-dataframe) |
| `df.astype(dtype)` | Convert a column or object to a chosen data type. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#5-data-types) |
| `df.select_dtypes(...)` | Select columns by data type. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#5-data-types) |
| `df.isnull()` | Mark missing values. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#7-missing-values-duplicates-and-string-cleaning) |
| `df.drop_duplicates()` | Remove duplicate rows. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#7-missing-values-duplicates-and-string-cleaning) |
| `df.groupby(keys)` | Group rows for summaries or aggregation. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#8-grouping-and-aggregation) |
| `df.agg(func)` | Apply one or more aggregation functions. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#8-grouping-and-aggregation) |
| `df.apply(func, axis=...)` | Apply a function along rows or columns. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#9-transform-data-with-functions-apply-map-and-replace) |
| `df.map(func)` | Map values through a function/dictionary (Series). | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#map-replace-and-assign) |
| `df.replace(old, new)` | Replace selected values. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#map-replace-and-assign) |
| `df.assign(...)` | Return a DataFrame with added or changed columns. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#map-replace-and-assign) |
| `pd.merge(left, right, ...)` | Combine tables using matching key columns. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#10-combine-dataframes-merge-join-concat) |
| `df.join(other)` | Combine tables, commonly by index. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#10-combine-dataframes-merge-join-concat) |
| `pd.concat(frames)` | Stack or align DataFrames/Series. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#10-combine-dataframes-merge-join-concat) |
| `pd.to_datetime(values)` | Convert values to datetime objects. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#7-missing-values-duplicates-and-string-cleaning) |
| `plt.figure()` | Create a new figure. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |
| `plt.bar(x, y)` | Draw a bar chart. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#bar-plot) |
| `plt.scatter(x, y)` | Draw a scatter plot. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#scatter-plot) |
| `plt.hist(x)` | Draw a histogram. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#histogram) |
| `plt.xlabel(text) / plt.ylabel(text)` | Label plot axes. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |
| `plt.title(text)` | Add a plot title. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |
| `plt.tight_layout()` | Adjust spacing so plot elements fit. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |
| `plt.savefig(path)` | Save a plot to a file. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |
| `plt.show()` | Display the plot. | [More](Python-Lecture-8-NumPy-Pandas-Matplotlib.md#12-plot-with-matplotlib) |

### Lecture 9 — Machine learning functions

| Search for | Use it when… | More |
|---|---|---|
| `train_test_split(X, y, ...)` | Split data into training and test sets. | [More](Python-Lecture-9-AI-fundamentals.md#5-classification) |
| `StandardScaler()` | Create a scaler to standardize features. | [More](Python-Lecture-9-AI-fundamentals.md#6-preparing-and-scaling-data) |
| `scaler.fit_transform(X)` | Learn scaling parameters and transform training data. | [More](Python-Lecture-9-AI-fundamentals.md#6-preparing-and-scaling-data) |
| `scaler.transform(X)` | Apply learned scaling to new/test data. | [More](Python-Lecture-9-AI-fundamentals.md#6-preparing-and-scaling-data) |
| `LinearRegression()` | Create a linear regression model. | [More](Python-Lecture-9-AI-fundamentals.md#4-regression) |
| `LogisticRegression()` | Create a logistic classification model. | [More](Python-Lecture-9-AI-fundamentals.md#5-classification) |
| `model.fit(X, y)` | Train a model on features and target values. | [More](Python-Lecture-9-AI-fundamentals.md#4-regression) |
| `model.predict(X)` | Predict target values or class labels. | [More](Python-Lecture-9-AI-fundamentals.md#4-regression) |
| `model.predict_proba(X)` | Predict class probabilities for supported classifiers. | [More](Python-Lecture-9-AI-fundamentals.md#5-classification) |
| `KMeans()` | Create a K-means clustering model. | [More](Python-Lecture-9-AI-fundamentals.md#7-unsupervised-clustering-k-means) |
| `kmeans.fit_predict(X)` | Fit K-means and return cluster labels. | [More](Python-Lecture-9-AI-fundamentals.md#7-unsupervised-clustering-k-means) |
| `PCA()` | Create a principal component analysis transformer. | [More](Python-Lecture-9-AI-fundamentals.md#8-dimensionality-reduction-pca) |
| `pca.fit_transform(X)` | Fit PCA and return transformed coordinates. | [More](Python-Lecture-9-AI-fundamentals.md#8-dimensionality-reduction-pca) |
| `np.where(condition, a, b)` | Choose values based on a condition. | [More](Python-Lecture-9-AI-fundamentals.md#5-classification) |
| `np.exp(x) / np.tanh(x)` | Calculate exponential / hyperbolic tangent elementwise. | [More](Python-Lecture-9-AI-fundamentals.md#10-neural-networks-and-activation-functions) |
| `accuracy_score(y_true, y_pred)` | Calculate the fraction of correct predictions. | [More](Python-Lecture-9-AI-fundamentals.md#9-evaluate-classification) |
| `precision_score(...)` | Measure how many positive predictions are correct. | [More](Python-Lecture-9-AI-fundamentals.md#9-evaluate-classification) |
| `recall_score(...)` | Measure how many actual positives were found. | [More](Python-Lecture-9-AI-fundamentals.md#9-evaluate-classification) |
| `confusion_matrix(y_true, y_pred)` | Count true/false positives and negatives by class. | [More](Python-Lecture-9-AI-fundamentals.md#9-evaluate-classification) |

### Lecture 10 — Object-oriented programming

| Search for | Use it when… | More |
|---|---|---|
| `__init__(self, ...)` | Initialise a new object; called during construction. | [More](Python-Lecture-10-OOP.md#7-special-methods) |
| `super()` | Access methods from a parent class, often in __init__. | [More](Python-Lecture-10-OOP.md#3-inheritance) |
| `__del__(self)` | Finalizer called when an object is being destroyed; timing is not reliable. | [More](Python-Lecture-10-OOP.md#7-special-methods) |
| `object.describe() / object.reproduce()` | Example instance methods defined by a class. | [More](Python-Lecture-10-OOP.md#1-what-is-object-oriented-programming-oop) |
| `object.get_...() / object.set_...()` | Example getter/setter methods to read or validate attributes. | [More](Python-Lecture-10-OOP.md#5-encapsulation) |

### Lecture 11 — Linting, typing, safe utilities

| Search for | Use it when… | More |
|---|---|---|
| `Path(path)` | Create a pathlib path object. | [More](Python-Lecture-11-Linting.md#9-useful-python-habits-from-the-supporting-notes) |
| `path.open(...)` | Open a file using a Path object. | [More](Python-Lecture-11-Linting.md#9-useful-python-habits-from-the-supporting-notes) |
| `line.rstrip()` | Remove trailing whitespace/newline from a line. | [More](Python-Lecture-11-Linting.md#9-useful-python-habits-from-the-supporting-notes) |
| `pd.read_csv(path)` | Load tabular data into Pandas. | [More](Python-Lecture-11-Linting.md#pandas-avoid-chained-assignment) |
| `math.isclose(a, b)` | Compare floating-point numbers with a tolerance. | [More](Python-Lecture-11-Linting.md#compare-floating-point-numbers-safely) |
| `logging.getLogger(name)` | Get a logger for recording program events. | [More](Python-Lecture-11-Linting.md#use-logging-in-reusable-code) |
| `log.info(message)` | Write an informational log message. | [More](Python-Lecture-11-Linting.md#use-logging-in-reusable-code) |
| `subprocess.run(args, ...)` | Run an external program with configurable safety options. | [More](Python-Lecture-11-Linting.md#run-external-programs-safely) |
| `len(x)` | Check the number of items (also useful in validation). | [More](Python-Lecture-11-Linting.md#9-useful-python-habits-from-the-supporting-notes) |
| `sum(x)` | Add numeric items. | [More](Python-Lecture-11-Linting.md#9-useful-python-habits-from-the-supporting-notes) |

---

## Important distinctions

| If you need to… | Use | Remember |
|---|---|---|
| Sort a list in place | `items.sort()` | Changes the original list; returns `None`. |
| Get a sorted copy | `sorted(items)` | Returns a new list; original remains unchanged. |
| Find literal text | `text.find(sub)` | Returns `-1` if absent. |
| Find literal text and require it to exist | `text.index(sub)` | Raises `ValueError` if absent. |
| Find a regex match anywhere | `re.search(pattern, text)` | Returns one match object or `None`. |
| Check a regex match at the start | `re.match(pattern, text)` | Does not search later in the string. |
| Read a file safely | `with open(path) as f:` | The file closes automatically when the block ends. |
| Add one list item | `items.append(x)` | Appends `x` as one item. |
| Add items from an iterable | `items.extend(xs)` | Extends the list with each item from `xs`. |
| Get a dictionary value without a missing-key error | `d.get(key, default)` | Does not add the key. |
| Apply scaling to test data | `scaler.transform(X_test)` | Reuse training-set scaling parameters; do not fit on the test set. |

## Scope and completeness

This index covers the Python Lecture 1–11 Markdown cheat sheets included in `BINP16-main.zip`. It collects the built-ins, string/list/dictionary methods, file and OS functions, regex functions, module/inspection calls, NumPy/Pandas/Matplotlib calls, machine-learning API calls, and OOP methods explicitly shown in those notes. It is a practical lookup, not a list of every function in the Python language or every API in each library.

For exact slide-number links, the original lecture slide PDFs (or exported slide text with page/slide markers) would need to be added to the repository.
