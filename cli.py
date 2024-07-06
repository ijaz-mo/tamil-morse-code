import argparse
from morse_converter import tamil_to_morse_code, morse_code_to_tamil

def main():
    parser = argparse.ArgumentParser(description='Convert between Tamil text and Morse code.')
    parser.add_argument('-m', '--mode', choices=['tamil_to_morse', 'morse_to_tamil'], default='tamil_to_morse', help='Conversion mode: tamil_to_morse or morse_to_tamil (default: tamil_to_morse)')
    parser.add_argument('input', help='Input text to convert')

    args = parser.parse_args()

    if args.mode == 'tamil_to_morse':
        result = tamil_to_morse_code(args.input)
    else:
        result = morse_code_to_tamil(args.input)

    print(result)

if __name__ == '__main__':
    main()
