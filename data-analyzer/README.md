# Data Analyzer CLI

A straightforward, beginner-friendly command-line tool that accepts numerical data inputs and calculates descriptive statistical measures without using third-party packages.

## Features

- **Flexible Input:** Accepts numbers separated by spaces or commas (e.g., `10, 20.5, 30` or `10 20.5 30`).
- **Comprehensive Statistics:** Computes count, sum, mean (average), minimum, maximum, and median.
- **Robust Median Logic:** Accurately handles both odd-sized and even-sized dataset lengths.
- **Manual Calculation Functions:** Implemented from scratch using standard loops to build algorithmic understanding for technical interviews.
- **Formatted Summary Report:** Formats decimal outputs neatly using Python f-string specifiers (`:.2f`).

## Python Concepts Learned

- **Lists (`list`):** Collecting numerical items, indexing (`[0]`), slicing (`[1:]`), sorting (`sorted()`), and measuring length (`len()`).
- **String Parsing:** Splitting user text input using `.split()` and replacing delimiter characters with `.replace()`.
- **Loops & Accumulators:** Iterating over elements to compute totals and track extremum values (min/max).
- **Mathematical Logic & Modulo Operator:** Calculating the median by testing odd or even length using `count % 2 != 0` and integer division `//`.
- **Functions & Modularity:** Writing dedicated functions for each statistic with clear input parameters and return values.
- **Exception Handling:** Catching `ValueError` when non-numeric values are submitted.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `data-analyzer` folder:
   ```bash
   cd data-analyzer
   ```
3. Run the script:
   ```bash
   python analyzer.py
   ```

## Example Usage

```text
=============================================
            DATA ANALYZER CLI                
=============================================
Calculate count, sum, mean, min, max, and median
from your numerical datasets.


Enter numbers separated by spaces or commas:
> 15, 8, 42, 23, 4, 16

===================================
       DATA ANALYSIS REPORT        
===================================
  Raw Dataset   : [15.0, 8.0, 42.0, 23.0, 4.0, 16.0]
  Count         : 6
  Sum           : 108.00
  Mean (Average): 18.00
  Minimum       : 4.00
  Maximum       : 42.00
  Median        : 15.50
===================================

Analyze another dataset? (y/n): n

Thank you for using Data Analyzer CLI. Goodbye!
```

## Possible Future Improvements

- Calculate variance and standard deviation.
- Calculate mode (most frequent value) using a dictionary frequency counter.
- Allow reading data points directly from a `.csv` or `.txt` file.
