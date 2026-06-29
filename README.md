# 🕵️‍♂️ Python Regex Information Extractor

A Python text-processing tool that utilizes the `re` module to intelligently scan raw, unstructured text and extract specific data types (Emails, Phone Numbers, and Dates).

## 🚀 Features
- **Data Extraction:** Accurately isolates emails, dates, and phone numbers from messy text blocks.
- **Data Cleaning:** Uses regex substitution (`re.sub()`) to strip out formatting inconsistencies in phone numbers, returning standardized outputs.
- **Pattern Matching:** Demonstrates the use of `re.findall()`, `re.finditer()`, and regex grouping.

## 🧩 Regex Patterns Explained
The script relies on the following custom patterns:

* **Email Pattern:** `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'`
    * *Matches 1+ valid characters, an `@` symbol, a domain name, a dot, and a 2+ character Top Level Domain.*
* **Date Pattern:** `r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'`
    * *Matches DD/MM/YYYY, DD-MM-YYYY, or DD.MM.YYYY formats using word boundaries.*
* **Phone Cleaning:** `r'\D'`
    * *Used with `re.sub()` to match all non-digit characters and replace them with empty strings, leaving only pure numbers for reformatting.*

## 💻 How to Run
1. Clone the repository.
2. Run the script to see the sample text processed in the terminal:
   ```bash
   python main.py
