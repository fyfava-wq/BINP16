# BINP16 — Python Lecture 7: Modules and Packages Cheat Sheet

Based on *Lecture 7: Python Modules* (October 2026) and `Lecture7.Modules.py`.

## 1. Function vs module vs package vs library

| Term | Meaning | Example |
|---|---|---|
| **Function** | Reusable block of code for a specific task | `gc_content(sequence)` |
| **Module** | A Python file (`.py`) containing related functions, classes, variables, or executable statements | `dna.py` |
| **Package** | A way to organize related modules, typically in a directory | `bioseq/` |
| **Library** | A collection of reusable modules and/or packages | Biopython |

Example structure:

```text
bioseq/
├── __init__.py
├── dna.py
└── protein.py
```

- `dna.py`: DNA sequence analysis functions.
- `protein.py`: protein sequence analysis functions.
- `__init__.py`: package initializer; an empty file is enough for the lecture's example and marks the directory as a package.

## 2. Three categories of modules and packages

| Category | Examples | Installation |
|---|---|---|
| Python standard library | `math`, `statistics`, `os`, `sys`, `random` | Included with Python |
| Third-party packages | `numpy`, `pandas`, `biopython`, `matplotlib` | Install separately |
| User-defined modules/packages | `dna.py`, `protein.py`, `bioseq` | Create them in your project |

## 3. Importing modules

### Import a whole module — recommended default

```python
import math

print(math.sqrt(25))  # 5.0
print(math.pi)
```

Use `module_name.function_name()` or `module_name.constant`.

**Why?** It makes it clear where a function comes from and reduces naming conflicts.

### Import a module with an alias

```python
import math as m

print(m.sqrt(25))  # 5.0
print(m.pi)
```

Common aliases:

```python
import numpy as np
import pandas as pd
```

### Import a specific function or class

```python
from math import sqrt
print(sqrt(25))  # 5.0

from math import sqrt, factorial
print(factorial(5))  # 120
```

Only the named items are imported into the current namespace.

### Avoid wildcard imports

```python
from math import *
```

This imports many public names directly into the current namespace. It can overwrite names and make it harder to tell where a function came from. Prefer `import math` or `from math import specific_name`.

### Common mistake

```python
import math
sqrt(25)       # NameError: sqrt is not imported directly
math.sqrt(25)  # Correct
```

If you instead use `from math import sqrt`, then `sqrt(25)` works, but `math.sqrt(25)` requires that `math` itself has also been imported.

## 4. Standard-library examples

```python
import math
import statistics
import os

print(math.sqrt(25))                  # 5.0
print(statistics.mean([10, 20, 30])) # 20
print(os.getcwd())                    # Current working directory
```

Useful reminder:
- `math`: mathematical functions and constants.
- `statistics`: statistical calculations.
- `os`: operating-system interactions, including working-directory information.
- `sys`: Python interpreter and command-line information.
- `random`: random values and selections.

## 5. Third-party packages: install, then import

**Important:** installing a package and importing it are two separate steps. Install it into the environment in which you will run Python.

### Install with pip

```bash
python -m pip install numpy pandas biopython
```

### Or install with Conda

```bash
conda activate bioinfo
conda install -c conda-forge numpy pandas biopython
```

### Import and use NumPy

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(data)          # [10 20 30 40 50]
print(np.mean(data)) # 30.0
print(np.std(data))  # Standard deviation
print(np.max(data))  # 50
print(np.min(data))  # 10
```

Because the module was imported as `np`, use `np.array(...)`, not `array(...)` or `numpy.array(...)`.

### Import and use Pandas

```python
import pandas as pd

values = pd.Series([10, 20, 30])
print(values.mean())  # 20.0
```

### Check the active Python and installed packages

```bash
conda activate bioinfo
conda list
conda list numpy
python -c "import sys; print(sys.executable)"
conda env list
```

`sys.executable` shows the exact Python executable being used.

## 6. Conda environments

A Conda environment is an isolated workspace with a specific Python version and the packages a project needs.

### Why use separate environments?

- Avoid changing the system Python installation and its packages.
- Reduce conflicts between package versions.
- Use different Python versions for different projects.
- Make computational analyses more reproducible.

### Common commands

```bash
# Create environments
conda create -n bioinformatics python=3.12
conda create -n machine_learning python=3.10

# Activate an environment
conda activate bioinformatics

# Leave the active environment
conda deactivate

# List environments
conda env list
```

**Good practice:** keep project dependencies in the corresponding project environment instead of installing everything into `base`.

### Conda channels

A channel is a location/repository from which Conda downloads packages. Examples:

- `defaults`: the default Anaconda channel.
- `conda-forge`: a large community-driven channel with packages and software from several programming languages.
- `bioconda`: specialized for bioinformatics software and biological data analysis, including tools such as `bowtie2`, `STAR`, `samtools`, and `bcftools`.

Example:

```bash
conda install -c conda-forge numpy pandas biopython
```

## 7. Export and recreate an environment

An environment YAML file helps recreate an environment on another computer.

### Export (computer 1)

```bash
conda activate bioinformatics
conda env export --from-history > environment.yml
```

`--from-history` exports the packages explicitly requested in the environment, rather than the complete resolved package list.

### Recreate (computer 2)

Copy `environment.yml` to the second computer, then run:

```bash
conda env create -f environment.yml
conda activate bioinformatics
conda list
```

Keep `environment.yml` with the project when others need to reproduce the environment.

## 8. Biopython: DNA sequence operations

### Import the `Seq` class

```python
from Bio.Seq import Seq

dna = Seq("ATGCGCATTA")

print(dna)                       # ATGCGCATTA
print(dna.complement())          # TACGCGTAAT
print(dna.reverse_complement())  # TAATGCGCAT
```

`Seq` is a class imported from the `Bio.Seq` module, which belongs to the `Bio` package.

### Transcribe and translate

```python
from Bio.Seq import Seq as BioSeq

dna = BioSeq("ATGGCTTTT")

print("DNA:", dna)                    # ATGGCTTTT
print("RNA:", dna.transcribe())       # AUGGCUUUU
print("Protein:", dna.translate())    # MAF
```

### Read sequence files with `SeqIO`

```python
from Bio import SeqIO
# Optional alias:
from Bio import SeqIO as sio
```

`SeqIO` is a Biopython module for reading and writing sequence files, including FASTA and GenBank formats.

### Distinguish package, module, and class

```python
from Bio.Seq import Seq
```

- `Bio`: package
- `Bio.Seq`: module
- `Seq`: class

The lecture notes that `from Bio import Seq` is not the same import and may fail because there is no `Bio.Seq` module object named `Seq` in that position.

## 9. Build your own package

### Directory structure

```text
project/
└── bioseq/
    ├── __init__.py
    ├── dna.py
    └── protein.py
```

Steps:
1. Create the `bioseq` directory.
2. Create `dna.py` and `protein.py`.
3. Put related functions in the appropriate module.
4. Give functions clear documentation (docstrings).
5. Create an empty `__init__.py` inside `bioseq`.

Example imports (run from the directory containing `bioseq/`):

```python
import bioseq.dna as BioDNA
import bioseq.protein as BioProtein
```

Then call a function with its module alias:

```python
print(BioDNA.name_nucleotide("A"))
print(BioDNA.name_nucleotide("g"))
print(BioDNA.name_nucleotide("X"))
```

The lecture's example outputs are `Adenine`, `Guanine`, and `Unknown nucleotide`, respectively.

## 10. Inspect your own modules

```python
# List names available in the module
print(dir(BioDNA))

# Display documentation
help(BioDNA.gc_content)
print(BioDNA.gc_content.__doc__)

# Module metadata
print(BioDNA.__file__)     # File path of the imported module
print(BioDNA.__name__)     # e.g. 'bioseq.dna'
print(BioDNA.__package__)  # e.g. 'bioseq'

# Check whether a named attribute exists
print(hasattr(BioDNA, "gc_content"))     # True
print(hasattr(BioDNA, "protein_class"))  # False
```

### List functions defined in a module

```python
import inspect

functions = inspect.getmembers(BioDNA, inspect.isfunction)

for name, function in functions:
    print(name)
```

The lecture's example lists:
- `gc_content`
- `mol_weight_nucleotide`
- `name_nucleotide`

`inspect.getmembers(..., inspect.isfunction)` returns `(name, function)` pairs for functions it identifies in the module.

## 11. Quick reference

| Goal | Code/command |
|---|---|
| Import a module | `import math` |
| Use a module function | `math.sqrt(25)` |
| Import one function | `from math import sqrt` |
| Alias a module | `import numpy as np` |
| Install packages with pip | `python -m pip install numpy pandas biopython` |
| Install packages with Conda | `conda install -c conda-forge numpy pandas biopython` |
| Create environment | `conda create -n bioinformatics python=3.12` |
| Activate environment | `conda activate bioinformatics` |
| List environments | `conda env list` |
| Export environment | `conda env export --from-history > environment.yml` |
| Recreate environment | `conda env create -f environment.yml` |
| Import Biopython sequence class | `from Bio.Seq import Seq` |
| Import sequence I/O module | `from Bio import SeqIO` |
| Inspect module names | `dir(BioDNA)` |
| Read a docstring | `BioDNA.gc_content.__doc__` |
| Find imported module file | `BioDNA.__file__` |

## Key takeaways

- A **module** is a `.py` file; a **package** organizes modules in a directory.
- Prefer explicit imports such as `import math` and `import numpy as np`; avoid `from module import *`.
- Install third-party packages in the same environment that runs your code.
- Use separate Conda environments for separate projects.
- Export an `environment.yml` to help make a project reproducible.
- Biopython's `Seq` class provides useful sequence operations, and `SeqIO` handles sequence-file formats.
- Organize your own reusable bioinformatics functions into documented modules and packages.
