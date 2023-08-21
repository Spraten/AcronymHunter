import re
import io

# List of patterns to match
patterns = [
    r'\$\w+',
    r'0x\d+',
    r'\w+_\w+',
    r'\w+-\w+',
    r'\w+\.\w+',
    r'[A-Z][a-z]+[A-Z]\w+'
]

def find_matches(filename):
    """Search for the given patterns in a text file and return them as a sorted and unique list."""
    matches = []
    try:
        with io.open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            for pattern in patterns:
                matches += re.findall(pattern, text)
    except UnicodeDecodeError:
        with io.open(filename, 'r', encoding='latin-1') as file:
            text = file.read()
            for pattern in patterns:
                matches += re.findall(pattern, text)
    
    # Remove duplicates and sort
    matches = sorted(set(matches))
    return matches

def save_to_file(entries):
    """Save the list of matches to the output file."""
    with io.open("out.txt", 'w',) as file:
        for match in entries:
            file.write(match + '\n')

if __name__ == "__main__":
    entries = find_matches("input.txt")
    save_to_file(entries)
