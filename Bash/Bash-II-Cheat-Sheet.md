# Git Cheat Sheet — 10-01

> Quick reference for managing course notes and files with Git and GitHub.

## 1. Git vs GitHub

```text
Git      = version control system running on your computer
GitHub   = online service for hosting Git repositories
```

Typical workflow:

```text
edit files → git status → git add → git commit → git push
```

## 2. Check Git

```bash
git --version
git config --list
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## 3. Create or clone a repository

Create a local repository:

```bash
mkdir project
cd project
git init
```

Clone a GitHub repository:

```bash
git clone REPOSITORY_URL
cd REPOSITORY_NAME
```

## 4. Check the repository

```bash
git status
git remote -v
```

`git status` shows the current branch, modified files, untracked files, and staged files.

## 5. Add files

```bash
git add file.md
git add Bash/
git add .
```

Then check:

```bash
git status
```

## 6. Commit changes

```bash
git commit -m "Add Bash cheat sheet"
```

A commit is a saved version/checkpoint of your work.

Good commit messages:

```bash
git commit -m "Add Bash lecture notes"
git commit -m "Update Week 1 README"
git commit -m "Add answered practice questions"
```

## 7. Push to GitHub

```bash
git push
```

For the first push of a new branch:

```bash
git push -u origin main
```

Typical workflow:

```bash
git add .
git commit -m "Update course notes"
git push
```

## 8. Pull changes from GitHub

```bash
git pull
```

Useful after editing something on GitHub and then continuing locally.

## 9. See changes

Unstaged changes:

```bash
git diff
```

Staged changes:

```bash
git diff --staged
```

## 10. View commit history

```bash
git log
git log --oneline
```

Example:

```text
f1366a9 Add Bash notes
cc16baa Initial commit
```

## 11. Files and folders

Git tracks **files**, not empty folders.

This creates a folder in the repository because it contains a file:

```text
Bash/
└── Bash-I-Cheat-Sheet.md
```

Create a folder and file:

```bash
mkdir Bash
touch Bash/README.md
```

Move an existing file into it:

```bash
mkdir Bash
mv Bash-I-Cheat-Sheet.md Bash/
```

Then:

```bash
git add Bash/
git commit -m "Organize Bash notes"
git push
```

## 12. Move / rename files

```bash
git mv oldname.md newname.md
git mv Bash-I-Cheat-Sheet.md Bash/
```

Then commit:

```bash
git commit -m "Move Bash cheat sheet"
```

## 13. Delete a file

Using Git:

```bash
git rm file.txt
git commit -m "Remove file"
git push
```

If you already used normal `rm`:

```bash
rm file.txt
git status
git add -u
git commit -m "Remove file"
```

## 14. Undo / restore changes

Restore an unstaged change:

```bash
git restore file.txt
```

This discards changes in the working file.

Unstage a file:

```bash
git restore --staged file.txt
```

Be careful: restoring a file can discard work.

## 15. `.gitignore`

`.gitignore` tells Git which files should not be tracked.

Create it:

```bash
touch .gitignore
```

Example:

```text
*.log
*.tmp
*.fastq.gz
.env
__pycache__/
```

Then:

```bash
git add .gitignore
git commit -m "Add gitignore"
```

For bioinformatics, `.gitignore` is useful for large raw sequencing files and temporary files that should not be uploaded to GitHub.

## 16. Branches

See branches:

```bash
git branch
```

Create a branch:

```bash
git branch notes-update
```

Switch to it:

```bash
git switch notes-update
```

Create and switch in one command:

```bash
git switch -c notes-update
```

Return to main:

```bash
git switch main
```

## 17. Merge a branch

Switch to the branch receiving the changes:

```bash
git switch main
```

Merge:

```bash
git merge notes-update
```

Then:

```bash
git push
```

## 18. Remote repositories

```bash
git remote -v
```

Add a remote:

```bash
git remote add origin REPOSITORY_URL
```

Change the remote:

```bash
git remote set-url origin REPOSITORY_URL
```

## 19. Your BINP16 course-note workflow

For your repository:

```bash
cd ~/BINP16
```

Check:

```bash
git status
```

Add a new class folder:

```bash
git add Bash/
```

Commit:

```bash
git commit -m "Add Bash class notes"
```

Upload:

```bash
git push
```

After another class:

```bash
git status
git add .
git commit -m "Add notes for 10-01"
git push
```

## 20. Recommended workflow before pushing

```bash
git status
git diff
git add .
git status
git commit -m "Describe the changes"
git push
```

The second `git status` lets you check what is staged before committing.

## 21. The three-stage model

```text
Working directory
       ↓ git add
Staging area
       ↓ git commit
Local repository
       ↓ git push
GitHub / remote repository
```

- **Working directory** — files you are editing.
- **Staging area** — changes selected for the next commit.
- **Local repository** — commits saved on your computer.
- **Remote repository** — the repository hosted on GitHub.

## 22. Most important commands

If you only remember a few:

```bash
git status
git add .
git commit -m "Describe changes"
git push
git pull
git log --oneline
```

Basic cycle:

```bash
git status
git add .
git commit -m "Update notes"
git push
```

## 23. Quick reference

| Command | What it does |
|---|---|
| `git init` | Create a Git repository |
| `git clone URL` | Clone a repository |
| `git status` | Show repository state |
| `git add file` | Stage a file |
| `git add .` | Stage all changes |
| `git commit -m "..."` | Save a version locally |
| `git push` | Upload commits to GitHub |
| `git pull` | Download and integrate remote changes |
| `git log` | Show commit history |
| `git diff` | Show unstaged changes |
| `git branch` | List branches |
| `git switch branch` | Switch branches |
| `git switch -c name` | Create + switch branch |
| `git merge branch` | Merge a branch |
| `git mv` | Move/rename under Git |
| `git rm` | Remove a tracked file |
| `git restore` | Restore/discard changes |
| `git remote -v` | Show remote repository |

## 24. BINP16 repository structure

```text
BINP16/
├── README.md
├── Bash/
│   ├── Bash-I-Cheat-Sheet.md
│   └── Bash-2025-101-Q-answered.md
├── Git/
│   └── Git-Cheat-Sheet-10-01.md
└── ...
```
