# BINP16 — Lecture 11: Python Linting and Clean Code
## Git Cheat Sheet

Based on the uploaded `06-python-linting.pptx` slides and `06-python-linting-explained.md` notes.

---

## 1. Why clean code matters

Clean code is easier to read, debug, maintain, and share with collaborators. Python tooling can help by checking style, sorting imports, finding likely bugs, and checking type annotations.

The lecture introduces these tools:

| Tool | Main purpose |
|---|---|
| **Black** | Automatically formats code consistently |
| **isort** | Organises imports |
| **Ruff** | Fast linting and automatic fixes; can also format code |
| **mypy** | Checks type hints and catches many type-related mistakes |

The supporting notes focus on a Ruff + mypy workflow. Ruff can cover formatting and import sorting too, so you may not need to run Black and isort separately if your project standardises on Ruff.

## 2. The three-step daily routine

The slide deck's workflow is to format code, check/fix lint issues, then check types. In the supplied notes, the recommended routine is:

```bash
make ruff-fix
make typecheck
```

This assumes the project has a `Makefile` with the targets shown below.

- `ruff-fix`: automatically fix supported lint issues, then format.
- `typecheck`: run mypy to check type annotations and type usage.

If you do not have the Makefile targets yet, use the direct commands:

```bash
ruff check --fix .
ruff format .
mypy .
```

## 3. Install the tools

Run these commands in the Python environment you use for your project:

```bash
python -m pip install --upgrade ruff
python -m pip install --upgrade mypy
```

Optional tools shown in the lecture:

```bash
python -m pip install --upgrade black isort
```

Check that a tool is installed:

```bash
ruff --version
mypy --version
```

## 4. Ruff: linting, formatting, and fixing

**Linting** means checking code for likely mistakes and rule violations. Ruff is a fast Python linter and can automatically fix many findings.

### Main commands

| Command | What it does |
|---|---|
| `ruff check .` | Reports lint findings; does not edit files |
| `ruff check --fix .` | Applies available automatic lint fixes |
| `ruff format .` | Formats code |
| `ruff clean` | Clears Ruff's cache |

Run these from the project root, where `.` means the current directory and its supported Python files.

**Remember:** automatic fixes cannot safely resolve every issue. Review the changes and manually fix anything Ruff leaves behind.

### Ruff examples

```python
import os
import pandas as pd  # unused import if never used

def count_genes(genes):
    total = 0
    for gene in genes:
        total += 1
    return total
```

Possible improvements include removing unused imports and adding type annotations if your project requires them:

```python
def count_genes(genes: list[str]) -> int:
    return len(genes)
```

## 5. Configure Ruff with `pyproject.toml`

`pyproject.toml` is a project configuration file. The notes provide this example:

```toml
[tool.ruff]
line-length = 100
target-version = "py311"
src = ["src", "tests"]
extend-exclude = ["build", "dist", ".venv", ".mypy_cache", ".pytest_cache"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true
docstring-code-line-length = "dynamic"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "C4", "SIM", "RUF"]

[tool.ruff.lint.isort]
known-first-party = ["your_package_name"]
combine-as-imports = true
force-sort-within-sections = true
```

### Important settings

- `line-length = 100`: configured line length.
- `target-version = "py311"`: target Python 3.11 for relevant checks and fixes.
- `extend-exclude`: folders to ignore.
- `quote-style = "double"`: prefer double quotes when formatting.
- `indent-style = "space"`: use spaces for indentation.
- `select`: enables groups of lint rules.
- `known-first-party`: replace `your_package_name` with your actual package name.

Rule groups in the supplied notes:

| Group | General purpose |
|---|---|
| `E` | Style and whitespace checks |
| `F` | Common errors such as unused imports and undefined names |
| `I` | Import sorting |
| `UP` | Modernise Python syntax |
| `B` | Common bug patterns |
| `C4` | Improve comprehensions |
| `SIM` | Simplify code |
| `RUF` | Ruff-specific checks |

## 6. isort and import order

Imports are conventionally grouped in this order:

1. Python standard library
2. Third-party packages
3. Your own project/package

Example:

```python
import re
from pathlib import Path

import pandas as pd
from Bio import SeqIO

from bioseq.dna import gc_content
```

`isort` organises imports into a consistent order. Ruff's `I` rule family can also check and fix import ordering.

## 7. mypy: static type checking

**mypy** checks whether code is consistent with type annotations. It can catch many mistakes before you run the program, but it does not prove the program is free of all bugs.

### Add type annotations

```python
def gc_content(sequence: str) -> float:
    gc = sequence.upper().count("G") + sequence.upper().count("C")
    return 100 * gc / len(sequence)
```

- `sequence: str` means the argument is expected to be a string.
- `-> float` documents the expected return type.

### Common mypy errors

| Error code | Meaning |
|---|---|
| `[arg-type]` | An argument has an incompatible type |
| `[return-value]` | A function returns an incompatible type |
| `[assignment]` | A value is assigned to a variable with an incompatible type |
| `[call-arg]` | A call has the wrong arguments |
| `[attr-defined]` | An attribute is not known on that object/type |
| `[name-defined]` | A name is undefined or out of scope |
| `[index]` / `[operator]` | An indexing or operator operation is not valid for the type |

### Install and run

```bash
python -m pip install --upgrade mypy
mypy .
```

### Example configuration

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_unused_configs = true
warn_return_any = true
warn_redundant_casts = true
warn_unused_ignores = true
no_implicit_optional = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
show_error_codes = true
pretty = true

[mypy-tests.*]
disallow_untyped_defs = false
```

`strict = true` enables a set of stricter checks. This can be useful for a project, but may be demanding for a beginner's first script; you can introduce strict checks gradually if needed.

## 8. Makefile: automate repeat commands

A `Makefile` lets you name common commands so you do not need to remember or type each one every time.

Example based on the supplied notes:

```make
RUFF ?= ruff
MYPY ?= mypy

.PHONY: ruff-format ruff-check ruff-fix ruff-clean mypy typecheck qa

ruff-format:
	$(RUFF) format .

ruff-check:
	$(RUFF) check .

ruff-fix:
	$(RUFF) check --fix .
	$(RUFF) format .

ruff-clean:
	$(RUFF) clean

mypy:
	$(MYPY) .

typecheck: mypy

qa: ruff-fix mypy
```

**Makefile reminder:** the command lines under each target must start with a real tab, not spaces.

Run the targets from the project root:

```bash
make ruff-check
make ruff-format
make ruff-fix
make typecheck
make qa
```

`qa` runs the `ruff-fix` and `mypy` targets in order.

## 9. Useful Python habits from the supporting notes

### Avoid mutable default arguments

Do not use an empty list as a default argument when the function will modify it. Use `None` and create a fresh list inside the function.

```python
def collect_gene(gene: str, acc: list[str] | None = None) -> list[str]:
    if acc is None:
        acc = []
    acc.append(gene)
    return acc
```

### Catch specific exceptions

```python
try:
    count = int(row["reads"])
except KeyError as e:
    raise KeyError("CSV missing 'reads' column") from e
except ValueError as e:
    raise ValueError(f"Bad integer: {row['reads']}") from e
```

Catch the error you expect rather than using a broad `except:` without a good reason. `raise ... from e` preserves the original exception as the cause.

### Close resources with `with`

```python
from pathlib import Path

path = Path("samples.csv")
with path.open(encoding="utf-8") as handle:
    for line in handle:
        print(line.rstrip())
```

The `with` block closes the file when the block exits.

### Equality vs. identity

```python
if sample is None:
    return

if status == "PASS":
    print("Passed")
```

- `==` compares values.
- `is` checks whether two references are the same object; use it for singletons such as `None`.

### Avoid shadowing built-in names

Avoid names such as `list`, `sum`, `id`, or `map` for your own variables/classes. These names already refer to built-ins.

```python
genes = ["BRCA1", "TP53"]
gene_count = len(genes)
```

### Pandas: avoid chained assignment

```python
# Risky
# df[df["tpm"] > 1]["status"] = "EXPRESSED"

# Safer: select a copy, then assign
expressed = df.loc[df["tpm"] > 1].copy()
expressed.loc[:, "status"] = "EXPRESSED"

# Or assign directly to rows of the original DataFrame
df.loc[df["tpm"] <= 1, "status"] = "LOW"
```

### Large data: process in chunks

```python
import pandas as pd

total = 0
for chunk in pd.read_csv(
    "counts.tsv",
    sep="\\t",
    chunksize=200_000,
    dtype={"gene": "string", "count": "Int64"},
):
    total += (chunk["count"] > 0).sum()

print("nonzero rows:", total)
```

Chunking can reduce memory use when reading large tables.

### Compare floating-point numbers safely

```python
from math import isclose

if isclose(tpm, 0.0, abs_tol=1e-9):
    print("Approximately zero")
```

Floating-point calculations may have small rounding differences.

### Use logging in reusable code

```python
import logging

log = logging.getLogger(__name__)
log.info("Loaded %d samples", len(samples))
```

Logging is more configurable than using `print()` for status messages in libraries and pipelines.

### Run external programs safely

```python
import subprocess as sp

sp.run(
    ["samtools", "view", "-b", "in.sam", "-o", "out.bam"],
    check=True,
)
```

Passing arguments as a list avoids shell parsing. `check=True` raises an error if the command exits unsuccessfully.

## 10. Naming conventions

| Item | Convention | Example |
|---|---|---|
| Functions and variables | `snake_case` | `load_config`, `total_count` |
| Classes and exceptions | `PascalCase` | `FastQueue`, `ParseError` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT` |
| Modules/packages | Short, lowercase | `utils.py`, `mypackage` |
| Internal helper | Leading underscore | `_serialize_user()` |

Avoid hardcoding “magic numbers” or strings throughout logic. Prefer named constants or configuration values.

## 11. Future annotations

The notes recommend placing this at the top of new modules:

```python
from __future__ import annotations
```

It can help with forward references in type hints and reduce some annotation-related import complications. It is useful with Python 3.11/3.12, though it is not required in every file.

## 12. PEPs mentioned in the notes

- **PEP 8:** Python style guide — naming, whitespace, imports and line length.
- **PEP 257:** docstring conventions.
- **PEP 20:** The Zen of Python. Run `python -c "import this"` to see it.
- **PEP 484 / 526 / 544:** type hints, variable annotations and protocols.

## 13. A few Ruff rules to recognise

| Rule | What it flags in the supplied notes |
|---|---|
| `F401` | Unused import |
| `F841` | Assigned variable is never used |
| `B006` | Mutable default argument |
| `UP` | Opportunities to modernise Python syntax |
| `SIM` | Code that can be simplified |
| `C4` | Comprehension improvements |

The notes also discuss builtin-shadowing rules such as `A001` and `A002`. Exact rule availability and names depend on Ruff configuration/version, so check the reported rule identifier if it differs in your environment.

## 14. Quick workflow checklist

1. Edit your Python code.
2. Run `ruff check --fix .` to apply supported lint fixes.
3. Run `ruff format .` to format.
4. Run `mypy .` to check types.
5. Fix remaining issues manually and rerun the checks.
6. Consider adding tests with `pytest` as a next step.

```bash
ruff check --fix .
ruff format .
mypy .
```

---

## Source materials

This cheat sheet is based on the uploaded `06-python-linting.pptx` slide deck and `06-python-linting-explained.md` supporting notes. The detailed Ruff configuration, mypy settings, Makefile targets, and everyday Python rules come from the Markdown notes; the slides introduce Black, isort, Ruff, mypy, `pyproject.toml`, and the daily workflow.
