# Conda + Python — Ubuntu & VS Code Cheat Sheet

## 1. What is Conda?

**Conda** manages isolated environments for Python and other software.

An **environment** is a separate workspace with its own:
- Python version
- installed packages
- package versions
- dependencies

Example:

```text
Miniconda
├── base
├── bioinfo       → Python 3.12 + bioinformatics packages
└── project2     → different Python/packages
```

This lets different projects use different software versions without interfering with each other.

---

## 2. Start Conda in Ubuntu Terminal

### Check that Conda is available

```bash
conda --version
```

### See available environments

```bash
conda env list
```

The `*` marks the currently active environment.

Example:

```text
# conda environments:
#
base                 *   /home/vaiva/miniconda3
bioinfo                   /home/vaiva/miniconda3/envs/bioinfo
```

### Activate an environment

```bash
conda activate bioinfo
```

The prompt changes from:

```text
(base) vaiva@Lenovo:~$
```

to:

```text
(bioinfo) vaiva@Lenovo:~$
```

That means `bioinfo` is active.

### Check which Python is being used

```bash
python --version
which python
```

Example:

```text
Python 3.12.15
/home/vaiva/miniconda3/envs/bioinfo/bin/python
```

### Start Python

```bash
python
```

Example:

```python
print("Hello!")
x = 10
print(x * 2)
```

Exit Python with:

```python
exit()
```

or `Ctrl+D`.

### Run a Python script

```bash
python script.py
```

### Deactivate the environment

```bash
conda deactivate
```

This takes you back to the previous environment, usually `base`.

---

## 3. If `conda` is not found

If you get:

```text
Command 'conda' not found
```

and Conda is already installed, reload your Bash configuration:

```bash
source ~/.bashrc
```

Then:

```bash
conda --version
```

`source ~/.bashrc` tells the current Bash shell to read and execute the commands in `~/.bashrc`. Conda's shell initialization is normally configured there.

---

## 4. Start Conda Python in VS Code

Assumption: **VS Code, the WSL extension, and the Python extension are already installed.**

Because Conda is installed inside Ubuntu/WSL, VS Code should be connected to **WSL: Ubuntu**.

### Step 1 — Connect VS Code to Ubuntu/WSL

In VS Code:

```text
Ctrl + Shift + P
```

Search for:

```text
WSL: Connect to WSL
```

Select your Ubuntu distribution.

The bottom-left of VS Code should show something similar to:

```text
WSL: Ubuntu
```

### Step 2 — Open your project

From Ubuntu:

```bash
cd ~/python_project
code .
```

Or open the project folder from VS Code while connected to WSL.

### Step 3 — Select the Conda Python interpreter

In VS Code:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Select the interpreter belonging to your Conda environment, for example:

```text
Python 3.12.15 ('bioinfo')
/home/vaiva/miniconda3/envs/bioinfo/bin/python
```

VS Code will then use that environment for the project.

### Step 4 — Verify

Create `test.py`:

```python
import sys

print(sys.executable)
print("Hello from Python!")
```

Run it.

You should see the Conda environment's Python path, for example:

```text
/home/vaiva/miniconda3/envs/bioinfo/bin/python
Hello from Python!
```

---

## 5. Create a new environment

Create an environment with a specific Python version:

```bash
conda create -n myproject python=3.12
```

Then activate it:

```bash
conda activate myproject
```

Check it:

```bash
python --version
```

You can create environments for different projects:

```bash
conda create -n project1 python=3.12
conda create -n project2 python=3.11
```

They can have different Python/package versions.

---

## 6. Install packages into an environment

First activate the environment:

```bash
conda activate bioinfo
```

Then install a package:

```bash
conda install numpy
```

Multiple packages:

```bash
conda install numpy pandas matplotlib
```

You can also install packages with `pip`:

```bash
pip install package_name
```

Check installed packages:

```bash
conda list
```

Check one package:

```bash
conda list numpy
```

> Install packages while the intended environment is active so they go into that environment.

---

## 7. Useful environment commands

| Command | What it does |
|---|---|
| `conda env list` | List environments |
| `conda activate bioinfo` | Activate an environment |
| `conda deactivate` | Deactivate current environment |
| `conda create -n NAME python=3.12` | Create an environment |
| `conda list` | List installed packages |
| `conda install PACKAGE` | Install a package |
| `conda remove PACKAGE` | Remove a package |
| `conda update PACKAGE` | Update a package |
| `python --version` | Check Python version |
| `which python` | Show which Python executable is active |

---

## 8. Clone an environment

Create a copy of an existing environment:

```bash
conda create -n newenv --clone bioinfo
```

Then:

```bash
conda activate newenv
```

Useful when you want to experiment without changing the original environment.

---

## 9. Export an environment

Save an environment's configuration:

```bash
conda env export > environment.yml
```

This creates:

```text
environment.yml
```

A more minimal export based on packages explicitly requested during environment creation is:

```bash
conda env export --from-history > environment.yml
```

Keep this file with your project so the environment setup can be recreated later.

---

## 10. Recreate an environment from `environment.yml`

If a project contains:

```text
environment.yml
```

create the environment with:

```bash
conda env create -f environment.yml
```

Then activate it:

```bash
conda activate ENVIRONMENT_NAME
```

This is useful when moving a project to another computer or sharing its environment setup.

---

## 11. Remove an environment

If you no longer need an environment:

```bash
conda deactivate
conda env remove -n myproject
```

Check:

```bash
conda env list
```

---

## 12. Useful project workflow

A typical Python project can look like:

```text
my_project/
├── environment.yml
├── README.md
├── script.py
└── data/
```

Start working:

```bash
cd ~/my_project
conda activate myproject
code .
```

Check Python:

```bash
python --version
which python
```

Run your program:

```bash
python script.py
```

When finished:

```bash
conda deactivate
```

---

## 13. Quick start — Ubuntu

For an existing environment:

```bash
source ~/.bashrc
conda activate bioinfo
python --version
```

Then:

```bash
python
```

or:

```bash
python script.py
```

---

## 14. Quick start — VS Code + WSL

```text
VS Code
   ↓
WSL: Ubuntu
   ↓
Python: Select Interpreter
   ↓
bioinfo
   ↓
/home/vaiva/miniconda3/envs/bioinfo/bin/python
```

Typical workflow:

```bash
conda activate bioinfo
cd ~/my_project
code .
```

Then in VS Code:

```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ Python 3.12 ('bioinfo')
```

---

## Key idea

**Conda environment = isolated software setup for a project.**

You normally:

```bash
conda activate ENVIRONMENT
```

→ work with Python and packages

```bash
conda deactivate
```

→ leave the environment

Always check that the correct environment is active before installing packages or running your code.
