# Automated File Organizer

## Overview

As a computer science student, I regularly download a large number of files, including PDFs, DOCXs, PPTXs, and more to support my coursework. However, this quickly turns my downloads destination into a cluttered mess, making it difficult to find what I need. To solve this, I developed a Python script that automatically organizes files in seconds. This tool categorizes files by type, moving them into designated folders like **Documents**, **Images**, **Videos**, and more, providing an instantly organized directory.

With this, I can keep my Downloads folder clean and easy to navigate, saving me time and helping me focus on my studies.

## Features

- **Automatic File Organization**: Instantly organizes files into categories such as Documents, Images, Videos, Music, Archives, and Scripts.
- **Duplicate Handling**: Renames duplicate files to avoid overwrites by appending an incremental index to the filename.
- **Log File**: Keeps a log of moved files for easy reference and troubleshooting.
- **Exclusion List**: Excludes specified files (such as the log file or the script itself) from being moved.

## Usage

To organize files in a directory, just place this script in the folder you want to organize and run it:

```bash
python auto_organizer.py
