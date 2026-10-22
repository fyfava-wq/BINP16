# BINP16 — Lecture 8: NumPy, Pandas and Matplotlib Cheat Sheet

Study notes based on the uploaded Lecture 8 Pandas slides, `Lecture_8_Pandas_notebook.ipynb`, and the NumPy/Pandas/Matplotlib exercises and solutions. Examples follow the material's focus on data manipulation, expression tables, and visualization.

## 1. Import the libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

- **NumPy (`np`)**: arrays and numerical operations.
- **Pandas (`pd`)**: labelled data structures and table manipulation.
- **Matplotlib (`plt`)**: plots and figures.

Install if needed (use your project's active environment):

```bash
conda install -c conda-forge numpy pandas matplotlib
# Alternative using pip:
python -m pip install numpy pandas matplotlib
```

## 2. NumPy arrays

### Create arrays

```python
values = [20.1, 20.8, 21.9, 22.5]
C = np.array(values)

# A character array from a DNA sequence
sequence = "ATGGCCCTG"
bases = np.array(list(sequence))
```

Unlike a regular Python list, a NumPy array supports vectorized numerical operations:

```python
celsius = np.array([20.1, 20.8, 21.9])
fahrenheit = celsius * 9 / 5 + 32
```

### Dimensions, shape and size

```python
x = np.array(42)                         # 0-D scalar array
one_d = np.array([1, 2, 3])              # 1-D
matrix = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D

np.ndim(matrix)   # number of dimensions: 2
matrix.shape      # rows and columns: (2, 3)
matrix.size       # total elements: 6
len(matrix)       # size of first dimension: 2
```

### Create ranges of values

```python
np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
np.arange(0.5, 3.0, 0.5)         # stop is excluded
np.linspace(1, 10, 5)            #  [1., 3.25, 5.5 , 7.75, 10.] 5 evenly spaced values including endpoints
np.linspace(1, 10, 5, endpoint=False)
```

- `np.arange(start, stop, step)` uses a step size; `stop` is excluded.
- `np.linspace(start, stop, num)` chooses a number of evenly spaced values; the endpoint is included by default.

### Indexing and slicing

Python/NumPy indexing starts at zero. Slice stop positions are excluded.

```python
a = np.array([3, 8, 12, 18, 7, 11, 30])
a[0]       # first element: 3
a[3]       # fourth element: 18
a[:3]      # first three elements
a[-1]      # last element
a[::-1]    # reversed array
```

For 2-D arrays, use `[rows, columns]`:

```python
A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55],
])

A[2, 1]       # row 3, column 2 -> 32
A[:3, 2:]     # first 3 rows, from column index 2 onward
A[3:, :]      # rows from index 3 onward, all columns
A[:, 4:]      # all rows, last column
A[::2, ::3]   # every second row and every third column
```

### Reshape

```python
x = np.arange(18)
x.reshape(3, 6)  # 3 rows x 6 columns; total element count must remain 18
x.reshape(3, -1) # 3 rows and calculates how many columns are needed
x.T              # transpose
x.flatten()      # makes 1D
```

### Count DNA bases and calculate GC percentage

```python
sequence = "ATGGCCCTG"
bases = np.array(list(sequence))
length = len(bases)
gc_count = np.sum((bases == "G") | (bases == "C"))
gc_percent = 100 * gc_count / length if length else 0

base_values, counts = np.unique(bases, return_counts=True)
count_dict = dict(zip(base_values, counts))
most_common = base_values[np.argmax(counts)]
```

- `(bases == "G") | (bases == "C")` makes a Boolean array that is true for G **or** C.
- `np.sum(...)` counts the true values.
- `np.unique(..., return_counts=True)` returns the unique values and their counts.
- `np.argmax(counts)` gives the position of the largest count.

For a dictionary that always reports A, T, G and C, including zero counts:

```python
for base in ["A", "T", "G", "C"]:
    print(base, count_dict.get(base, 0))
```

## 3. Pandas core data structures

### Series and DataFrame

- A **Series** is a one-dimensional labelled array.
- A **DataFrame** is a two-dimensional table with labelled rows and columns.

```python
s = pd.Series([1, 3, 5, 6, 8])

# Create a DataFrame from a dictionary (each value is a column)
data = {
    "Name": ["John", "Jane", "Joe"],
    "Age": [23, 24, 25],
}
df = pd.DataFrame(data)

# Or from rows (list of lists)
rows = [["John", 23], ["Jane", 24], ["Joe", 25]]
df2 = pd.DataFrame(rows, columns=["Name", "Age"])
```

### Read and write files

```python
df = pd.read_csv("data.csv")
df = pd.read_table("data.tsv", sep="\t")

# Save results
 df.to_csv("cleaned.csv", index=False)
# df.to_excel("cleaned.xlsx", index=False)
# df.to_json("cleaned.json")
```

`index=False` prevents the DataFrame index from being written as an extra column. For tab-separated data, `pd.read_table()` is convenient; `pd.read_csv(..., sep="\t")` also works.

### Load expression data from a URL

```python
url = (
    "https://media.githubusercontent.com/media/ahmedmoustafa/"
    "gene-expression-datasets/main/datasets/irf6/irf6.tsv"
)
df = pd.read_table(url, index_col=0)
```

`index_col=0` uses the first column as row labels (for example, gene identifiers), rather than treating it as a regular data column.

## 4. Inspect, summarize and sort a DataFrame

```python
df.head()          # first 5 rows
df.tail()          # last 5 rows
df.shape           # (number of rows, number of columns)
df.columns         # column labels
df.columns.tolist()# column labels as a Python list
df.dtypes          # data type of each column
df.info()          # concise summary, non-null counts and types
df.describe()      # summary statistics for numerical columns
df.sort_values(by="Age", ascending=False)
```

- `df.shape` returns a tuple `(rows, columns)`.
- `df.dtypes` helps find numbers stored as text or columns with unexpected types.
- `df.describe()` reports numerical summaries such as count, mean, standard deviation, minimum, quartiles and maximum.
- `sort_values()` returns a sorted DataFrame. Use `inplace=True` only if you deliberately want to modify the existing DataFrame.

## 5. Data types

```python
df["Gender"] = df["Gender"].astype("category")
df["Physical Activity Level"] = df["Physical Activity Level"].astype("category")
df["Date"] = pd.to_datetime(df["Date"])
```

Use `astype("category")` for categorical columns when appropriate, and `pd.to_datetime()` for dates/times. Inspect `df.dtypes` before and after conversion.

## 6. Select rows and columns

Assume `df` is a DataFrame with columns such as `Age`, `Gender`, and `Sleep Quality`.

### Select columns and row slices

```python
df["Age"]                 # one column -> Series
df[["Age", "Gender"]]    # multiple columns -> DataFrame
df[0:3]                   # first three rows by position
```

### Label-based selection: `loc` and `at`

```python
df.loc[0]                  # row whose index label is 0
df.loc[0, "Age"]           # value at label 0, column Age
df.loc[:, "Age"]           # all rows, Age column
df.at[0, "Age"]            # fast access to one labelled scalar
```

### Position-based selection: `iloc` and `iat`

```python
df.iloc[0]                 # first row by position
df.iloc[:, 1]              # second column, all rows
df.iloc[0, 1]              # first row, second column
df.iat[0, 1]               # fast access to one positional scalar
```

**Remember:** `loc`/`at` use labels; `iloc`/`iat` use integer positions.

### Boolean filtering

```python
df[df["Age"] > 30]
df[df["Gender"].isin(["m", "f"])]
df[(df["Age"] > 30) & (df["Sleep Quality"] >= 7)]
```

Use `&` for AND and `|` for OR when combining conditions, and wrap each condition in parentheses. Use `.isin([...])` to test whether values belong to a list of options.

## 7. Missing values, duplicates and string cleaning

```python
df.isnull().sum()          # missing-value count per column
df.notnull()               # True where values are present
df.dropna()                # return rows with missing values removed
df.fillna(0)               # return data with missing values replaced by 0

df.duplicated().sum()      # number of duplicated rows
df.drop_duplicates()       # return rows with duplicates removed

df["name"].str.lower()    # lowercase text
df["name"].str.upper()    # uppercase text
df["name"].str.replace("_", " ", regex=False)
```

The examples above return a cleaned result without changing `df` unless you assign the result back or use an appropriate in-place option. Check what missing values mean before deciding whether to drop or fill them; filling all missing values with zero is not always scientifically appropriate.

## 8. Grouping and aggregation

`groupby()` splits rows into groups, then lets you calculate summaries for each group.

```python
# Number of rows per category
df.groupby("Dietary Habits", observed=False).size()

# Mean age for each category
df.groupby("Dietary Habits", observed=False)["Age"].mean()

# Group by two categorical columns
df.groupby(
    ["Dietary Habits", "Physical Activity Level"], observed=False
)["Age"].mean()

# Multiple summaries at once
df.groupby(
    ["Dietary Habits", "Physical Activity Level"], observed=False
).agg({"Age": "mean", "Sleep Quality": "max"})
```

Common aggregation functions: `.sum()`, `.mean()`, `.count()`, `.size()`, `.min()`, `.max()`, and `.agg([...])` or `.agg({...})`.

In the lecture notebook, `observed=False` is used in categorical groupings to request the categories even if some categories have no observed rows.

## 9. Transform data with functions, `apply`, `map` and `replace`

### Create a derived column

```python
df["double_age"] = df["Age"].apply(lambda x: x * 2)
```

### Apply a function row-wise

```python
def sleep_duration(row):
    # Example assumes these columns contain comparable time values.
    if row["Wake-up Time"] > row["Bedtime"]:
        return row["Wake-up Time"] - row["Bedtime"]
    return row["Wake-up Time"] + pd.Timedelta(days=1) - row["Bedtime"]

# Use axis=1 to pass each row as a Series
# df["Sleep Duration"] = df.apply(sleep_duration, axis=1)
```

Time calculations depend on how the input columns are represented. Convert text to datetimes/timedeltas as appropriate before subtracting them; the snippet is a pattern to adapt to your dataset.

### `map`, `replace` and `assign`

```python
# Map categories to numeric codes (unmapped values become missing)
df["activity_code"] = df["Physical Activity Level"].map(
    {"low": 1, "medium": 2, "high": 3}
)

# Replace values in an existing column
df["Physical Activity Level"] = df["Physical Activity Level"].replace(
    {1: "low", 2: "medium", 3: "high"}
)

# Create a column based on existing columns
df = df.assign(total=lambda x: x["column1"] + x["column2"])
```

- `Series.map()` transforms each value in a Series according to a mapping or function.
- `.replace()` substitutes specified values and leaves other values unchanged.
- `.assign()` returns a DataFrame with added or updated columns.

## 10. Combine DataFrames: `merge`, `join`, `concat`

### `merge()` — combine using key columns

```python
merged = pd.merge(left, right, on="customer_id", how="inner")
```

Join types:

| `how=` | Result |
|---|---|
| `"inner"` | Only keys present in both DataFrames (intersection) |
| `"outer"` | All keys from both; unmatched values are missing (`NaN`) |
| `"left"` | All keys from the left DataFrame plus matching right rows |
| `"right"` | All keys from the right DataFrame plus matching left rows |

You can merge on multiple keys using `on=["key1", "key2"]`. If the key column names differ, use `left_on=` and `right_on=`.

### `join()` — commonly combine by index

```python
joined = df1.join(df2, how="left")
```

`DataFrame.join()` is convenient when the matching labels are in the DataFrame indexes. It supports `left`, `right`, `inner`, and `outer` joins.

### `concat()` — stack rows or align columns

```python
stacked = pd.concat([df1, df2], axis=0)       # stack rows
side_by_side = pd.concat([df1, df2], axis=1)  # place columns side by side
aligned = pd.concat([df1, df2], axis=1, join="inner")

hierarchical = pd.concat([df1, df2], keys=["df1", "df2"])
```

- `axis=0`: concatenate along rows.
- `axis=1`: concatenate along columns.
- `keys=` adds an outer level to the resulting index.
- Unlike `merge()`, `concat()` does not require a common key column; alignment follows the axis and indexes.

## 11. NumPy + Pandas: gene-expression example

The exercise solution uses an IRF6 expression table with columns `WT1`, `WT2`, `WT3`, `KO1`, `KO2`, and `KO3`.

```python
url = (
    "https://media.githubusercontent.com/media/ahmedmoustafa/"
    "gene-expression-datasets/main/datasets/irf6/irf6.tsv"
)
df = pd.read_table(url, index_col=0)

print(df.shape)
print(df.head())
print(df.columns.tolist())

wt_cols = ["WT1", "WT2", "WT3"]
ko_cols = ["KO1", "KO2", "KO3"]
mean_wt = df[wt_cols].mean(axis=1)
mean_ko = df[ko_cols].mean(axis=1)

overall_mean = df.mean(axis=1)
top_10 = overall_mean.nlargest(10)
high_expression = overall_mean[overall_mean > 10000]
```

- `axis=1` calculates a mean across columns for each row/gene.
- `.nlargest(10)` returns the ten largest values.
- `overall_mean > 10000` creates a Boolean filter for genes whose mean expression is greater than 10,000.

## 12. Plot with Matplotlib

### Basic workflow

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
# Add a plot here
plt.title("Plot title")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.tight_layout()
plt.show()
```

### Bar plot: counts of DNA bases

```python
bases = ["A", "T", "G", "C"]
counts = [count_dict.get(base, 0) for base in bases]

plt.figure(figsize=(6, 4))
plt.bar(bases, counts)
plt.title("Base Counts in Human Insulin CDS")
plt.xlabel("Base")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("base_counts_bar.png", dpi=150)
plt.show()
```

### Histogram: distribution of a numerical variable

```python
df["Age"].hist(bins=15)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
```

### Pie chart: category proportions

```python
df["Physical Activity Level"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Physical Activity Level")
plt.ylabel("")  # hide the default y-axis label
plt.tight_layout()
plt.show()
```

### Scatter plot: relationship between two numerical variables

```python
df.plot.scatter(x="Calories Burned", y="Sleep Quality")
plt.title("Calories Burned vs Sleep Quality")
plt.tight_layout()
plt.show()
```

### Scatter plot: mean WT vs mean KO expression

```python
plt.figure(figsize=(6, 6))
plt.scatter(mean_wt, mean_ko, alpha=0.3, s=10)

lims = [0, max(mean_wt.max(), mean_ko.max())]
plt.plot(lims, lims, "k--", alpha=0.5, label="Equal expression")
plt.title("Mean Expression: WT vs KO")
plt.xlabel("Mean WT")
plt.ylabel("Mean KO")
plt.legend()
plt.tight_layout()
plt.savefig("wt_vs_ko_scatter.png", dpi=150)
plt.show()
```

Points above the diagonal have a higher KO value than WT; points below it have a higher WT value, assuming WT is on the x-axis and KO is on the y-axis.

### Bar plot: top ten genes

```python
plt.figure(figsize=(8, 4))
plt.bar(range(len(top_10)), top_10.values)
plt.xticks(range(len(top_10)), top_10.index, rotation=45, ha="right")
plt.title("Top 10 Highest Expressed Genes")
plt.xlabel("Gene")
plt.ylabel("Mean Expression")
plt.tight_layout()
plt.savefig("top_genes_bar.png", dpi=150)
plt.show()
```

### Save plots

```python
plt.savefig("figure.png", dpi=150, bbox_inches="tight")
```

Call `savefig()` before `show()` in the usual workflow. `dpi` controls image resolution; `bbox_inches="tight"` helps avoid clipped labels.

## 13. Quick reference table

| Task | Code |
|---|---|
| Make NumPy array | `np.array([1, 2, 3])` |
| Number of dimensions | `np.ndim(arr)` |
| Array shape | `arr.shape` |
| Total elements | `arr.size` |
| Evenly spaced values | `np.linspace(0, 1, 5)` |
| Reverse array | `arr[::-1]` |
| Unique values and counts | `np.unique(arr, return_counts=True)` |
| Read CSV | `pd.read_csv("file.csv")` |
| Read TSV | `pd.read_table("file.tsv", index_col=0)` |
| Inspect first rows | `df.head()` |
| DataFrame dimensions | `df.shape` |
| Column data types | `df.dtypes` |
| Summary statistics | `df.describe()` |
| Select column | `df["Age"]` |
| Select by labels | `df.loc[row_label, "Age"]` |
| Select by position | `df.iloc[row_pos, col_pos]` |
| Boolean filter | `df[df["Age"] > 30]` |
| Missing values | `df.isnull().sum()` |
| Remove duplicates | `df.drop_duplicates()` |
| Group and summarize | `df.groupby("group")["value"].mean()` |
| Combine by key | `pd.merge(df1, df2, on="id", how="inner")` |
| Stack DataFrames | `pd.concat([df1, df2], axis=0)` |
| Bar plot | `plt.bar(x, y)` |
| Scatter plot | `plt.scatter(x, y)` |
| Histogram | `df["Age"].hist(bins=15)` |
| Save plot | `plt.savefig("figure.png", dpi=150)` |

## Key takeaways

- NumPy arrays support efficient element-wise calculations, slicing, and counting.
- Pandas Series and DataFrames are labelled structures for data analysis.
- Inspect data early with `.head()`, `.shape`, `.dtypes`, and `.describe()`.
- Use `loc`/`at` for labels and `iloc`/`iat` for positions.
- Check missing values, duplicates, and data types before analysis.
- `groupby()` and aggregation summarize data by category; `merge()`, `join()`, and `concat()` combine datasets in different ways.
- Matplotlib plots should have clear titles and axis labels; save figures when they are part of your workflow.

## Further reference

- Pandas documentation: <https://pandas.pydata.org/docs/>
- Pandas user guide: <https://pandas.pydata.org/docs/user_guide/>
