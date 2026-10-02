# Bash III — Cheat Sheet

**Course:** BINP16  
**Class date:** 10-02

## 1. Regular Expressions (Regex)

Regex is a language for describing search patterns in text. In bioinformatics it is useful for FASTA headers, FASTQ reads, VCF records, motifs, and format validation.

### Character classes

```text
[ATGC]       one DNA base
[0-9]        one digit
[A-Z]        one uppercase letter
[^ATGC]      one character that is NOT A, T, G, or C
```

Examples:

```bash
grep "BRCA1" genes.txt
grep "[^ATGC]" reads.txt
grep "[AT]G[CT]" motifs.txt
```

## 2. Anchors

```text
^pattern       start of line
pattern$       end of line
\bpattern\b    whole word
```

Examples:

```bash
grep "^>" genome.fa
grep "PASS$" variants.vcf
grep -E "\bBRCA1\b" annot.txt
grep "^@RG" aln.sam
```

## 3. Quantifiers

```text
*       zero or more
+       one or more
?       zero or one
{n,m}   n to m repetitions
{n,}    n or more
```

Examples:

```bash
grep "N+" reads.fastq
grep -E "colou?r" words.txt
grep -E "[ATGC]{8,12}" barcodes.txt
grep -E "A{10,}" genome.fa
```

## 4. Grouping and OR

```text
(...)    group
|        OR
```

Example:

```bash
grep -E "(BRCA1|BRCA2|TP53)" genes.txt
grep -E "(chr1|chr2):[0-9]+" coords.bed
```

The lecture also mentions non-capturing groups:

```text
(?:...)
```

## 5. Dot and wildcards

```text
.       any single character
.*      greedy match
.*?     lazy match
```

Example:

```bash
grep "A.C" file.txt
grep "^@" reads.fastq
```

Be careful with greedy matches because they can capture too much.

## 6. Escaping

Special regex characters include:

```text
. ^ $ * + ? { } [ ] | ( ) \
```

Use `\` when you want the literal character.

```bash
grep "\.vcf$" files.txt
grep "^#" variants.vcf
```

Here `\.` means a literal dot, so `\.vcf$` matches filenames ending in `.vcf`.

## 7. Useful bioinformatics regex

```bash
grep "^>" genome.fa
grep -oE "[ATGC]{3}" cds.fa
grep "N+" reads.fastq
grep "[^ATGCN]" reads.fastq
grep -E "TATA[AT]{2}" promoters.fa
grep "PASS$" variants.vcf
grep -P "^chr[0-9XY]+\t[0-9]+\t[0-9]+" regions.bed
grep "^@RG" aln.sam
grep -E "^[ATGC]{8,16}$" barcodes.txt
grep -E "[ATGC]{20,}" guides.fa
grep -E "(BRCA1|BRCA2)" genes.txt
```

## 8. Quoting

### Single quotes

```bash
echo 'Hello, $USER'
```

`$USER` is treated literally.

### Double quotes

```bash
echo "Hello, $USER"
```

`$USER` is expanded.

Always quote variables:

```bash
rm -i "$file"
```

This safely handles filenames containing spaces or special characters.

## 9. Command substitution

Use:

```bash
$(command)
```

Example:

```bash
echo "Run at $(date)"
```

Prefer `$(...)` over older backticks:

```bash
`date`
```

## 10. Brace expansion

Generate lists with:

```text
{A,B}
{1..3}
```

Examples:

```bash
touch sample_{R1,R2}.fastq.gz
mkdir -p data/{raw,results,logs}
```

The first creates two files; the second creates three directories.

## 11. Here-documents

Create multi-line input directly:

```bash
cat <<EOF > samples.tsv
sampleA	R1.fq.gz	R2.fq.gz
sampleB	R1.fq.gz	R2.fq.gz
EOF
```

Use a quoted delimiter to disable expansion:

```bash
cat <<'EOF' > file.txt
$USER
$(date)
EOF
```

Useful for small config files, scripts, and reproducible examples.

## 12. Here-strings

Send a short string to standard input:

```bash
line="chr1 100 PASS"
grep -n "PASS" <<< "$line"
```

Similar to:

```bash
echo "$line" | grep -n "PASS"
```

Another example:

```bash
awk '{print toupper($0)}' <<< "acgt"
```

Use here-strings for small inputs; use files for large data.

## 13. `xargs`

Safe batch processing:

```bash
find . -name "*.fastq.gz" -print0 | xargs -0 ls -lh
```

`-print0` + `-0` safely handles filenames containing spaces.

Process a fixed number at a time:

```bash
xargs -n 10
```

Parallel processing:

```bash
xargs -P 4
```

On shared HPC systems, use parallelism responsibly.

Example:

```bash
find . -name "*.tsv" -print0 | xargs -0 wc -l
```

## 14. SSH keys

Generate an Ed25519 key:

```bash
ssh-keygen -t ed25519
```

SSH configuration is stored in:

```text
~/.ssh/config
```

SSH keys can make repeated HPC access easier and more secure.

## 15. Symbolic links

Create a symbolic link:

```bash
ln -s data data_link
```

Here:

```text
data       = original
data_link  = symbolic link
```

Symlinks let you refer to data without copying it.

If the original target is moved, the symlink may become broken.

## 16. Checksums

Create a SHA-256 checksum:

```bash
sha256sum samples.tsv > samples.tsv.sha256
```

Verify it:

```bash
sha256sum -c samples.tsv.sha256
```

Successful verification looks like:

```text
samples.tsv: OK
```

## 17. Quick reference

| Pattern / command | Meaning |
|---|---|
| `^` | start of line |
| `$` | end of line |
| `.` | any single character |
| `*` | zero or more |
| `+` | one or more |
| `?` | zero or one |
| `{n,m}` | n–m repetitions |
| `[ABC]` | one character from set |
| `[^ABC]` | one character NOT in set |
| `(A|B)` | A OR B |
| `\.` | literal dot |
| `\b` | word boundary |
| `'...'` | no variable expansion |
| `"..."` | variable expansion |
| `$(...)` | command substitution |
| `{A,B}` | brace expansion |
| `{1..3}` | sequence expansion |
| `<<EOF` | here-document |
| `<<<` | here-string |
| `find ... -print0` | null-separated filenames |
| `xargs -0` | safely read null-separated names |
| `ln -s` | symbolic link |
| `sha256sum` | SHA-256 checksum |

## 18. Key patterns to remember

Search at the beginning:

```bash
grep "^pattern" file
```

Search at the end:

```bash
grep "pattern$" file
```

One of several characters:

```bash
grep "[ATGC]" file
```

NOT one of several characters:

```bash
grep "[^ATGC]" file
```

Repetition:

```bash
grep -E "A{10,}" file
```

OR:

```bash
grep -E "(BRCA1|BRCA2)" file
```

Literal dot:

```bash
grep "\.vcf$" files.txt
```

Safe variable:

```bash
rm -i "$file"
```

Generate several names:

```bash
touch sample_{R1,R2}.fastq.gz
```

Safe batch processing:

```bash
find . -name "*.fastq.gz" -print0 | xargs -0 ls -lh
```

Verify a file:

```bash
sha256sum samples.tsv > samples.tsv.sha256
sha256sum -c samples.tsv.sha256
```

## Main takeaway

```text
REGEX
  → precise text matching

QUOTING
  → safe Bash commands

BRACE / COMMAND EXPANSION
  → generate names and reuse command output

HERE-DOCS / HERE-STRINGS
  → feed text directly into commands

find + xargs
  → safe batch processing

SSH KEYS
  → convenient secure remote access

SYMLINKS
  → refer to data without copying it

SHA256
  → verify file integrity
```
