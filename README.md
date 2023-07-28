Of course! Here's the updated `README.md`:

---

# AcronymHunter

Python tool to extract abbreviations, acronyms, and function calls from text files.

## Description

`AcronymHunter` scours text files to identify abbreviations, acronyms, and function calls. Using regular expressions, this script facilitates a comprehensive and precise search to extract relevant patterns from the provided text.

## Features

- Recognizes and extracts abbreviations and acronyms, both standalone and those provided with their full forms.
- Pinpoints function calls within the text.
- Outputs the results to a designated text file.

## Regular Expressions & Samples

1. **For acronyms and abbreviations:** 
    - Regex: `((?:\b[A-Z][a-z]*\b\s*)+\((\b[A-Z]{2,}\b)\))|\b[A-Z]{2,}\b`
    - Sample matches:
      - Full form with acronym: `United Nations (UN)`
      - Standalone acronym: `NATO`

2. **For function calls:** 
    - Regex: `\b(\w+)\(\)`
    - Sample match: `calculate()`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Spraten/AcronymHunter.git
```
2. Navigate to the repository directory:
```bash
cd AcronymHunter
```

## Usage

1. Place the text file you want to analyze into the repository directory. The script is set to read from a file named `input.txt` by default.
2. Run the script:
```bash
python3 AcronymHunter.py
```
3. The findings—abbreviations, acronyms, and function calls—will be stored in `out.txt`.

## Customizing Input/Output

To target a different file or alter the output file name:

1. Open `AcronymHunter.py` in a text editor or IDE of your choice.
2. Change the filename in the `find_abbreviations("input.txt")` line to your intended input filename.
3. (Optionally) To adjust the output filename, modify the `io.open("out.txt", 'w', encoding='utf-8')` line.

## Contributing

Your contributions are invaluable! If you notice room for improvements, discover bugs, or come up with potential fixes, please open an issue or submit a pull request.

## License

This project is open-sourced and distributed under the [MIT License](LICENSE).

---

This enhanced README provides a clearer idea of the regex patterns used in the script, and it also includes sample matches to help users understand the patterns better.
