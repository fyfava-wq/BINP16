# Bash for Bioinformatics — Day 1 Cheat Sheet

> **Class:** Bash I / 09:30  
> **Focus:** Linux navigation, files, permissions, streams, pipes, searching, FASTQ inspection, logging, and remote data transfer.

---

## 1. Command anatomy

Most Bash commands follow:

```bash
command [options] [arguments]
```

Example:

```bash
ls -lh raw/
```

- `ls` = command
- `-lh` = options
- `raw/` = argument

**Important:** `$` shown in lecture notes is the shell prompt. Do **not** type it.

---

# 2. Navigation

### Where am I?

```bash
pwd
```

Print working directory.

### List files

```bash
ls
ls -l       # detailed information
ls -h       # human-readable sizes
ls -a       # include hidden files
ls -lh      # detailed + human-readable
ls -lha     # detailed + human-readable + hidden
```

### Change directory

```bash
cd directory/
cd ..       # one level up
cd ~        # home directory
cd -        # previous directory
cd /home/inf-40-2026/bio_project   # absolute path
cd ../data/                         # relative path
```

Useful habit:

```bash
pwd
ls
```

after changing directories.

### Directory structure

```bash
tree
```

If `tree` is unavailable:

```bash
find . -type d
```

---

# 3. Filesystem concepts

The Linux filesystem starts at `/`.

Common locations:

```text
/       root of filesystem
/home   users' home directories
/usr    system software and libraries
/bin    essential executables
/etc    configuration files
```

Special path symbols:

```text
.       current directory
..      parent directory
~       your home directory
/       filesystem root
```

### Hidden files

Files beginning with `.` are hidden:

```bash
ls -a
```

Examples include `.bashrc` and `.gitignore`.

---

# 4. Identity and permissions

### Who am I?

```bash
whoami
```

### What groups am I in?

```bash
groups
```

or:

```bash
id
```

### Inspect permissions

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

Permissions:

```text
r = read
w = write
x = execute
```

For directories, `x` also means you can enter/traverse the directory.

### `chmod`

```bash
chmod u+x script.sh
```

Give the owner execute permission.

Who:

```text
u = user/owner
g = group
o = others
a = all
```

Actions:

```text
+ = add
- = remove
= = set exactly
```

Examples:

```bash
chmod u+x script.sh
chmod o-w notes.txt
chmod a+r file.txt
chmod go-rwx secret.txt
```

Numeric permissions:

```text
r = 4
w = 2
x = 1

7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---
```

Common examples:

```bash
chmod 755 program
chmod 644 file.txt
```

---

# 5. System resources

```bash
uname -a       # kernel / OS information
lscpu          # CPU information
free -h        # RAM
df -h          # filesystem disk space
du -sh *       # size of items in current directory
nvidia-smi     # GPU information, if available
```

For a specific directory:

```bash
df -h raw/
```

---

# 6. Creating files and directories

```bash
mkdir test
mkdir -p bio_project/{raw,results,scripts,logs}
touch notes.txt
```

Create/write a file:

```bash
echo "ACGT" > data.txt
```

`>` **overwrites** the file.

Append instead:

```bash
echo "another line" >> data.txt
```

`>>` **appends**.

---

# 7. Copy, move, rename, delete

### Copy

```bash
cp file1 file2
cp file1 directory/
cp -r directory1 directory2/
cp -v file1 results/
```

### Move / rename

```bash
mv oldname.txt newname.txt
mv file.txt directory/
mv file1 file2 file3 directory/
```

### Delete

```bash
rm file.txt
rm -i file.txt       # ask before deleting
rm -r directory/
rm -ir directory/    # interactive recursive deletion
```

**Safety:** before destructive commands:

```bash
pwd
ls
```

Avoid blindly using:

```bash
rm -r *
```

---

# 8. Viewing files

### Small files

```bash
cat file.txt
```

### Large files

```bash
less file.txt
```

Inside `less`:

```text
Space = down
q     = quit
/pattern = search
```

### Beginning/end

```bash
head file.txt
head -n 20 file.txt

tail file.txt
tail -n 20 file.txt
```

### Monitor a log continuously

```bash
tail -f logs/pipeline.log
```

Stop with:

```text
Ctrl+C
```

---

# 9. Counting

```bash
wc -l file.txt    # lines
wc -w file.txt    # words
wc -c file.txt    # bytes
```

For FASTQ:

```bash
zcat sample.fastq.gz | wc -l
```

FASTQ has **4 lines per read**, so:

```bash
zcat sample.fastq.gz | wc -l | awk '{print $1/4}'
```

---

# 10. Compression

A `.gz` file is compressed. Do not inspect it with ordinary `head`/`cat` if you want readable content.

Use:

```bash
zcat sample.fastq.gz
zcat sample.fastq.gz | head -n 8
```

Other useful commands:

```bash
gzip file
gzip -t file.gz       # test gzip integrity
zless file.gz         # browse compressed text
```

For compressed searching:

```bash
zgrep "pattern" file.fastq.gz
```

---

# 11. FASTQ structure

A FASTQ record normally has four lines:

```text
@read_header
SEQUENCE
+
QUALITY
```

Therefore:

```text
line 1 → header
line 2 → sequence
line 3 → +
line 4 → quality
```

Preview two complete reads:

```bash
zcat raw/ERR769583.fastq.gz | head -n 8
```

Extract sequence lines:

```bash
zcat raw/ERR769583.fastq.gz | awk 'NR%4==2'
```

Find sequence lines containing `N`:

```bash
zcat raw/ERR769583.fastq.gz | awk 'NR%4==2' | grep N
```

First matching sequence:

```bash
zcat raw/ERR769583.fastq.gz | awk 'NR%4==2' | grep N | head -1
```

---

# 12. Standard streams

Commands use three standard streams:

```text
stdin   0   input
stdout  1   normal output
stderr  2   error messages
```

### Redirect stdout

```bash
ls -l > files.txt
```

Overwrite/create `files.txt`.

### Append stdout

```bash
echo "done" >> log.txt
```

### Redirect errors

```bash
command 2> errors.log
```

### Combine stdout + stderr

```bash
command > out.log 2>&1
```

---

# 13. Pipes

A pipe `|` sends the output of one command into another:

```bash
command1 | command2
```

Examples:

```bash
cat example_cities.txt | cut -f2
cat example_cities.txt | cut -f2 | sort
cat example_cities.txt | cut -f2 | sort | uniq -c
```

For many commands, `cat file | command` is unnecessary; the command can often read the file directly.

---

# 14. Useful filters

### grep

Search for text:

```bash
grep "PASS" file.vcf
grep "^chrX" file.bed
grep -c "PASS" file.vcf
grep -i "pattern" file.txt
```

Important regex anchors:

```text
^pattern   starts with pattern
pattern$   ends with pattern
```

### cut

Extract columns from tab-separated data:

```bash
cut -f1 file.tsv
cut -f1-3 file.tsv
```

### sort

```bash
sort file.txt
sort -k4n file.txt
```

### uniq

```bash
sort file.txt | uniq
sort file.txt | uniq -c
```

`uniq` normally works on **adjacent** identical lines, so sort first when counting unique values.

### awk

Basic form:

```bash
awk '{print $2}' file.txt
```

Print column 2.

```bash
awk '{print "City:", $2}' file.txt
```

For conditions:

```bash
awk '$5 > 20' file.txt
```

Useful FASTQ line selection:

```bash
awk 'NR%4==2'
```

---

# 15. `awk` basics

Important variables:

```text
$0       whole current line
$1       first field
$2       second field
NR       current line/record number
```

Example:

```bash
awk '{print $2}' example.tsv
```

FASTQ positions:

```bash
awk 'NR%4==1'   # headers
awk 'NR%4==2'   # sequences
awk 'NR%4==3'   # + lines
awk 'NR%4==0'   # quality lines
```

---

# 16. Finding files

```bash
find . -name "*.fastq.gz"
find . -type f -name "*.fastq.gz"
find . -type d
```

Difference:

```text
find → searches for files/directories
grep → searches inside text
```

Recursive content search:

```bash
grep -r "mutation" results/
```

---

# 17. Processes

```bash
ps aux
ps aux | grep python
top
htop
```

Stop a foreground command:

```text
Ctrl+C
```

Stop a process by PID:

```bash
kill PID
```

Force kill only if necessary:

```bash
kill -9 PID
```

Background command:

```bash
sleep 60 &
```

Check jobs:

```bash
jobs
```

Bring job 1 to foreground:

```bash
fg %1
```

---

# 18. Logging

Create/overwrite a log:

```bash
echo "Pipeline started" > logs/pipeline.log
```

Append:

```bash
echo "FastQC started" >> logs/pipeline.log
```

Monitor:

```bash
tail -f logs/pipeline.log
```

Save a command's output while still seeing it:

```bash
command | tee logfile
```

Append while displaying:

```bash
command | tee -a logfile
```

---

# 19. History

Show commands used in the current Bash history:

```bash
history
```

Search history:

```bash
history | grep zcat
```

Save history:

```bash
history > logs/0930.txt
```

Remove history numbers when making a clean command list:

```bash
history | sed 's/^ *[0-9]* *//' > commands.txt
```

---

# 20. Data transfer: `scp` vs `rsync`

### `scp` — simple one-off copy

Local → remote:

```bash
scp file.txt user@server:/path/
```

Remote → local:

```bash
scp user@server:/path/file.txt .
```

Copy a directory:

```bash
scp -r user@server:/path/logs ~/bio_project/
```

### `rsync` — synchronize directories

```bash
rsync -av source/ target/
```

With progress:

```bash
rsync -avP source/ target/
```

Example:

```bash
rsync -avP raw/ backup/
```

For repeated server → local syncing:

```bash
rsync -avP user@server:~/bio_project/logs/ ~/bio_project/logs/
```

**Rule of thumb:**

```text
scp    = quick copy
rsync  = synchronization / repeated transfers
```

---

# 21. Useful bioinformatics project structure

A clean project can look like:

```text
bio_project/
├── raw/       # original data — do not modify
├── results/   # analysis outputs
├── scripts/   # scripts
└── logs/      # logs
```

Create it:

```bash
mkdir -p bio_project/{raw,results,scripts,logs}
```

---

# 22. Data integrity

Test compressed files:

```bash
gzip -t raw/*.gz
```

Calculate an MD5 checksum:

```bash
md5sum raw/ERR769583.fastq.gz
```

Save it:

```bash
md5sum raw/ERR769583.fastq.gz > raw/ERR769583.fastq.gz.md5
```

Verify against an expected checksum:

```bash
echo "EXPECTED_MD5  raw/ERR769583.fastq.gz" | md5sum -c -
```

---

# 23. Commands practiced in today's session

Examples from the class session:

```bash
pwd
ls
ls -hl
ls -lha
cd bio_project/
cd raw/
cd ..
cd ~
whoami
groups
id
df -h raw/
lscpu
tree
mkdir test
touch notes.txt data.txt
echo "ACGT" > data.txt
cat data.txt
cp data.txt data_copy.txt
mv notes.txt logs.txt
wc -l data.txt
rm -i data_copy.txt
mkdir BINP17
mv ann-lab/ BINP17
```

FASTQ practice:

```bash
cp -v raw/ERR769583.fastq.gz results/
mv raw/ERR769587.fastq.gz raw/sample2.fastq.gz
head -n 8 raw/ERR769583.fastq.gz
zcat raw/ERR769583.fastq.gz | head -n 8
zcat ERR769583.fastq.gz | wc -l
zcat ERR769583.fastq.gz | wc -l | awk '{print $1/4}'
zcat ERR769583.fastq.gz | awk 'NR%4==2' | grep N | head -1
```

Logging:

```bash
echo "Pipeline started" > logs/pipeline.log
echo "FastQC started" >> logs/pipeline.log
tail logs/pipeline.log
tail -f logs/pipeline.log
history > logs/0930.txt
```

---

# 24. Common mistakes / gotchas

### Don't type the `$`

Lecture:

```text
$ ls
```

You type:

```bash
ls
```

### Don't inspect `.gz` with ordinary `head`

This:

```bash
head raw/file.fastq.gz
```

shows compressed/binary data.

Use:

```bash
zcat raw/file.fastq.gz | head
```

### `>` vs `>>`

```text
>    overwrite
>>   append
```

### `rm` is destructive

Check first:

```bash
pwd
ls
```

Use:

```bash
rm -i file
```

when learning or when unsure.

### `uniq` needs sorted/adjacent input

Use:

```bash
sort file | uniq -c
```

### `find` vs `grep`

```text
find = find files/directories
grep = find text inside files
```

---

# 25. One practical workflow

```bash
cd ~/bio_project
pwd
ls -lh raw/
zcat raw/sample.fastq.gz | head -n 8
zcat raw/sample.fastq.gz | wc -l
zcat raw/sample.fastq.gz | wc -l | awk '{print $1/4}'
echo "QC started" > logs/pipeline.log
tail -f logs/pipeline.log
```

For remote results:

```bash
rsync -avP user@server:~/bio_project/logs/ ~/bio_project/logs/
```

This keeps raw data, results, scripts, and logs organized and makes the workflow easier to reproduce.
