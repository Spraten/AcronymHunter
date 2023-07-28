import re
import io

def find_abbreviations(filename):
    """Search for abbreviations and acronyms in a text file and return them as a list."""
    with io.open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

        # Pattern for acronyms and abbreviations
        pattern = r'((?:\b[A-Z][a-z]*\b\s*)+\((\b[A-Z]{2,}\b)\))|\b[A-Z]{2,}\b'
        abbreviations = re.findall(pattern, text)

        # Find function calls using provided function
        function_calls = find_function_calls(text)
        
        return abbreviations + [(func, "") for func in function_calls]

def find_function_calls(text):
    # This pattern looks for sequences of word characters followed by ().
    pattern = r'\b(\w+)\(\)'
    functions = re.findall(pattern, text)
    return [func + '()' for func in functions]

def save_to_file(entries):
    """Save the list of abbreviations and functions to the output file."""
    with io.open("out.txt", 'w', encoding='utf-8') as file:
        for match in entries:
            # If it's an abbreviation with acronym
            if match[0]:
                file.write(match[0] + '\n')
            # If it's a standalone acronym
            elif match[1]: 
                file.write(match[1] + '\n')

if __name__ == "__main__":
    entries = find_abbreviations("input.txt")
    save_to_file(entries)
