# STRING TO MORSE CODE.


# Making a dict to store mose code, caracters encoding.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Getting a string.
string: str = input("Enter a string to convert: ").upper()
# Converting string to morse code.
def convert_to_morse(string: str):
    for chr in string:
        if chr in morse_code_dict.keys():
            convert_with = morse_code_dict[chr] # morse code of that specific char in loop.
            string = string.replace(chr, convert_with) # replacing with morse code.
    return string

# Printing morse code of string.
print(convert_to_morse(string))
