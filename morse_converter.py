import json

# Load the JSON file
with open('morse_mappings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Generate morse_to_tamil by reversing tamil_to_morse
tamil_to_morse = data['tamil_to_morse']
morse_to_tamil = {v: k for k, v in tamil_to_morse.items()}

def tamil_to_morse_code(tamil_text):
    return ' '.join(tamil_to_morse.get(char, '') for char in tamil_text)

def morse_code_to_tamil(morse_code):
    return ''.join(morse_to_tamil.get(code, '') for code in morse_code.split())

data['morse_to_tamil'] = morse_to_tamil
