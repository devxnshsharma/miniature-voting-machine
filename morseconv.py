MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..',   'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '@': '.--.-.', '#': '#', '$': '...-..-', '%': '----.',
    '&': '.-...', '-': '-....-', '_': '..--.-', '=': '-...-', '+': '.-.-.',
    '/': '-..-.', '\\': '\\', '.': '.-.-.-', ',': '--..--', '!': '-.-.--',
    '?': '..--..', ':': '---...', ';': '-.-.-.', '"': '.-..-.', '\'': '.----.',
    '(': '-.--.', ')': '-.--.-'
}

def encode_morse(text):
    morse_output = []
    for char in text:
        if char in MORSE_CODE:
            morse_output.append(MORSE_CODE[char])
        elif char == ' ':
            morse_output.append('/')
        else:
            raise Exception(f"Invalid character: {char}")
    return ' '.join(morse_output)

def decode_morse(morse_text):
    text_output = ''
    morse_words = morse_text.split('/')
    for word in morse_words:
        word_letters = word.split(' ')
        for letter in word_letters:
            if letter in MORSE_CODE.values():
                text_output += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(letter)]
            elif letter == '':
                text_output += ' '
            else:
                raise Exception(f"Invalid Morse code: {letter}")
    return text_output

print("\n- - - WELCOME TO THE MORSE CODER - - -")

while True:
    print("\nOptions:")
    print("1. Encode to Morse code")
    print("2. Decode from Morse code")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        try:
            text = input("Enter the text to encode: ").upper()
            morse = encode_morse(text)
            print(f"Encoded Morse code: {morse}")
        except Exception as e:
            print(e)
    elif choice == 2:
        try:
            morse = input("Enter the Morse code to decode: ")
            text = decode_morse(morse)
            print(f"Decoded text: {text}")
        except Exception as e:
            print(e)
            
    elif choice == 3:
        print("Exiting . . .\n")
        break
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
