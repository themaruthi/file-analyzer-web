#  Python + Linux File Analyzer

#   Introduction

This is a fun and practical Python project that blends the power of scripting with Linux commands to explore `.txt` files, analyze their contents, and generate useful insights. It’s designed to showcase how we can use Python and Linux together to automate file operations efficiently.

---

##  What This Project Does

1. **Find all `.txt` files** inside any directory you choose (using the Linux `find` command).
2. **Read each file line by line** and count how many lines contain the word **"error"** (case-insensitive).
3. **Create a summary file** (`summary.txt`) that records:
   - File name
   - How many "error" lines were found
   - Total number of lines (calculated using Python and `wc -l`)
   - If there's any mismatch in line count, it flags it
4. **Bonus**: Optionally, it can bundle all `.txt` files into a `.tar.gz` archive using `tar`.

---

## Tech Behind It

- **Python Modules**: `os`, `subprocess`, `sys`
- **Linux Commands**: `find`, `wc -l`, `tar`
- No fancy libraries — just good old standard Python and bash magic!

---

## Sample Output (`summary.txt`)

Here’s a small peek at what the output looks like:
File: log3.txt
Error Count (Python): 1
Total Lines (Python): 100
Total Lines (wc -l): 100
Discrepancy: No
##  Interface Preview
![sampleoutput](sampleoutput.png)
# Project Structure
file-analyzer/
├── app.py             # Main script
├── summary.txt        # Output report
├── text_files_archive.tar.gz  # (Optional) archive of all .txt files
└── README.md          # You're reading it!


# Why This Matters
With just a few lines of code, scripting and shell commands can be used to automate repetitive tasks, scan logs, and generate summaries in real-world DevOps and Data Engineering tasks. That combination of automation and insight is reflected in this project.

# Author
Kadiyala Maruthi Prasad
MSc Data Science 
maruthi2485@gmail.com
