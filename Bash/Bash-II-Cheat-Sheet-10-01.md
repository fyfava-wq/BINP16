# Bash II — Cheat Sheet

**Course:** BINP16  
**Class date:** 10-01

> Based on the Bash-II lecture. Main topics: filters, package/environment management, and everyday system utilities.

---

## 1. Filters

Bioinformatics formats such as FASTA, FASTQ, SAM, VCF and BED are often plain text. Unix filters let you inspect, clean and transform them by combining small tools with pipes.

### `grep` — search

```bash
grep "pattern" file
grep "^chrM" variants.vcf
grep -i "pattern" file.txt
grep -v "pattern" file.txt
grep -c "pattern" file.txt
grep -r "pattern" dir/
```

| Option | Meaning |
|---|---|
| `-i` | case-insensitive |
| `-v` | invert / exclude matches |
| `-c` | count matches |
| `-r` | recursive |

### `grep -E` — extended regular expressions

```bash
grep -E "A[TG]C" seqs.txt
```

Matches `ATC` or `AGC`.

Useful regex:

```text
^       start of line
$       end of line
[0-9]   digit
[A-Z]   uppercase letter
```

Examples:

```bash
grep "^chrM" demo.txt
grep "PASS$" demo.txt
grep -E "[0-9]" demo.txt
grep -E "^chr[0-9M]" demo.txt
```

---

## 2. `cut` — extract columns

For tab-separated data:

```bash
cut -f1 file.tsv
cut -f1,3-5 file.tsv
cut -f1,2 variants.vcf
```

Change delimiter:

```bash
cut -d',' -f1 file.csv
```

`-f` = field/column; `-d` = delimiter.

---

## 3. `sort` — order data

```bash
sort file
sort -n file
sort -k2,2n file
sort -k6,6nr variants.vcf
```

Useful options:

```text
-k   sort by key/column
-n   numeric sort
-r   reverse
```

---

## 4. `uniq` — unique values and counts

`uniq` works on adjacent duplicates, so sort first when necessary.

```bash
sort samples.txt | uniq
sort samples.txt | uniq -c
sort samples.txt | uniq -d
```

Common frequency workflow:

```bash
sort file | uniq -c | sort -nr
```

Example:

```bash
cut -f1 barcodes.tsv | sort | uniq -c | sort -nr | head
```

---

## 5. `awk` — filter, calculate, reformat

Basic syntax:

```bash
awk 'condition {action}' file
```

Example:

```bash
awk '$6 > 70' variants.vcf
```

Important variables:

```text
$0    whole line
$1    column 1
$2    column 2
NR    current line number
```

`BEGIN` runs before processing; `END` runs after processing.

```bash
awk 'BEGIN { ... } condition { ... } END { ... }' file
```

Think:

```text
awk = filtering + calculations + reformatting
```

---

## 6. `sed` — stream editing

Substitute:

```bash
sed 's/old/new/' file
```

Examples:

```bash
sed 's/PASS/OK/' variants.vcf > variants_ok.vcf
sed 's/chr//' variants.vcf
sed '/^#/d' file
```

Useful for quick text transformations in pipelines.

---

## 7. Filter mini-pipeline

A typical variant-data workflow:

```bash
grep "^chr1" variants.vcf
cut -f1,2 variants.vcf
sort -k2,2n variants.vcf
sort file | uniq -c
awk '$6 > 30' variants.vcf
sed 's/chr//' variants.vcf
```

Remember:

```text
grep       → search
cut        → columns
sort       → order
uniq       → unique/count
awk        → filter/calculate
sed        → edit/transform
```

---

# Package Management & Environments

## 8. Python `venv`

Create:

```bash
python3 -m venv myenv
```

Specific Python version:

```bash
python3.13 -m venv myenv
```

Activate:

```bash
source myenv/bin/activate
```

Deactivate:

```bash
deactivate
```

Install packages:

```bash
pip install biopython pandas numpy
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install from a requirements file:

```bash
pip install -r requirements.txt
```

Delete an environment:

```bash
rm -rf myenv
```

> `rm -rf` permanently deletes the directory, so use it carefully.

---

## 9. Conda / Mamba

Create a bioinformatics environment:

```bash
conda create -n bioenv python=3.12 samtools -c conda-forge -c bioconda
```

Activate/deactivate:

```bash
conda activate bioenv
conda deactivate
```

Check a tool:

```bash
samtools --version
```

Export an environment:

```bash
conda env export --from-history > env.yml
```

The lecture presents Mamba as a faster Conda solver and notes that Conda includes the libmamba solver by default.

---

## 10. LUNARC / module setup

The lecture gives these commands for LUNARC:

```bash
deactivate
module purge
module spider Anaconda3
module load Anaconda3
source config_conda.sh
which conda
```

On LUNARC, `source config_conda.sh` is required before Conda should work.

---

## 11. Useful utilities

```bash
tree
htop
ncdu
bat
```

| Tool | Purpose |
|---|---|
| `tree` | visualize directories |
| `htop` | monitor CPU/memory/processes |
| `ncdu` | analyze disk usage |
| `bat` | syntax-highlighted file viewer |

---

## 12. Core bioinformatics tools

```text
samtools   → SAM/BAM/CRAM
bcftools   → VCF/BCF
bedtools   → genomic intervals
fastqc     → sequencing quality
bwa        → short-read alignment
bowtie2    → DNA/RNA-seq alignment
minimap2   → long-read alignment
gatk       → variant discovery
```

Install common tools through Bioconda:

```bash
conda install -c bioconda samtools bedtools fastqc
```

---

## 13. Other package ecosystems

```text
pip       → Python packages
apt       → Debian/Ubuntu system packages
dnf/yum   → Linux system packages
brew      → macOS/Linux
Nix/Guix  → declarative/reproducible environments
```

Containers can also be used for reproducible environments. The lecture mentions **Apptainer** as the successor to Singularity and an important HPC container solution.

---

# Everyday Utilities & System Interaction

## 14. Session control

Clear the terminal:

```bash
clear
```

Exit a shell or SSH session:

```bash
exit
logout
```

Keyboard shortcut:

```text
Ctrl+D
```

On HPC/cloud systems: **do not reboot the machine; exit safely instead.**

---

## 15. `gzip` / `gunzip`

Compress:

```bash
gzip file.fastq
```

Creates:

```text
file.fastq.gz
```

Decompress:

```bash
gunzip file.fastq.gz
```

Keep the original while compressing:

```bash
gzip -k file.fastq
```

Common in bioinformatics for FASTQ, VCF and other large files.

---

## 16. `tar` — archive files

Create archive:

```bash
tar -cvf archive.tar dir/
```

Extract:

```bash
tar -xvf archive.tar
```

Create compressed archive:

```bash
tar -czvf archive.tar.gz dir/
```

List contents without extracting:

```bash
tar -tzf archive.tar.gz
```

---

## 17. Inspect files and storage

Identify file type:

```bash
file sample.bam
```

Directory size:

```bash
du -sh dir/
```

Filesystem usage:

```bash
df -h
```

File metadata:

```bash
stat file
```

---

## 18. `echo` and environment variables

Print text:

```bash
echo "Hello Bioinformatics"
```

Show executable search path:

```bash
echo $PATH
```

Set a variable:

```bash
export VAR=value
```

Add a directory to `PATH`:

```bash
export PATH=$PATH:~/bin
```

Check active Conda environment:

```bash
echo $CONDA_DEFAULT_ENV
```

---

## 19. `wget` — download

Basic download:

```bash
wget URL
```

Custom filename:

```bash
wget -O newname.fa.gz URL
```

Resume an interrupted download:

```bash
wget -c URL
```

Run in background:

```bash
nohup wget URL &
```

---

## 20. `curl` — download / APIs

Download:

```bash
curl -O URL
```

Follow redirects:

```bash
curl -L URL
```

Download and extract:

```bash
curl URL | tar -xz
```

`curl` is useful for APIs such as Ensembl, NCBI and GEO.

---

## 21. Command history

Show recent commands:

```bash
history
```

Re-run command number 23:

```bash
!23
```

Search previous commands interactively:

```text
Ctrl+R
```

Search history for a command:

```bash
history | grep samtools
```

Save history:

```bash
history > my_commands.log
```

---

# Example Workflow

A simple workflow from the lecture:

### 1. Download

```bash
wget ftp://.../reads.fastq.gz
```

### 2. Inspect

```bash
file reads.fastq.gz
du -sh reads.fastq.gz
```

### 3. Decompress

```bash
gunzip reads.fastq.gz
```

### 4. Archive results

```bash
tar -czvf project.tar.gz results/
```

### 5. Save environment/path information

```bash
echo $PATH > path.txt
```

### 6. Save command history

```bash
history > my_commands.log
```

---

# Quick Reference

| Command | Purpose |
|---|---|
| `grep` | search patterns |
| `grep -E` | extended regex |
| `cut` | extract columns |
| `sort` | sort data |
| `uniq` | unique/count duplicates |
| `awk` | filter/calculate/reformat |
| `sed` | stream editing |
| `venv` | isolated Python environment |
| `pip` | Python packages |
| `conda` | environments/packages |
| `tree` | directory structure |
| `htop` | process/resource monitor |
| `ncdu` | disk usage |
| `gzip` | compress |
| `gunzip` | decompress |
| `tar` | archive/extract |
| `file` | identify file type |
| `du` | directory/file size |
| `df` | filesystem space |
| `stat` | metadata |
| `wget` | download |
| `curl` | download/API |
| `history` | command history |

---

## Key Takeaways

```text
grep / grep -E  → search
cut             → select columns
sort            → order
uniq            → count/identify duplicates
awk             → filter + calculate
sed             → transform text

venv / conda    → isolated environments
pip             → Python packages
Bioconda        → bioinformatics packages

gzip / gunzip   → compression
tar             → archiving
file / stat     → inspect files
du / df         → storage
wget / curl     → downloads
history         → reproduce commands
```

**Core idea:** combine small Unix tools with pipes to build efficient, reproducible bioinformatics workflows.
