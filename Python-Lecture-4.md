# BINP16 Python --- Lecture 4 Cheat Sheet: File Handling

> Lund University --- BINP16 Bioinformatics: Programming in Python ---
> Lecture 4, October 2026

## 1. User input

`input()` always returns a string:

``` python
name = input("What is your name? ")
```

Convert when a number is needed:

``` python
number = int(input("Enter a number: "))
number = float(input("Enter a number: "))
```

Handle invalid numbers:

``` python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

### Avoid dangerous input execution

Do **not** use:

``` python
eval(input())
```

The lecture warns against dangerous functions including:

``` python
eval()
exec()
os.system()
subprocess.call(..., shell=True)
```

------------------------------------------------------------------------

## 2. File formats

Python can read and write files. The lecture focuses on plain text
files.

Common bioinformatics formats mentioned:

-   FASTA --- nucleotide/protein sequences
-   VCF --- variant information
-   XML --- tagged/structured data
-   PLINK `.bim` --- tab-delimited data

A file may contain one record per line, often with a header. Another
common structure uses delimiters such as tabs.

**Important:** your code should understand the input format and be
flexible enough to handle changes.

------------------------------------------------------------------------

# 3. Opening files

Basic syntax:

``` python
f = open(filename, mode)
```

Modes:

  Mode    Meaning
  ------- ------------------------------
  `"r"`   read
  `"w"`   write / overwrite
  `"a"`   append
  `"x"`   create; error if file exists
  `"b"`   binary
  `"t"`   text

Examples:

``` python
f = open("file.txt", "r")
f = open("file.txt", "w")
f = open("file.txt", "a")
```

### Preferred: `with`

``` python
with open("file.txt", "r") as f:
    data = f.read()
```

The file is automatically closed when leaving the `with` block.

Without `with`:

``` python
f = open("file.txt", "r")
data = f.read()
f.close()
```

------------------------------------------------------------------------

# 4. Reading files

## `read()`

Reads the entire file as one string:

``` python
with open("file.txt") as f:
    data = f.read()
```

Good for small files; avoid loading huge files unnecessarily.

## `readline()`

Reads one line:

``` python
with open("file.txt") as f:
    line = f.readline()
```

At end-of-file it returns an empty string.

A common pattern:

``` python
f = open("file.txt")

line = f.readline()
while line:
    print(line)
    line = f.readline()

f.close()
```

## `readlines()`

Reads all lines into a list:

``` python
with open("file.txt") as f:
    lines = f.readlines()
```

Example result:

``` python
["ACAGC\n", "TAGCA\n", "TCGAT\n"]
```

Like `read()`, it loads the whole file.

## Loop directly over a file

Usually preferred for large files:

``` python
with open("file.txt") as f:
    for line in f:
        print(line)
```

------------------------------------------------------------------------

# 5. Newlines and whitespace

Lines read from files normally contain `\n`.

Remove it:

``` python
line.rstrip()
```

or:

``` python
line.strip("\n")
```

Useful debugging:

``` python
print(repr(line))
```

`repr()` makes hidden characters such as `\n` visible.

------------------------------------------------------------------------

# 6. Whitespace-separated files

Use:

``` python
data = line.split()
```

Example:

``` text
1 rs123 0 742429 A G
```

becomes:

``` python
["1", "rs123", "0", "742429", "A", "G"]
```

Example from the lecture:

``` python
r = open("bim.txt")
header = r.readline()

pos_vec = []

for line in r:
    data = line.split()
    chr, SNP, temp, pos, a1, a2 = data
    pos_vec.append(int(pos))

r.close()

print(len(pos_vec))
```

For comma-separated data:

``` python
line.split(",")
```

For tab-separated data:

``` python
line.split("\t")
```

------------------------------------------------------------------------

# 7. FASTA files

FASTA stores nucleotide or protein sequences.

A FASTA record begins with `>`:

``` text
>sequence_1
ATGCGATCGATC
>sequence_2
GGCTACGATGCA
```

Test for a header:

``` python
if line.startswith(">"):
```

FASTA sequences can span multiple lines, so sequence fragments must be
concatenated.

------------------------------------------------------------------------

# 8. Reading FASTA files

Lecture pattern:

``` python
r = open("Fasta_example_3_seq.txt", "r")

seq = []
temp = ""

for line in r:
    if line.startswith(">"):
        if temp:
            seq.append(temp)
        temp = ""
    else:
        temp += line.rstrip()

if temp:
    seq.append(temp)

r.close()

print(seq)
```

### Logic

``` text
new header
    ↓
save previous sequence
    ↓
reset temp

sequence line
    ↓
add fragment to temp

end of file
    ↓
save final sequence
```

The final:

``` python
if temp:
    seq.append(temp)
```

is needed because there is no next header to trigger saving the last
sequence.

------------------------------------------------------------------------

# 9. FASTA: `+=` vs `join()`

For short sequences:

``` python
temp = ""

for line in r:
    temp += line.rstrip()
```

For long sequences, the lecture recommends a list plus `join()`:

``` python
pieces = []

for line in r:
    pieces.append(line.rstrip())

temp = ''.join(pieces)
```

Why?

Repeated `+=` can repeatedly create/copy strings. A list allows the
final string to be constructed once.

### `join()`

``` python
''.join(pieces)       # no separator
'\t'.join(fields)     # tab-separated
'\n'.join(lines)      # newline-separated
```

The string before `.join()` is the separator.

------------------------------------------------------------------------

# 10. Checking files

Use `os.path` to check input:

``` python
import os

filename = "Fasta_example_3_seq.txt"

if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")
```

For FASTA, also consider checking:

-   headers start with `>`
-   sequence lines contain appropriate nucleotide/protein codes

------------------------------------------------------------------------

# 11. Command-line arguments

Run a script:

``` bash
python programfile.py inputFile.txt
```

Use `sys.argv`:

``` python
import sys

PythonScriptName = sys.argv[0]
DataScriptName = sys.argv[1]

print("Python script name:", PythonScriptName)
print("Input file name:", DataScriptName)
```

Important:

``` python
sys.argv[0]  # script name
sys.argv[1]  # first argument
sys.argv[2]  # second argument
```

Loop through arguments:

``` python
import sys

for arg in sys.argv:
    print(arg)
```

Or with indexes:

``` python
for i, arg in enumerate(sys.argv):
    print(i, arg)
```

### File-reading script pattern

``` python
import sys

script_name = sys.argv[0]
filename = sys.argv[1]

print("Python script name:", script_name)
print("Input file name:", filename)

with open(filename, "r") as f:
    content = f.read()

print("\nContent of the input file:")
print(content)
```

------------------------------------------------------------------------

# 12. Writing files

Open for writing:

``` python
with open("filename.txt", "w") as f:
    f.write("Hello\n")
```

`write()` expects a string:

``` python
f.write(str(2022))
```

Append:

``` python
with open("filename.txt", "a") as f:
    f.write("Another line\n")
```

### `writelines()`

Writes a list of strings:

``` python
lines = ["line 1\n", "line 2\n"]

with open("filename.txt", "w") as f:
    f.writelines(lines)
```

`writelines()` does **not** automatically add newlines.

------------------------------------------------------------------------

# 13. `%` formatting for output

Basic specifiers:

  Format   Meaning
  -------- -----------------------------------
  `%s`     string / string representation
  `%d`     integer
  `%f`     floating point
  `%.2f`   float with 2 digits after decimal
  `%x`     hexadecimal, lowercase
  `%X`     hexadecimal, uppercase

Example:

``` python
name = "Daniel"
age = 5

line = "%s is %d years old." % (name, age)
```

------------------------------------------------------------------------

# 14. Writing a FASTA file

The lecture uses `enumerate()` to write sequence characters and insert a
newline every 60 characters.

``` python
fileObj = open("FASTA_write.txt", "w")

fileObj.write("> %s\n" % comment)

for n, code in enumerate(sequence):
    if n > 0 and n % 60 == 0:
        fileObj.write("\n")
    fileObj.write(code)

if n % 60 != 0:
    fileObj.write("\n")

fileObj.close()
```

### `enumerate()`

Gives the index and character:

``` python
for n, code in enumerate(sequence):
    print(n, code)
```

Conceptually:

``` text
0 A
1 G
2 C
3 G
...
```

`n % 60 == 0` detects multiples of 60.

------------------------------------------------------------------------

# 15. Column-delimited files

PLINK `.bim` is used as an example of a tab-delimited file.

``` python
data = [
    ['chr1', 'rs121', 0, 100, '1', '1'],
    ['chr2', 'rs111', 0, 101, '2', '3']
]

heading = ['chr', 'rs#', 'cM', 'Pos', 'Allele1', 'Allele2']

formats = ['%s', '%s', '%d', '%d', '%c', '%c']

separator = '\t'
```

Build the header:

``` python
line = separator.join(heading)
fileobj.write('%s\n' % line)
```

Build a format string:

``` python
format_string = separator.join(formats)
```

Write each row:

``` python
for row in data:
    line = format_string % tuple(row)
    fileobj.write('%s\n' % line)
```

The lecture specifically converts each list row to a tuple because the
old-style `%` operator is used with multiple values.

------------------------------------------------------------------------

# 16. `os` and `os.path`

``` python
import os
```

  Python                    Linux idea   Purpose
  ------------------------- ------------ ----------------------
  `os.getcwd()`             `pwd`        current directory
  `os.chdir(path)`          `cd`         change directory
  `os.listdir(path)`        `ls`         list contents
  `os.makedirs(...)`        `mkdir -p`   create directories
  `os.rmdir(path)`          `rmdir`      remove directory
  `os.remove(path)`         `rm`         remove file
  `os.rename(src, dst)`     `mv`         rename/move
  `os.path.exists(path)`    ---          path exists?
  `os.path.isfile(path)`    ---          regular file?
  `os.path.isdir(path)`     ---          directory?
  `os.path.join(...)`       ---          join path components
  `os.path.dirname(path)`   ---          containing directory

Examples:

``` python
import os

print(os.getcwd())
print(os.listdir("."))

os.chdir("/path/to/directory")

if os.path.exists("file.txt"):
    print("File exists")

if os.path.isfile("file.txt"):
    print("It is a file")

if os.path.isdir("Data"):
    print("It is a directory")
```

Build paths with:

``` python
path = os.path.join("Data", "reads.txt")
```

Rename/move:

``` python
os.rename("old.txt", "new.txt")
```

Remove:

``` python
os.remove("file.txt")
```

------------------------------------------------------------------------

# 17. Debugging file code

The lecture recommends:

1.  Read the traceback and line number.
2.  Use `print()` to inspect variables.
3.  Use the REPL/interactive session to test individual commands.
4.  Reduce the input file to a small example.
5.  Use a debugger and breakpoints.
6.  Search documentation/Stack Overflow when appropriate.
7.  Ask the teacher after thinking through the problem.

Useful checks:

``` python
print(os.getcwd())
print(filename)
print(os.path.exists(filename))
print(repr(line))
print(type(data))
```

### Debugging mindset

Ask:

``` text
Does the file exist?
Is the path correct?
Am I in the expected working directory?
Did I use the correct file mode?
What type did the function return?
Does the file actually have the format I expect?
Are there hidden newlines/whitespace?
Did I accidentally process the header?
Are the delimiters correct?
Is the input valid?
```

------------------------------------------------------------------------

# 18. Common patterns

### Read a small file

``` python
with open("file.txt") as f:
    data = f.read()
```

### Process a large file line-by-line

``` python
with open("file.txt") as f:
    for line in f:
        line = line.rstrip()
        # process line
```

### Write

``` python
with open("file.txt", "w") as f:
    f.write("line 1\n")
```

### Append

``` python
with open("file.txt", "a") as f:
    f.write("line 2\n")
```

### Check existence

``` python
import os

if os.path.exists("file.txt"):
    print("File exists")
```

### FASTA header

``` python
if line.startswith(">"):
```

### Split columns

``` python
fields = line.split()
```

### Join sequence fragments

``` python
sequence = ''.join(pieces)
```

------------------------------------------------------------------------

# 19. High-yield comparison

  Function/pattern         Result
  ------------------------ -------------------------------------
  `f.read()`               whole file as one string
  `f.readline()`           one line as a string
  `f.readlines()`          all lines as a list
  `for line in f`          one line at a time
  `f.write(s)`             writes one string
  `f.writelines(lines)`    writes a list of strings
  `line.rstrip()`          removes trailing whitespace/newline
  `line.split()`           splits whitespace-separated fields
  `''.join(pieces)`        combines strings without separator
  `'\t'.join(fields)`      combines fields with tabs
  `line.startswith(">")`   tests for FASTA header

------------------------------------------------------------------------

# 20. One-page mental model

``` text
INPUT
  |
  +-- input() -----------------> string
  |                                |
  |                                +-- int()/float() if needed
  |
FILE
  |
  +-- open(filename, mode)
          |
          +-- r = read
          +-- w = write/overwrite
          +-- a = append
          +-- x = create
          |
          +-- with open(...) as f:
                  |
                  +-- read()       -> whole string
                  +-- readline()   -> one line
                  +-- readlines()  -> list of lines
                  +-- for line in f -> line-by-line
                  |
                  +-- write()      -> string
                  +-- writelines() -> list of strings

FASTA
  |
  +-- line.startswith(">") -> header
  |
  +-- otherwise -> sequence fragment
                         |
                         +-- list.append()
                         +-- ''.join()

COLUMN FILE
  |
  +-- line.split() -> fields
  |
  +-- process fields
  |
  +-- '\t'.join(fields) -> tab-delimited output

COMMAND LINE
  |
  +-- python program.py input.txt
          |
          +-- sys.argv[0] -> script
          +-- sys.argv[1] -> input file

FILESYSTEM
  |
  +-- os.getcwd()
  +-- os.chdir()
  +-- os.listdir()
  +-- os.path.exists()
  +-- os.path.isfile()
  +-- os.path.isdir()
  +-- os.path.join()
  +-- os.rename()
  +-- os.remove()
```

------------------------------------------------------------------------

# 21. Exam / exercise checklist

-   [ ] Explain `input()` and convert its result with `int()` /
    `float()`.
-   [ ] Explain why `eval(input())` is unsafe.
-   [ ] Open files with `open()`.
-   [ ] Know `r`, `w`, `a`, and `x`.
-   [ ] Prefer `with open(...)`.
-   [ ] Know `read()`, `readline()`, and `readlines()`.
-   [ ] Loop through files line-by-line.
-   [ ] Remove `\n` with `rstrip()`.
-   [ ] Split whitespace/tab-delimited data.
-   [ ] Recognize FASTA headers.
-   [ ] Read multi-line FASTA sequences.
-   [ ] Use a list + `join()` for long sequence construction.
-   [ ] Use `sys.argv`.
-   [ ] Write text with `write()` and `writelines()`.
-   [ ] Write FASTA output using `enumerate()`.
-   [ ] Create tab-delimited output.
-   [ ] Use `os` / `os.path` for file operations.
-   [ ] Debug using traceback, `print()`, `repr()`, REPL, and small test
    files.

------------------------------------------------------------------------

## Key takeaways

1.  Use `with open(...)` for normal file handling.
2.  Prefer line-by-line processing for large files.
3.  `read()` gives one large string; `readlines()` gives a list.
4.  FASTA headers begin with `>`.
5.  FASTA sequences may span multiple lines.
6.  Use list + `join()` when building long sequences.
7.  `sys.argv` provides command-line arguments.
8.  `write()` takes strings; `writelines()` takes a list of strings.
9.  `os` / `os.path` provide file and directory operations.
10. Validate input and debug with small, controlled examples.

------------------------------------------------------------------------

## Source

Based on **BINP16 Bioinformatics: Programming in Python --- Lecture 4:
File handling**, Lund University, October 2026. The lecture covers user
input, file formats, reading/writing files, FASTA handling, command-line
arguments, debugging, and standard-library file operations.
