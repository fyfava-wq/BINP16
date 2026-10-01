# Bash for Bioinformatics – Practice Worksheet

This worksheet covers **90 practice examples** across 9 sections, directly aligned with the course presentation (after removing the Fundamentals section for focus on hands-on skills).  
Each task is grounded in bioinformatics contexts (e.g., FASTQ processing, genomic tools, reproducibility) and uses **real datasets** from ENA (PRJEB8448 for single-end FASTQ, PRJEB7537 for paired-end FASTQ) and RCSB PDB (4KRP chains A and B as FASTA).  

For each task you will find:  
- **Task**: A detailed explanation of the objective, including the precise steps or goal, the bioinformatics context (e.g., why this is useful for handling genomic data), and any assumptions or prerequisites to avoid ambiguity.  
- **Golden solution**: The shortest working command that directly answers the task.  
- **Elegant solution**: A best-practice approach with a one-line explanation.  

Sections mirror the course flow: Navigation, Manipulation (file commands), Dataflow (processes/search), Filters, Package Management/Tools, Utilities/System Interaction, Patterns (regex + operational), Awk Examples, Sed Examples.  

**Assumptions**: GNU coreutils (ls, grep, awk, sed, etc.); Linux environment; files in bio_project/raw/; FASTQ=4-line records (header, sequence, +, quality); Phred+33 encoding (Q<20 ⇔ ASCII < '5'); tools like wget, curl, zgrep, nproc available; no sudo in goldens (HPC-friendly); for compressed search, prefer zgrep to zcat | grep for speed and simplicity; find -printf is GNU-specific (for macOS, use alternatives).

**Why this worksheet matters**: These exercises build practical habits for automating bioinformatics workflows, ensuring reproducibility, and scaling to HPC environments—skills essential for handling large genomic datasets without errors.

**Gotchas across all sections**: Always quote variables ("$f") to handle spaces; uniq requires sorted input; use zgrep for compressed files to simplify pipes.

**Table of Contents**:
- [Section 1: File System Navigation](#section-1-file-system-navigation--10-examples) (skills: pwd, ls, cd, whoami, du, free, nproc)
- [Section 2: Essential File Commands](#section-2-essential-file-commands--10-examples) (skills: mkdir, cp, mv, rm, head, rsync, wc, zless, tail, echo)
- [Section 3: Processes, Search, and Data Flow](#section-3-processes-search-and-data-flow--10-examples) (skills: >, |, grep, find, top, &, pkill, 2>&1, sort, cat <<EOF)
- [Section 4: Essential Filters](#section-4-essential-filters--10-examples) (skills: grep, cut, sort, uniq, awk, sed, fold, tr)
- [Section 5: Package Management & Essential Tools](#section-5-package-management--essential-tools--10-examples) (skills: apt-get, apt, venv, pip, source, deactivate)
- [Section 6: Everyday Utilities & System Interaction](#section-6-everyday-utilities--system-interaction--10-examples) (skills: gzip, tar, du, wget, curl, export, history, file, clear)
- [Section 7: Essential Regular Expressions & Operational Patterns](#section-7-essential-regular-expressions--operational-patterns--10-examples) (skills: grep -o, grep '^>', grep '{10,}', echo "$F", touch {1,2}, grep '(1|2)', find | xargs, ssh-keygen, sha256sum, cat <<EOF)
- [Section 8: Awk Examples](#section-8-awk-examples--10-examples) (skills: awk for filtering, calculating, reformatting bio data)
- [Section 9: Sed Examples](#section-9-sed-examples--10-examples) (skills: sed for substitutions, deletions, editing bio files)

---

## Preparation – Download Data

To ensure reproducibility, run this block once to set up the project directory, download datasets, and verify integrity (as per data transfers and organization slides). This puts all files in predictable paths under 'bio_project/raw/' and checks for corruption.

```bash
mkdir -p bio_project/{raw,results,scripts,logs} && cd bio_project
# PRJEB8448 singles (human data)
wget -nc -P raw/ ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR769/ERR769583/ERR769583.fastq.gz
wget -nc -P raw/ ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR769/ERR769587/ERR769587.fastq.gz
# PRJEB7537 pairs (horse data)
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR102/003/ERR1021663/ERR1021663_{1,2}.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR102/004/ERR1021664/ERR1021664_{1,2}.fastq.gz
# 4KRP FASTA (protein chains for regex/pattern practice)
curl -sL 'https://www.rcsb.org/fasta/entry/4KRP/display?chain=A' -o raw/4KRP_chainA.fasta
curl -sL 'https://www.rcsb.org/fasta/entry/4KRP/display?chain=B' -o raw/4KRP_chainB.fasta
# Sample VCF/BED for filters/regex (create small tabular files)
echo -e "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\nchr1\t100\t.\tA\tG\t50\tPASS\nchr2\t200\t.\tC\tT\t30\tPASS\nchrM\t300\t.\tG\tA\t10\tLOW" > raw/sample.vcf
echo -e "chr1\t10\t20\nchr2\t30\t40\nchrX\t50\t60" > raw/regions.bed
# Sanity check: list files with sizes and verify gzip integrity
printf '%s\n' raw/*.fastq.gz raw/*.fasta raw/*.vcf raw/*.bed | xargs -r ls -lh && for f in raw/*.gz; do gzip -t "$f" || echo "Corrupt file: $f"; done
# Real MD5 verification example (MD5s from ENA https://www.ebi.ac.uk/ena/browser/view/PRJEB8448?show=reads; compare calculated to expected)
md5sum raw/ERR769583.fastq.gz > raw/ERR769583.fastq.gz.md5 && cat raw/ERR769583.fastq.gz.md5  # Compute local MD5
# Note: Visit ENA link above, find MD5 for ERR769583, replace in echo below, then run to compare (should match if download OK)
echo "5e0f3b6ec51e9019cbb890c95e98fcd5  raw/ERR769583.fastq.gz" | md5sum -c -  
md5sum raw/ERR769587.fastq.gz > raw/ERR769587.fastq.gz.md5 && echo "7ebedb8fd1cf11f2020659b058bdea85  raw/ERR769587.fastq.gz" | md5sum -c -  # Repeat for second file
# For paired files, visit ENA, find MD5s, compute local, compare manually
```

**Why this preparation matters**: Setting up a structured project with integrity checks prevents common errors like truncated downloads or path mismatches, common in real NGS pipelines.

---

## Section 1: File System Navigation – 10 examples

**Why this section matters**: Mastering navigation ensures you can locate and organize large genomic datasets in HPC environments, avoiding misplaced results or permission issues.

### Practice 1
**Task**: Determine your current working directory to confirm you are in the bio_project folder before processing any data; this prevents accidental overwrites in system directories and is essential for reproducible workflows in shared HPC systems where paths must be absolute or relative correctly.

**Answer:**

```bash
pwd
```
### Practice 2
**Task**: List all files and directories in the raw/ folder with detailed information including permissions, sizes in human-readable format, and timestamps, to inspect data before analysis and ensure no hidden files (like .nextflow configs) are overlooked in bioinformatics tool setups.

**Answer:**

```bash
ls -lha bio_project/raw/
```
### Practice 3
**Task**: Change your current directory to the raw/ folder, print the new location to verify, and then return to the previous directory, demonstrating safe navigation that avoids getting lost in deep HPC file trees during multi-step analyses like QC and alignment.

**Answer:**

```bash
cd raw/
pwd
cd -
```
### Practice 4
**Task**: Count the number of hidden files (starting with '.') in your home directory, as bioinformatics tools often use hidden configs like .conda or .nextflow for reproducibility, and knowing how to reveal them helps in troubleshooting environment issues.

**Answer:**

```bash
find ~ -maxdepth 1 -type f -name '.*' | wc -l
```
### Practice 5
**Task**: Print your username and group memberships to check privileges, which is critical in shared HPC clusters where group permissions determine access to biobanks or cloud-mounted storage for large-scale genomic studies.

**Answer:**

```bash
whoami
groups
```
### Challenging 6
**Task**: Measure the total disk space used by the raw/ directory in human-readable format, to assess storage requirements for scaling to larger datasets like multi-omics biobanks, ensuring you don't exceed quotas in HPC or cloud environments.

**Answer:**

```bash
du -sh raw/
```
### Challenging 7
**Task**: Print available RAM and number of CPU cores to evaluate system resources before running memory-intensive tasks like alignment with BWA or variant calling, preventing job failures in HPC schedulers like Slurm.

**Answer:**

```bash
free -h
nproc
```
### Challenging 8
**Task**: Use relative paths to navigate from the bio_project folder to a new temp/ folder one level up (creating it if needed), print the path to verify, then return, to practice flexible navigation for scripting in varying directory structures typical in cloud workflows.

**Answer:**

```bash
mkdir -p ../temp
cd ../temp
pwd
cd -
```
### Optional 9
**Task**: Visualize the structure of the bio_project directory tree up to depth 2, to quickly inspect organization for reproducibility, assuming tree is installed or falling back to ls if not (useful for auditing workflows before submission to journals or compliance).

**Answer:**

```bash
tree -L 2 bio_project
```
### Optional 10
**Task**: Check free disk space on the current filesystem, extracting only the available space for the root mount, to monitor storage during large data transfers like syncing biobanks with rsync, preventing out-of-space errors in pipelines.

**Answer:**

```bash
df -h / | awk 'NR==2 {print $4}'
```
---

## Section 2: Essential File Commands – 10 examples

**Why this section matters**: These commands enable safe organization, copying, and inspection of large sequencing files, reducing human error in workflows like batch QC on FASTQ files.

### Practice 1
**Task**: Create subdirectories raw/, results/, scripts/, and logs/ inside bio_project if they don't exist, to structure your project for reproducible bioinformatics pipelines where raw data is separated from processed results and scripts.

**Answer:**

```bash
mkdir -p bio_project/{raw,results,scripts,logs}
```
### Practice 2
**Task**: Copy the file raw/ERR769583.fastq.gz to the results/ directory without overwriting existing files, verifying the operation with verbose output, to simulate backing up raw data before processing in a workflow.

**Answer:**

```bash
cp -vn raw/ERR769583.fastq.gz results/
```
### Practice 3
**Task**: Rename the file raw/ERR769587.fastq.gz to raw/sample2.fastq.gz interactively to avoid overwrites, then confirm the new name with ls, to practice safe file management in analyses where sample IDs need standardization.

**Answer:**

```bash
mv -i raw/ERR769587.fastq.gz raw/sample2.fastq.gz
ls raw/
```
### Practice 4
**Task**: Safely remove a temporary file (e.g., create temp.txt first if needed), prompting for confirmation, to demonstrate cautious deletion in HPC where rm -r could destroy critical datasets if misused.

**Answer:**

```bash
touch temp.txt
rm -i temp.txt
```
### Practice 5
**Task**: Preview the first 8 lines (2 full reads) of raw/ERR769583.fastq.gz without decompressing to disk, to check read headers and quality before full processing in a sequencing QC step.

**Answer:**

```bash
zcat raw/ERR769583.fastq.gz | head -n 8
```
### Challenging 6
**Task**: Synchronize the raw/ directory to a backup/ directory, preserving permissions and timestamps, with progress display, to model data transfers for biobanks or cloud integration in large-scale genomics.

**Answer:**

```bash
rsync -avP raw/ backup/
```
### Challenging 7
**Task**: Count the number of reads in raw/ERR769583.fastq.gz by calculating lines/4, to perform a sanity check on sequencing depth before alignment, ensuring the file is complete and not truncated.

**Answer:**

```bash
zcat raw/ERR769583.fastq.gz | wc -l | awk '{print $1/4}'
```
### Challenging 8
**Task**: Scroll through the contents of raw/ERR769583.fastq.gz without decompressing to disk, searching for the first 'N' base to inspect for ambiguous sequences, useful for quality assessment in genomic analyses.

**Answer:**

```bash
zless raw/ERR769583.fastq.gz
# Search in less with /N, then press n for the next match.
```
### Optional 9
**Task**: Monitor the last lines of a log file (create logs/pipeline.log with echo if needed) in real-time, to track progress of a running pipeline like FastQC or alignment, essential for long HPC jobs.

**Answer:**

```bash
mkdir -p logs
echo 'Pipeline started' > logs/pipeline.log
tail -f logs/pipeline.log
```
### Optional 10
**Task**: Create a file data.txt with sequence "ATGC", copy it to copy.txt, count its lines, and remove the copy interactively, to practice a full file management cycle in a safe, reversible way for learning.

**Answer:**

```bash
echo 'ATGC' > data.txt
cp data.txt copy.txt
wc -l data.txt
rm -i copy.txt
```
---

## Section 3: Processes, Search, and Data Flow – 10 examples

**Why this section matters**: These techniques allow building efficient pipelines without temporary files, crucial for handling massive sequencing data in memory-limited environments.

### Practice 1
**Task**: Redirect the first 8 lines of raw/ERR769583.fastq.gz to preview.txt while logging any errors to errors.log, to separate results from diagnostics in a QC step, ensuring clean outputs for reproducibility.

**Answer:**

```bash
head -n 8 raw/ERR769583.fastq.gz > preview.txt 2> errors.log
```
### Practice 2
**Task**: Pipe the output of zcat raw/ERR769583.fastq.gz to head and then count the lines, to demonstrate data flow without disk writes, useful for quick sanity checks on large FASTQ files in pipelines.

**Answer:**

```bash
zcat raw/ERR769583.fastq.gz | head -n 8 | wc -l
```
### Practice 3
**Task**: Search for 'chr1' lines in raw/sample.vcf, counting the matches, to filter variants by chromosome in genomic studies, providing a quick summary without loading the full file.

**Answer:**

```bash
grep -c 'chr1' raw/sample.vcf
```
### Practice 4
**Task**: Find all .fastq.gz files in the raw/ directory recursively and list them with details, to locate sequencing data in nested folders, common in multi-sample projects.

**Answer:**

```bash
find raw/ -type f -name '*.fastq.gz' -exec ls -lh {} +
```
### Practice 5
**Task**: Display the top processes by CPU usage in batch mode for one iteration, filtering for any zcat processes, to monitor resource usage during data decompression in HPC.

**Answer:**

```bash
ps aux --sort=-%cpu | grep '[z]cat' | head
```
### Challenging 6
**Task**: Run zcat on raw/ERR769583.fastq.gz in the background, redirecting output to /dev/null and errors to logs/decomp.log, to simulate non-blocking decompression while preparing other steps in a pipeline.

**Answer:**

```bash
zcat raw/ERR769583.fastq.gz > /dev/null 2> logs/decomp.log &
```
### Challenging 7
**Task**: Identify and force-kill any running zcat processes matching the pattern, or report if none are running, to clean up stuck jobs in shared systems without wasting resources.

**Answer:**

```bash
pkill -x zcat || echo 'No zcat processes found'
```
### Challenging 8
**Task**: Combine stdout and stderr when attempting to list a non-existent file, saving to out.log, then preview the log, to demonstrate stream management for debugging tool errors in workflows.

**Answer:**

```bash
ls does_not_exist > out.log 2>&1
head out.log
```
### Optional 9
**Task**: Sort the lines of raw/sample.vcf using input redirection from the file, saving the sorted output to sorted.vcf, to prepare data for tools that require sorted input like bedtools.

**Answer:**

```bash
sort < raw/sample.vcf > sorted.vcf
```
### Optional 10
**Task**: Create a multi-line BED file inline using a here document, including a header, save to temp.bed, make it executable if needed, and preview, to generate config files for genomic interval operations.

**Answer:**

```bash
cat <<'EOF' > temp.bed
#CHROM	START	END
chr1	10	20
chr2	30	40
chrX	50	60
EOF
cat temp.bed
```
---
