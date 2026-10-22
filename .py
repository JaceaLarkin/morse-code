MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", 

    ".": ".-.-.-", ",": "--..--", "?": "..--..", 
    "'": ".----.", "!": "-.-.--", "/": "-..-.", 
    "(": "-.--.", ")": "-.--.-", "&": ".-...", 
    ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", 
    "\"": ".-..-.", "$": "...-..-", "@": ".--.-.",
}


REVERSE_MORSE_DICT = {}
for key, value in MORSE_CODE_DICT.items():
    REVERSE_MORSE_DICT[value] = key



def encode_text(text):
    """Converts text into Morse code and returns the result"""
    words = text.upper().split()
    morse_words = []

    for word in words:
        morse_letters = []

        for char in word:
            if char in MORSE_CODE_DICT:
                morse_letters.append(MORSE_CODE_DICT[char])
            else:
                print(f'[Warning] Character "{char}" not recognized. Skipped.')

        morse_words.append(" ".join(morse_letters))

    return "   ".join(morse_words)



def decode_morse(morse_code):
    """Converts Morse code into text and returns the result"""
    text = ""

    words = morse_code.split("   ")

    for word in words:
        letters = word.split()

        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                text += REVERSE_MORSE_DICT[letter]
            else:
                print(f'[Warning] Sequence "{letter}" not recognized, Skipped.')

        text += " "

    return text.strip()



def main():
    """Displays the menu and lets the user encode, decode, or exit"""
    while True:
        print("\nSelect an option:")
        print("1. Encode text to Morse code")
        print("2. Decode Morse code to text")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to encode: ")
            result = encode_text(text)
            print(result)

        elif choice == "2":
            morse = input("Enter Morse code to decode: ")
            result = decode_morse(morse)
            print(result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option, choose 1, 2, or 3.")


main()




















