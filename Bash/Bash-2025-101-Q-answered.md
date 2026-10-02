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

## Section 4: Essential Filters – 10 examples

**Why this section matters**: Filters enable text-based processing of plain-text formats like FASTQ, VCF, BED, allowing reproducible summarization without intermediate files.

### Practice 1
**Task**: Search for lines containing 'PASS' in raw/sample.vcf, counting the matches case-insensitively, to filter high-quality variants in genomic variant calling workflows.

**Answer:**

```bash
grep -ic 'PASS' raw/sample.vcf
```
### Practice 2
**Task**: Extract the first two columns (CHROM and POS) from raw/sample.vcf, skipping the header line, to summarize variant locations for downstream analysis like plotting.

**Answer:**

```bash
awk 'NR>1 {print $1, $2}' raw/sample.vcf
```
### Practice 3
**Task**: Sort the lines of raw/sample.vcf numerically by the second column (POS) in descending order, skipping the header, to rank variants by position for priority review.

**Answer:**

```bash
awk 'NR>1' raw/sample.vcf | sort -k2,2nr
```
### Practice 4
**Task**: Extract the first column (CHROM) from raw/sample.vcf, sort it, and count unique entries with frequencies, ranking by count, to analyze variant distribution across chromosomes.

**Answer:**

```bash
awk 'NR>1 {print $1}' raw/sample.vcf | sort | uniq -c | sort -nr
```
### Practice 5
**Task**: Filter lines from raw/sample.vcf where the second column (POS) is greater than 100, skipping the header, to select variants in a specific genomic region.

**Answer:**

```bash
awk 'NR>1 && $2>100' raw/sample.vcf
```
### Challenging 6
**Task**: Remove the 'chr' prefix from the first column in raw/regions.bed, saving to a backup of the original, and preview the changes, to normalize chromosome names for tool compatibility.

**Answer:**

```bash
cp raw/regions.bed raw/regions.bed.bak
sed 's/^chr//' raw/regions.bed > raw/regions_no_chr.bed
head raw/regions_no_chr.bed
```
### Challenging 7
**Task**: Extract sequences from raw/4KRP_chainA.fasta (skipping headers), break into individual amino acids, sort and count unique with frequencies ranked, to compute amino acid composition in protein analysis.

**Answer:**

```bash
awk 'NR%2==0' 4KRP_chainA.fasta | grep -oE "[A-Z]{1}" | sort | uniq -c | sort -nr
# OR
grep -v '^>' raw/4KRP_chainA.fasta | fold -w1 | sort | uniq -c | sort -nr
```
### Challenging 8
**Task**: Compute the frequency of each amino acid in the sequences of raw/4KRP_chainA.fasta (skipping headers), printing sorted by count, to assess protein composition.

**Answer:**

```bash
grep -v '^>' raw/4KRP_chainA.fasta | fold -w1 | sort | uniq -c | sort -nr
```
## Optional 9:

**Task**: In `raw/4KRP_chainB.fasta`, count the N-glycosylation motif **`N[^P][ST][^P]`** (as defined in Uniprot), allowing matches across line breaks, and also report **1-based start positions**.

**Answer:**

```bash
python - <<'PY'
from pathlib import Path
s=''.join(x.strip() for x in Path('raw/4KRP_chainB.fasta').read_text().splitlines() if not x.startswith('>'))
for i in range(len(s)-3):
    m=s[i:i+4]
    if m[0]=='N' and m[1]!='P' and m[2] in 'ST' and m[3]!='P':
        print(i+1, m)
PY
```

### Optional 10
**Task**: Replace all 'A' residues with 'N' in the sequence lines of raw/4KRP_chainA.fasta (leaving headers intact), saving to masked.fasta, to mask specific residues for privacy or testing in annotations.

**Answer:**

```bash
sed '/^>/! s/A/N/g' raw/4KRP_chainA.fasta > masked.fasta
```
---

## Section 5: Package Management & Essential Tools – 10 examples

**Why this section matters**: Proper package management with apt and Python venvs avoids dependency conflicts, ensuring portable setups for basic data analysis in bioinformatics without overwhelming complexity.

### Practice 1
**Task**: Update the package list and install the 'tree' utility using apt-get, assuming sudo access on a Debian-based system like Ubuntu, to enable directory visualization for project organization without needing advanced managers.

**Answer:**

```bash
sudo apt-get update && sudo apt-get install tree
```
### Practice 2
**Task**: Install the 'htop' process viewer using apt, to monitor system resources like CPU and memory during bioinformatics tasks, confirming installation by running its version.

**Answer:**

```bash
sudo apt install htop && htop --version
```
### Practice 3
**Task**: Install Python 3.11 using apt-get (adds PPA if needed on older systems), to set up a specific version for compatibility with legacy bioinformatics scripts, verifying the installation.

**Answer:**

```bash
sudo apt-get install python3.11 && python3.11 --version
```
### Practice 4
**Task**: Install Python 3.12 using apt, to use a stable version for general data processing, then check the version to confirm.

**Answer:**

```bash
sudo apt install python3.12 && python3.12 --version
```
### Practice 5
**Task**: Install Python 3.13 using apt-get (adds PPA if needed), for accessing the latest features in scripts, verifying with version output.

**Answer:**

```bash
sudo apt-get install python3.13 && python3.13 --version
```
### Challenging 6
**Task**: Create a virtual environment named 'env311' using Python 3.11, activate it, to isolate dependencies for numpy-based array operations in data analysis.

**Answer:**

```bash
python3.11 -m venv env311
source env311/bin/activate
```
### Challenging 7
**Task**: Create 'env312' with Python 3.12, activate, install xgboost for ML models on genomic data, then list installed packages.

**Answer:**

```bash
python3.12 -m venv env312
source env312/bin/activate
pip install xgboost
pip list
deactivate
```
### Challenging 8
**Task**: Create 'env313' with Python 3.13, activate, install pandas for data frames in variant tables, deactivate after listing packages.

**Answer:**

```bash
python3.13 -m venv env313
source env313/bin/activate
pip install pandas
pip list
deactivate
```
### Optional 9
**Task**: Activate 'env311', install numpy for numerical computations, list all packages to confirm, then deactivate, to manage isolated environments for array-based bio data processing.

**Answer:**

```bash
source env311/bin/activate
pip install numpy
pip list
deactivate
```
### Optional 10
**Task**: Switch between env312 and env313: activate env312, list packages, deactivate, then activate env313, list, to practice environment switching for different package needs in workflows.

**Answer:**

```bash
source env312/bin/activate
pip list
deactivate
source env313/bin/activate
pip list
```
---

## Section 6: Everyday Utilities & System Interaction – 10 examples

**Why this section matters**: These utilities handle compression, downloads, and monitoring, key for managing terabyte-scale sequencing data in cloud/HPC.

### Practice 1
**Task**: Copy raw/ERR769583.fastq.gz to temp.fastq, compress it with gzip keeping the original, and list the results, to practice compression for storage efficiency in data archives.

**Answer:**

```bash
cp raw/ERR769583.fastq.gz temp.fastq
gzip -k temp.fastq
ls -lh temp.fastq*
```
### Practice 2
**Task**: Archive the raw/ directory into raw.tgz with compression and verbose output, then check the archive size, to bundle data for sharing or backup in collaborative studies.

**Answer:**

```bash
tar -czvf raw.tgz raw/
ls -lh raw.tgz
```
### Practice 3
**Task**: Measure disk usage for each file in raw/, sorting by size, to identify large datasets and manage storage in resource-limited environments.

**Answer:**

```bash
du -ah raw/ | sort -h
```
### Practice 4
**Task**: Download ERR769583.fastq.gz to raw/ with resume support if interrupted, to handle unstable connections common in large data fetches from ENA.

**Answer:**

```bash
wget -c -P raw/ ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR769/ERR769583/ERR769583.fastq.gz
```
### Practice 5
**Task**: Fetch a JSON response from Ensembl API for ping, parsing with jq if available, to test API integration for annotation in scripts.

**Answer:**

```bash
curl -s 'https://rest.ensembl.org/info/ping' -H 'Content-Type: application/json' | jq .
```
### Challenging 6
**Task**: Export the PATH variable after appending a bin/ directory, saving to path.log, to debug environment setups in tool integrations.

**Answer:**

```bash
export PATH="$PATH:$PWD/bin"
echo "$PATH" > path.log
```
### Challenging 7
**Task**: Search command history for 'zcat' uses, showing the last 5, to recall previous commands for building repeatable scripts (note: Bash must be interactive for history to show entries; test in interactive terminal).

**Answer:**

```bash
history | grep zcat | tail -n 5
```
### Challenging 8
**Task**: Determine the file type of all .gz files in raw/, to confirm compression and format before processing.

**Answer:**

```bash
file raw/*.gz
```
### Optional 9
**Task**: Clear the terminal screen and reprint the current path, to reset focus during long sessions without losing orientation.

**Answer:**

```bash
clear
pwd
```
### Optional 10
**Task**: Download a FASTQ, inspect its type and size, compress if needed, and archive to tgz, confirming each step, to practice a full data ingestion workflow.

**Answer:**

```bash
wget -c -P raw/ ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR769/ERR769583/ERR769583.fastq.gz
file raw/ERR769583.fastq.gz
ls -lh raw/ERR769583.fastq.gz
gzip -f raw/ERR769583.fastq.gz
tar -czvf raw.tgz raw/ERR769583.fastq.gz
```
---

## Section 7: Essential Regular Expressions & Operational Patterns – 10 examples

**Why this section matters**: Regex and patterns enable precise text parsing and safe scripting for genomic formats, bridging to advanced pipelines.

### Practice 1
**Task**: Search for the pattern 'ATC' in raw/4KRP_chainA.fasta, counting occurrences, to find specific motifs in protein sequences for functional analysis.

**Answer:**

```bash
grep -o 'ATC' raw/4KRP_chainA.fasta | wc -l
```
### Practice 2
**Task**: Match and count lines starting with '>' in raw/4KRP_chainA.fasta, to determine the number of sequences in a FASTA file for multi-entry processing.

**Answer:**

```bash
grep -c '^>' raw/4KRP_chainA.fasta
```
### Practice 3
**Task**: Find and count sequences with 10 or more consecutive 'A's in raw/4KRP_chainA.fasta, to detect poly-A regions in proteins.

**Answer:**

```bash
grep -Ec 'A{10,}' raw/4KRP_chainA.fasta
```
### Practice 4
**Task**: Store a filename in a variable and echo it with its size, quoting to handle spaces, to practice safe variable expansion in scripts.

**Answer:**

```bash
F='raw/4KRP_chainA.fasta'; echo "$F"; du -h "$F"
```
### Practice 5
**Task**: Use brace expansion to create files sample1.txt and sample2.txt in one command, to batch generate placeholders for multi-sample analyses.

**Answer:**

```bash
touch sample{1,2}.txt
```
### Challenging 6
**Task**: Match lines with 'chr1' or 'chr2' in raw/sample.vcf using alternation, extracting the CHROM column, to filter specific chromosomes.

**Answer:**

```bash
grep -E '^(chr1|chr2)' raw/sample.vcf | cut -f1
```
### Challenging 7
**Task**: Simulate SSH key generation for bio@lab, with no passphrase, to set up secure remote access for HPC or cloud workflows.

**Answer:**

```bash
ssh-keygen -t ed25519 -C 'bio@lab' -N ''
```
### Challenging 8
**Task**: Compute SHA256 checksum for raw/ERR769583.fastq.gz, save to check.sha, and verify it, to ensure data integrity after download.

**Answer:**

```bash
sha256sum raw/ERR769583.fastq.gz > check.sha
sha256sum -c check.sha
```
### Optional 9
**Task**: Use find to locate .fastq.gz files in raw/, pass null-safe to xargs for parallel line counting (limit to 2 processes), to batch process read counts politely on shared HPC (increase -P only if policy allows).

**Answer:**

```bash
find raw/ -type f -name '*.fastq.gz' -print0 | xargs -0 -n1 -P2 sh -c 'zcat "$0" | wc -l | awk "{print \$1/4}"'
```
### Optional 10
**Task**: Create a simple SLURM-like script inline with here-doc, including a zcat command, make it executable, to orchestrate jobs in HPC.

**Answer:**

```bash
cat <<'EOF' > run_fastq.sh
#!/bin/bash
zcat raw/ERR769583.fastq.gz | head -n 8
EOF
chmod +x run_fastq.sh
./run_fastq.sh
```
---

## Section 8: Awk Examples – 10 examples

**Why this section matters**: Awk is powerful for tabular data processing in bio formats like VCF, BED, allowing one-liners for filtering and stats.

### Practice 1
**Task**: Create a mock VCF with echo if needed, then use awk to print the number of lines (variants), skipping the header, to count entries in variant files for summary stats.

**Answer:**

```bash
awk 'BEGIN{n=0} !/^#/ {n++} END{print n}' raw/sample.vcf
```
### Practice 2
**Task**: Use awk to extract the CHROM and POS columns from raw/sample.vcf, skipping the header, to generate a simple position list for genomic plotting.

**Answer:**

```bash
awk 'NR>1 {print $1, $2}' raw/sample.vcf
```
### Practice 3
**Task**: Filter raw/sample.vcf for QUAL > 20, printing the full lines, skipping header, to select high-quality variants for downstream analysis.

**Answer:**

```bash
awk 'NR>1 && $6>20' raw/sample.vcf
```
### Practice 4
**Task**: Compute the average QUAL from raw/sample.vcf, skipping header, to assess overall variant quality in a dataset.

**Answer:**

```bash
awk 'NR>1 {sum+=$6; n++} END{if(n) print sum/n}' raw/sample.vcf
```
### Practice 5
**Task**: Print lines from raw/regions.bed where end - start > 20, to filter large intervals for genomic feature analysis.

**Answer:**

```bash
awk '$3-$2>20' raw/regions.bed
```
### Optional 6
**Task**: Create a mock FASTQ with echo if needed, then use awk to count reads with average quality >30 (Phred+33), to perform QC filtering.

**Answer:**

```bash
# The lecture/worksheet materials do not provide an awk character-to-ASCII
# conversion function, so there is no fully supported one-line solution
# from the supplied material for this task.
#
# The intended calculation is:
# average Phred quality = sum(ASCII(quality character) - 33) / read length
# and keep reads where that average > 30.
```
### Challenging 7
**Task**: Use awk to add a new column to raw/sample.vcf (QUAL*2), printing the modified lines, skipping header, to normalize scores for comparison.

**Answer:**

```bash
awk 'NR==1 {print; next} {print $0, $6*2}' raw/sample.vcf
```
### Challenging 8
**Task**: Compute min, max, avg POS from raw/sample.vcf, skipping header, to get position stats for variant distribution.

**Answer:**

```bash
awk 'NR>1 {if(n++==0){min=max=sum=$2}else{if($2<min)min=$2;if($2>max)max=$2}sum+=$2} END{if(n) print min, max, sum/n}' raw/sample.vcf
```
### Optional 9
**Task**: Use awk to transpose columns in raw/regions.bed (mock tabular), to reformat for different tool inputs.

**Answer:**

```bash
awk '{print $2, $1, $3}' raw/regions.bed
```
### Optional 10
**Task**: Calculate average read length from mock FASTQ, to assess sequencing quality.

**Answer:**

```bash
awk 'NR%4==2 {sum+=length($0); n++} END{if(n) print sum/n}' mock.fastq
```
---
## Section 9: Sed Examples – 10 examples

**Why this section matters**: Sed excels at stream-editing large text files like FASTQ without creating temporary files, enabling efficient substitutions, deletions, and transformations in bioinformatics pipelines for tasks such as cleaning sequences or normalizing headers.

### Practice 1
**Task**: Normalize headers in raw/ERR1021663_1.fastq.gz by stripping the '/1' suffix from header lines (every 1st of 4 lines), previewing the first 20 lines to verify, to standardize read identifiers for compatibility with tools like aligners that expect clean headers without pair suffixes.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed -E '1~4 s#/1$##' | head -n 20
```
### Practice 2
**Task**: Replace spaces with underscores in header lines of raw/ERR1021663_1.fastq.gz (every 1st of 4 lines), previewing the first 20 lines, to prevent parsing errors in downstream tools that treat spaces as delimiters in FASTQ headers.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed '1~4 s/ /_/g' | head -n 20
```
### Practice 3
**Task**: Extract only the sequence lines from raw/ERR1021663_1.fastq.gz (every 2nd of 4 lines), saving to a text file and previewing the first 20, to isolate sequences for analyses like motif searching without headers or qualities.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed -n '2~4p' > sequences.txt
head -n 20 sequences.txt
```
### Practice 4
**Task**: Convert FASTQ to FASTA by changing '@' to '>' in headers (every 1st of 4 lines) and printing only headers and sequences (skipping '+' and quality), previewing the first 20 lines, to prepare data for tools that require FASTA input like BLAST.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed -n '1~4 s/^@/>/; 2~4p' | head -n 20
```
### Practice 5
**Task**: Mask homopolymers of 6 or more 'A's in sequence lines of raw/ERR1021663_1.fastq.gz (every 2nd of 4 lines) with 'NNNNNN', keeping qualities intact and lengths preserved, to handle low-complexity regions that may cause alignment artifacts.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed '2~4 s/A{6,}/NNNNNN/g' | head -n 20
```
### Challenging 6
**Task**: Remove a known Illumina adapter sequence 'AGATCGGAAGAGC' from sequence lines in raw/ERR1021663_1.fastq.gz (every 2nd of 4 lines), previewing the first 40 lines case-insensitively, to perform basic adapter trimming before alignment, noting this is a simple global replacement not a full trimmer.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed -E '2~4 s/AGATCGGAAGAGC//Ig' | head -n 40
```
### Optional 7
**Task**: Identify reads in raw/ERR1021663_1.fastq.gz where sequences (every 2nd of 4 lines) end with one or more 'N's, printing only their headers (every 1st of 4 lines), to flag ambiguous tail bases for quality filtering in sequencing pipelines.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | awk '
NR%4==1 {h=$0}
NR%4==2 && /N+$/ {print h}
'
```
### optional 8
**Task**: Filter raw/ERR1021663_1.fastq.gz to keep only full 4-line reads where headers contain 'ERR1021663', to subset reads by sample ID in multi-sample FASTQ files for targeted analysis.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | awk '
NR%4==1 {h=$0}
NR%4==2 {s=$0}
NR%4==3 {p=$0}
NR%4==0 {q=$0; if (h ~ /ERR1021663/) print h ORS s ORS p ORS q}
'
```
### Optional 9
**Task**: Append '/1' to headers in raw/ERR1021663_1.fastq.gz (every 1st of 4 lines) that do not already end with '/1' or '/2', previewing the first 16 lines, to standardize single-end reads for paired-end compatible tools.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | awk '
NR%4==1 {
    h=$0
    if (h !~ /\/(1|2)$/) h=h "/1"
    print h
    next
}
NR%4==2 {print}
NR%4==3 {print}
NR%4==0 {print}
' | head -n 16
```
### Optional 10
**Task**: Mask repeats of 'AT' three or more times in sequence lines of raw/ERR1021663_1.fastq.gz (every 2nd of 4 lines) with 'NNNNNN', case-insensitively, to handle dinucleotide repeats that may affect variant calling accuracy.

**Answer:**

```bash
zcat raw/ERR1021663_1.fastq.gz | sed -E '2~4 s/(AT){3,}/NNNNNN/Ig' | head -n 40
```
---

# End of Worksheet
Practice these in your terminal for mastery. Refer back to presentation slides for context!
