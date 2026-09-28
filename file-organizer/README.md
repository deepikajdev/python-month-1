# File Organizer CLI

A clean, beginner-friendly file management utility that organizes messy directories by automatically sorting files into categorized folders based on their extensions.

## Features

- **Automatic Classification:** Categorizes files into `Images`, `Documents`, `Videos`, `Music`, and `Others`.
- **Safe Directory Navigation:** Distinguishes between files and directories to avoid altering existing folder hierarchies.
- **Dynamic Folder Creation:** Automatically creates category folders only when needed.
- **Path Validation:** Checks whether the specified path exists and is a valid directory before proceeding.
- **Detailed Summary:** Displays a clean breakdown of how many files were sorted into each category.

## Python Concepts Learned

- **Operating System Operations (`os` module):** Checking existence (`os.path.exists`), checking directory status (`os.path.isdir`), listing directory contents (`os.listdir`), joining paths safely (`os.path.join`), and extracting extensions (`os.path.splitext`).
- **File Management (`shutil` module):** Moving files across folders using `shutil.move()`.
- **Dictionaries & Sets:** Using dictionaries to map category names to lists of extensions and using sets for quick membership checks.
- **Looping & Conditionals:** Iterating through items and using `if / elif / else` branching.
- **String Cleaning:** Sanitizing user input using `.strip()` and stripping quotation marks from copied file paths.
- **Error Handling:** Wrapping file movement actions in `try...except` blocks to handle permission or system errors gracefully.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `file-organizer` folder:
   ```bash
   cd file-organizer
   ```
3. Run the script:
   ```bash
   python organizer.py
   ```

## Example Usage

```text
=============================================
            FILE ORGANIZER CLI               
=============================================
Automatically sorts files into Images, Documents,
Videos, Music, and Others.

Enter the absolute path of the folder to organize: C:\Users\YourName\Downloads

Scanning: C:\Users\YourName\Downloads...
Moved: photo.jpg -> Images/
Moved: invoice.pdf -> Documents/
Moved: presentation.pptx -> Documents/
Moved: song.mp3 -> Music/
Moved: archive.zip -> Others/

===================================
        ORGANIZATION SUMMARY        
===================================
  Images: 1 file(s)
  Documents: 2 file(s)
  Music: 1 file(s)
  Others: 1 file(s)

Total files organized: 5
===================================
```

## Possible Future Improvements

- Add a "dry run" preview mode to inspect moves before executing them.
- Add undo functionality by logging moved paths to a session log file.
- Support user-customizable extension categories via a configuration file.
